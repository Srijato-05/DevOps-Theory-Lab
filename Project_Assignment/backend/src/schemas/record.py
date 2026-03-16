from pydantic import BaseModel
from typing import Optional

class RecordBase(BaseModel):
    name: str
    description: str

class RecordCreate(RecordBase):
    pass

class RecordResponse(RecordBase):
    id: int

    class Config:
        from_attributes = True
