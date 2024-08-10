from fastapi import FastAPI
from app.api.endpoints import landing_page, docks, graphql_api

app = FastAPI(
    title="awareSatisfactory API",
    description="API for the awareSatisfactory ERP project for the Satisfactory game.",
    version="1.0.0",
    contact={
        "name": "Your Name",
        "url": "http://example.com/contact",
        "email": "your-email@example.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

app.include_router(landing_page.router, prefix="/api", tags=["Landing Page"])
app.include_router(docks.router, prefix="/api", tags=["Docks"])
app.include_router(graphql_api.router, prefix="/api", tags=["GraphQL"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
