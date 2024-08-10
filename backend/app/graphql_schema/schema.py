from ariadne import QueryType, make_executable_schema, gql
from pathlib import Path
import json

type_defs = gql(
    """
    type Column {
        name: String!
        data_type: String!
    }

    type Tank {
        name: String!
        columns: [Column!]!
    }

    type DockInfo {
        created_at: String!
        updated_at: String!
    }

    type Dock {
        id: String!
        name: String!
        dockInfo: DockInfo!
        tanks: [Tank!]!
    }

    type Query {
        docks: [Dock!]!
        dock(id: String!): Dock
    }
"""
)

query = QueryType()


def load_docks_data():
    """Load docks data from the JSON file."""
    file_path = Path(__file__).parent.parent / "data" / "docks.json"
    with open(file_path, "r") as file:
        return json.load(file)


@query.field("docks")
def resolve_docks(*_):
    """Resolver for fetching all docks."""
    return load_docks_data()


@query.field("dock")
def resolve_dock(*_, id):
    """Resolver for fetching a specific dock by ID."""
    docks_data = load_docks_data()
    for dock in docks_data:
        if dock["id"] == id:
            return dock
    return None


schema = make_executable_schema(type_defs, query)
