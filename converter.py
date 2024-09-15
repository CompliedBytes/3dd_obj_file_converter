from dataclasses import dataclass

@dataclass
class shape:
    number: int
    shape_desc: str
    SiFlag:int
    RoundFlag: float
    Height: float
    Width: float
    Area: float
    Ix: float
    Iy: float
    Iz: float
    Sy: float
    Sz: float
    SepDistance: float

@dataclass
class material:
    number: int
    material_desc: str
    SiFlag:int
    RoundFlag: float
    Height: float
    Width: float
    Area: float

@dataclass
class joint:
    number: int
    x: float
    y: float
    z: float
    trans_x: int
    trans_y: int
    trans_z: int
    rot_x: int
    rot_y: int
    rot_z: int
    joint_type: str
    subtype: str

@dataclass
class member:
    number: int
    start_joint: int
    End_joint: int
    EffectiveLengthyy: float
    EffectiveLengthzz: float
    MembLengthzzflag: int
    MembLengthyyflag: int
    Offsety: float
    Offsetz: float
    Shape_No: int
    Material_No: int
    Sub_Type: int
    RollAngle: float
    UseTorsionFlag: int
    FixMy1: int
    FixMz1: int
    FixMy2: int
    FixMz2: int
    MembColorRed: float
    MembColorGreen: float
    MemColorBlue: float



file = open("k_truss.3dd", "r")

for line in file:
    print(line)