import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / 'scripts'))
from core.animation import Scene, Element
from core.composition import Composition
from plugins.utility_animation_components import reveal_object, move_object, pause_for_prediction, lookup
from plugins.utility_animation_registry import list_components, component_manifest

class UtilityComponentTests(unittest.TestCase):
    def setUp(self):
        self.scene=Scene(); self.scene.add(Element('v','vector',{'x':0,'y':0,'x1':0,'y1':0,'x2':1,'y2':1}))
    def test_recipe_and_accessibility(self):
        r=reveal_object(self.scene,'v'); self.assertEqual(r.recipe_id,'reveal_object'); self.assertTrue(r.accessible_text)
        self.assertGreaterEqual(len(list_components()),10); self.assertIn('rotate_about_axis',[x['name'] for x in list_components('3d')])
    def test_composition_and_conflicts(self):
        c=Composition(self.scene); c.add(move_object(self.scene,'v',0,1,[0,0],[1,1])); c.add(pause_for_prediction(self.scene,'Where is v?',1.2)); self.assertEqual(c.manifest()['event_count'],2)
        with self.assertRaises(ValueError): c.add(move_object(self.scene,'v',.5,1,[1,1],[2,2]))
    def test_manifest(self): self.assertGreater(component_manifest()['count'],10); self.assertTrue(lookup('rotate'))

if __name__=='__main__': unittest.main()
