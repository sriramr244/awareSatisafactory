from pydantic import BaseModel
from typing import List
from datetime import datetime


class Column(BaseModel):
    name: str
    data_type: str


class Tank(BaseModel):
    name: str
    columns: List[Column]


class DockInfo(BaseModel):
    created_at: datetime
    updated_at: datetime


class Dock(BaseModel):
    id: str
    name: str
    metadata: DockInfo
    tanks: List[Tank]
