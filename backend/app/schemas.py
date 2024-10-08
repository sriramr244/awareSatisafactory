from pydantic import BaseModel
from typing import List


class Column(BaseModel):
    name: str
    data_type: str


class Tank(BaseModel):
    name: str
    columns: List[Column]


class DockInfo(BaseModel):
    created_at: str
    updated_at: str


class Dock(BaseModel):
    id: str
    name: str
    dockInfo: DockInfo
    tanks: List[Tank]
