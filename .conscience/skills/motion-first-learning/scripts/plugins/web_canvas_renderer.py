"""Generate a dependency-free HTML preview for 2D, 2.5D, and simple 3D scenes."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any

def generate_html(scene: dict[str, Any], output: str | Path) -> dict[str, Any]:
    out=Path(output); out.parent.mkdir(parents=True, exist_ok=True)
    payload=json.dumps(scene, ensure_ascii=False)
    title=json.dumps(scene.get('title','Learning scene'), ensure_ascii=False)
    template='''<!doctype html><html><head><meta charset="utf-8"><title>__TITLE__</title><style>body{margin:0;background:#f5f7f3;font-family:system-ui;color:#2d2d2a}#bar{padding:10px 16px;color:#4c2c69;font-weight:700}canvas{display:block;width:100%;max-width:1280px;margin:auto;background:#f5f7f3}button{margin-right:6px}</style></head><body><div id="bar">__TITLE__ <button onclick="play()">Play</button><button onclick="pause()">Pause</button><button onclick="step()">Step</button><button onclick="reset()">Reset</button></div><canvas id="c" width="1280" height="720"></canvas><script>
const S=__PAYLOAD__;const c=document.getElementById('c'),x=c.getContext('2d');let t=0,running=false,last=0;const dur=S.duration||6;
function ease(q){return q*q*(3-2*q)} function project(p){const mode=S.mode||'2d',z=p[2]||0;if(mode==='2d')return [640+p[0]*140,360-p[1]*140];const par=(mode==='2.5d'?1+z*0.08:1/(1+Math.max(-.8,z*.12)));return [640+p[0]*140*par,360-p[1]*140*par]}
function draw(){x.clearRect(0,0,c.width,c.height);x.fillStyle='#4c2c69';x.font='22px system-ui';x.fillText('t = '+t.toFixed(1)+'s',24,34);for(const o of (S.objects||[])){const tr=o.transform||{position:[0,0,0]},p=tr.position||[0,0,0],q=project(p);x.save();x.translate(q[0],q[1]);x.strokeStyle=o.color||'#4c2c69';x.fillStyle=o.fill||'rgba(76,44,105,.14)';const k=o.kind;if(k==='point'){x.beginPath();x.arc(0,0,7,0,7);x.fill()}else if(k==='vector'||k==='arrow'){const d=o.direction||[1,0,0],e=project([p[0]+d[0],p[1]+d[1],p[2]+(d[2]||0)]);x.beginPath();x.moveTo(0,0);x.lineTo(e[0]-q[0],e[1]-q[1]);x.stroke()}else if(k==='circle'||k==='sphere'){x.beginPath();x.arc(0,0,Math.max(12,(o.radius||.6)*55),0,7);x.stroke()}else if(k==='rect'||k==='cube'||k==='plane'){let w=(o.width||1)*90,h=(o.height||1)*90;x.strokeRect(-w/2,-h/2,w,h)}else if(k==='text'){x.font='20px system-ui';x.fillStyle=o.color||'#2d2d2a';x.fillText(o.text||o.id,0,0)}if(o.label){x.font='18px system-ui';x.fillStyle='#2d2d2a';x.fillText(o.label,10,-12)}x.restore()}}
function loop(ms){if(!last)last=ms;if(running)t=Math.min(dur,t+(ms-last)/1000);last=ms;draw();if(running&&t<dur)requestAnimationFrame(loop);else running=false}function play(){running=true;last=0;requestAnimationFrame(loop)}function pause(){running=false}function step(){t=Math.min(dur,t+.25);draw()}function reset(){running=false;t=0;draw()}draw();</script></body></html>'''
    html=template.replace('__TITLE__',title).replace('__PAYLOAD__',payload)
    out.write_text(html, encoding='utf-8')
    return {'ok':True,'html':str(out),'mode':scene.get('mode','2d'),'controls':['play','pause','step','reset'],'errors':[],'warnings':[]}
