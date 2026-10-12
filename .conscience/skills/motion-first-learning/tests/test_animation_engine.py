import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / 'scripts'))
from core.math3d import Vec3, lerp_vec, rotation_y
from core.scene_graph import Node, SceneGraph
from core.timeline import evaluate_timeline
from core.animation_schema import validate_scene
from core.renderer_router import choose

class AnimationEngineTests(unittest.TestCase):
    def test_vec_and_hierarchy(self):
        self.assertEqual(Vec3(1,2,3)+Vec3(2,1,0), Vec3(3,3,3))
        g=SceneGraph(); g.add(Node('root','group',{'position':[1,0,0]})); g.add(Node('child','point',{'position':[0,2,0]},'root'))
        self.assertEqual(g.world_position('child'), Vec3(1,2,0))
    def test_interpolation_and_timeline(self):
        self.assertEqual(lerp_vec(Vec3(0,0,0),Vec3(2,2,2),.5), Vec3(1,1,1))
        s={'objects':[{'id':'v','kind':'vector'}],'timeline':[{'from':0,'to':1,'target':'v','property':'direction','value':[[0,0,0],[2,2,0]]}]}
        q=evaluate_timeline(s,.5); self.assertEqual(len(q['events']),1); self.assertEqual(q['objects']['v']['animated']['direction'],[1,1,0])
    def test_schema_and_routing(self):
        s={'schema_version':'animation-1.0','mode':'3d','objects':[{'id':'p','kind':'point','transform':{'position':[0,0,0]}}]}
        self.assertTrue(validate_scene(s)['ok']); self.assertEqual(choose(s,needs_interaction=True)['renderer'],'webgl_3d')
        self.assertFalse(validate_scene({'mode':'unknown'})['ok'])

if __name__=='__main__': unittest.main()
