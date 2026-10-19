import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / 'scripts'))
from core.animation_schema import validate_scene
from core.renderer_router import choose
from plugins.web_canvas_renderer import generate_html

OUT=Path('/home/ubuntu/motion-first-learning-simulation/unified-output'); OUT.mkdir(parents=True, exist_ok=True)

def scene(mode):
    return {'schema_version':'animation-1.0','mode':mode,'title':f'{mode} spatial learning demo','duration':4,'camera':{'projection':'orthographic'},'objects':[{'id':'origin','kind':'point','transform':{'position':[0,0,0]},'label':'origin','color':'#4c2c69'},{'id':'vector','kind':'vector','transform':{'position':[0,0,0]},'direction':[2,1,0], 'label':'moving vector','color':'#f2a900'}], 'timeline':[{'at':0,'event':'show','target':'origin'}], 'learning':{'purpose':'show a spatial transition','prompt':'Predict the next endpoint'}}

for mode in ('2d','2.5d','3d'):
    s=scene(mode); check=validate_scene(s); assert check['ok'], check
    decision=choose(s, needs_interaction=True, needs_continuous_motion=True)
    result=generate_html(s, OUT/f'{mode}.html')
    print(mode, decision, result)
