from fastapi import APIRouter
from typing import List
from app.schemas import Dock
import json

router = APIRouter()


@router.get(
    "/docks",
    response_model=List[Dock],
    summary="Get All Docks",
    description="Retrieve a list of all docks.",
)
def get_docks():
    # Load docks data from JSON file
    return load_docks_data()


@router.get(
    "/dock/{id}",
    response_model=Dock,
    summary="Get Dock by ID",
    description="Retrieve a specific dock by its ID.",
)
def get_dock(id: str):
    # Load a specific dock by ID from JSON file
    return load_dock_data(id)


def load_docks_data():
    """Load docks data from the JSON file."""
    file_path = Path(__file__).parent.parent / "data" / "docks.json"
    with open(file_path, "r") as file:
        return json.load(file)


def load_dock_data(dock_id: str):
    """Load a specific dock by ID from the JSON file."""
    docks_data = load_docks_data()
    for dock in docks_data:
        if dock["id"] == dock_id:
            return dock
    return None
