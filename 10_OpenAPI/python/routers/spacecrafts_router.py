from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Spacecraft(BaseModel):
    id: int
    name: str

class SpacecraftRequestModel(BaseModel):
    name: str


spacecrafts: List[Spacecraft] = [
    Spacecraft(id=1, name="Apollo 13"),
    Spacecraft(id=2, name="Challenger"),
    Spacecraft(id=3, name="Enterprise"),
]

@router.get(
    path="/api/spacecrafts", 
    tags=["spacecrafts"],
    response_model=List[Spacecraft]
    )
def get_spacecrafts():
    return spacecrafts


@router.get(
    path="/api/spacecrafts/{spacecraft_id}", 
    tags=["spacecrafts"],
    response_model=Spacecraft
    )
def get_spacecraft_by_id(spacecraft_id: int):
    for spacecraft in spacecrafts:
        if spacecraft.id == spacecraft_id:
            return spacecraft
    raise HTTPException(status_code=404, detail="Spacecraft not found")

@router.post(
    path="/api/spacecrafts", 
    tags=["spacecraft"],
    response_model=Spacecraft
    )
def create_spacecraft(spacecraft: SpacecraftRequestModel):
    new_spacecraft = Spacecraft(id=5, name=spacecraft.name)
    spacecrafts.append(new_spacecraft)
    return new_spacecraft