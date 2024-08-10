from fastapi import APIRouter
from ariadne.asgi import GraphQL
from app.graphql_schema.schema import schema

router = APIRouter()

graphql_app = GraphQL(schema, debug=True)

router.add_route("/graphql", graphql_app)
router.add_websocket_route("/graphql", graphql_app)
