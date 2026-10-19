"""Fast deterministic 2D animation primitives for motion-first learning visuals.

The runtime deliberately uses Pillow for drawing and FFmpeg only for optional
video encoding. It is not a general animation engine: it favors small,
inspectable educational scenes with predictable render time.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Any
import math, subprocess
from PIL import Image, ImageDraw, ImageFont

Color = tuple[int, int, int]

def ease_in_out(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)

def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t

@dataclass
class Keyframe:
    start: float
    end: float
    values: dict[str, tuple[float, float]]
    easing: Callable[[float], float] = ease_in_out
    def value(self, name: str, time: float) -> float:
        a, b = self.values[name]
        if self.end <= self.start: return b
        t = self.easing((time - self.start) / (self.end - self.start))
        return lerp(a, b, t)

@dataclass
class Element:
    element_id: str
    kind: str
    props: dict[str, Any]
    keyframes: list[Keyframe] = field(default_factory=list)
    def at(self, time: float) -> dict[str, Any]:
        result = dict(self.props)
        for kf in self.keyframes:
            if kf.start <= time <= kf.end or time >= kf.end:
                for name in kf.values: result[name] = kf.value(name, time)
        return result

@dataclass
class Scene:
    width: int = 1280
    height: int = 480
    fps: int = 12
    duration: float = 6.0
    background: Color = (245, 247, 243)
    elements: list[Element] = field(default_factory=list)
    title: str = ""
    def add(self, element: Element) -> "Scene":
        self.elements.append(element); return self

class Renderer:
    def __init__(self, scene: Scene): self.scene = scene
    def _font(self, size: int):
        try: return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', size)
        except OSError: return ImageFont.load_default()
    def frame(self, time: float) -> Image.Image:
        im = Image.new('RGB', (self.scene.width, self.scene.height), self.scene.background)
        d = ImageDraw.Draw(im)
        if self.scene.title: d.text((40, 24), self.scene.title, font=self._font(34), fill=(76,44,105))
        for element in self.scene.elements:
            p = element.at(time); kind = element.kind
            if kind == 'rect':
                x, y, w, h = [int(p[k]) for k in ('x','y','w','h')]
                fill = p.get('fill', (235,225,245))
                d.rounded_rectangle((x,y,x+w,y+h), radius=int(p.get('radius',12)), fill=tuple(fill) if fill is not None else None, outline=tuple(p.get('outline',(76,44,105))), width=int(p.get('stroke',4)))
                text = p.get('text')
                if text:
                    f = self._font(int(p.get('font_size',22))); box=d.textbbox((0,0),text,font=f)
                    d.text((x+(w-(box[2]-box[0]))/2, y+(h-(box[3]-box[1]))/2-3), text, font=f, fill=tuple(p.get('text_fill',(45,45,42))))
            elif kind == 'arrow':
                x1,y1,x2,y2=[int(p[k]) for k in ('x1','y1','x2','y2')]
                color=tuple(p.get('fill',(242,169,0))); width=int(p.get('stroke',5)); d.line((x1,y1,x2,y2), fill=color, width=width)
                ang=math.atan2(y2-y1,x2-x1); size=12
                pts=[(x2,y2),(x2-size*math.cos(ang-math.pi/6),y2-size*math.sin(ang-math.pi/6)),(x2-size*math.cos(ang+math.pi/6),y2-size*math.sin(ang+math.pi/6))]
                d.polygon(pts, fill=color)
            elif kind == 'label':
                d.text((int(p['x']),int(p['y'])), p['text'], font=self._font(int(p.get('font_size',22))), fill=tuple(p.get('fill',(45,45,42))))
        return im
    def render(self, output_dir: str | Path) -> list[Path]:
        out=Path(output_dir); out.mkdir(parents=True, exist_ok=True); paths=[]
        count=max(1, int(self.scene.duration*self.scene.fps))
        for i in range(count):
            path=out/f'frame_{i:04d}.png'; self.frame(i/self.scene.fps).save(path); paths.append(path)
        return paths
    def export(self, output_dir: str | Path, name: str = 'animation') -> dict[str, Any]:
        frames=self.render(output_dir); out=Path(output_dir); mp4=out/f'{name}.mp4'; gif=out/f'{name}.gif'
        subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(self.scene.fps),'-i',str(out/'frame_%04d.png'),'-c:v','libx264','-pix_fmt','yuv420p','-movflags','+faststart',str(mp4)], check=True)
        images=[Image.open(p).convert('RGB') for p in frames]
        images[0].save(gif, save_all=True, append_images=images[1:], duration=int(1000/self.scene.fps), loop=0)
        return {'ok': True, 'frames': len(frames), 'fps': self.scene.fps, 'duration': self.scene.duration, 'mp4': str(mp4), 'gif': str(gif)}
