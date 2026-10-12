"""Renderer-neutral scene graph for 2D, 2.5D, and 3D educational scenes."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
from .math3d import Vec3, mat4_identity, mat4_mul, translation, scale, rotation_y, mat4_apply

@dataclass
class Node:
    node_id: str
    kind: str
    props: dict[str, Any] = field(default_factory=dict)
    parent: str | None = None
    children: list[str] = field(default_factory=list)

class SceneGraph:
    def __init__(self): self.nodes: dict[str, Node] = {}
    def add(self, node: Node) -> None:
        if node.node_id in self.nodes: raise ValueError(f'Duplicate node: {node.node_id}')
        if node.parent and node.parent not in self.nodes: raise ValueError(f'Unknown parent: {node.parent}')
        self.nodes[node.node_id] = node
        if node.parent: self.nodes[node.parent].children.append(node.node_id)
    def get(self, node_id: str) -> Node: return self.nodes[node_id]
    def world_position(self, node_id: str) -> Vec3:
        node=self.get(node_id); p=node.props.get('position',[0,0,0]); local=Vec3(*p)
        return local if not node.parent else self.world_position(node.parent)+local
    def snapshot(self) -> dict[str, Any]:
        return {'nodes': {k: {'kind':n.kind,'parent':n.parent,'children':list(n.children),'props':dict(n.props),'world_position':self.world_position(k).__dict__} for k,n in self.nodes.items()}}
    @classmethod
    def from_scene(cls, scene: dict[str, Any]) -> 'SceneGraph':
        graph=cls()
        for raw in scene.get('objects',[]): graph.add(Node(raw['id'], raw.get('kind','group'), raw.get('transform',{}) | raw.get('geometry',{}) | raw.get('style',{}), raw.get('parent')))
        return graph
