from dataclasses import dataclass
from typing import Tuple, List

class OpType:
    def __init__(self):
        print("")

class Operation:

    def __init__(self, op_type: OpType, steps: List[str]):
        print("DF")


@dataclass
class Insert(OpType):
    img_path: str
    fg_coords: Tuple[int, int]
    fg_dims: Tuple[int, int]

@dataclass
class Shell(OpType):
    img_path: str
    fg_coords: Tuple[int, int]
    fg_dims: Tuple[int, int]

@dataclass
class Audio(OpType):
    img_path: str
    fg_coords: Tuple[int, int]
    fg_dims: Tuple[int, int]
