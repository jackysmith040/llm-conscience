"""Small dependency-free 3D math kernel for educational scenes."""
from __future__ import annotations
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class Vec3:
    x: float; y: float; z: float
    def __add__(self, o): return Vec3(self.x+o.x, self.y+o.y, self.z+o.z)
    def __sub__(self, o): return Vec3(self.x-o.x, self.y-o.y, self.z-o.z)
    def __mul__(self, s: float): return Vec3(self.x*s, self.y*s, self.z*s)
    def dot(self, o): return self.x*o.x+self.y*o.y+self.z*o.z
    def cross(self, o): return Vec3(self.y*o.z-self.z*o.y, self.z*o.x-self.x*o.z, self.x*o.y-self.y*o.x)
    def length(self): return math.sqrt(self.dot(self))
    def normalized(self):
        n=self.length(); return self if n==0 else self*(1/n)

def lerp_vec(a: Vec3, b: Vec3, t: float) -> Vec3: return a*(1-t)+b*t

def mat4_identity(): return ((1.,0.,0.,0.),(0.,1.,0.,0.),(0.,0.,1.,0.),(0.,0.,0.,1.))

def mat4_mul(a,b): return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(4)) for j in range(4)) for i in range(4))

def mat4_apply(m, v: Vec3, w=1.0):
    q=[sum(m[i][k]*([v.x,v.y,v.z,w][k]) for k in range(4)) for i in range(4)]
    return Vec3(q[0]/q[3],q[1]/q[3],q[2]/q[3]) if q[3] else Vec3(q[0],q[1],q[2])

def translation(v: Vec3):
    m=[list(r) for r in mat4_identity()]; m[0][3]=v.x; m[1][3]=v.y; m[2][3]=v.z; return tuple(map(tuple,m))

def scale(v: Vec3):
    return ((v.x,0.,0.,0.),(0.,v.y,0.,0.),(0.,0.,v.z,0.),(0.,0.,0.,1.))

def rotation_y(angle: float):
    c,s=math.cos(angle),math.sin(angle); return ((c,0.,s,0.),(0.,1.,0.,0.),(-s,0.,c,0.),(0.,0.,0.,1.))

def perspective(fov_y: float, aspect: float, near: float, far: float):
    f=1/math.tan(fov_y/2); q=far/(near-far)
    return ((f/aspect,0,0,0),(0,f,0,0),(0,0,q,near*q),(0,0,-1,0))

def orthographic(left,right,bottom,top,near,far):
    return ((2/(right-left),0,0,-(right+left)/(right-left)),(0,2/(top-bottom),0,-(top+bottom)/(top-bottom)),(0,0,-2/(far-near),-(far+near)/(far-near)),(0,0,0,1))

def project(v: Vec3, view_projection, width: int, height: int):
    q=mat4_apply(view_projection,v); return ((q.x+1)*0.5*width, (1-q.y)*0.5*height, q.z)
