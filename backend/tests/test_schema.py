from ariadne import graphql_sync
from app.graphql_schema.schema import schema


def test_docks_query():
    query = """
    query {
        docks {
            id
            name
            dockInfo {
                created_at
                updated_at
            }
            tanks {
                name
                columns {
                    name
                    data_type
                }
            }
        }
    }
    """
    success, result = graphql_sync(schema, {"query": query})
    assert success
    assert "docks" in result["data"]


def test_dock_query():
    query = """
    query {
        dock(id: "dock_1") {
            id
            name
            dockInfo {
                created_at
                updated_at
            }
            tanks {
                name
                columns {
                    name
                    data_type
                }
            }
        }
    }
    """
    success, result = graphql_sync(schema, {"query": query})
    assert success
    assert "dock" in result["data"]
    assert result["data"]["dock"]["id"] == "dock_1"
