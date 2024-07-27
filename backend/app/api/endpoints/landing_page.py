from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/landing-page-info",
    summary="Get Landing Page Info",
    description="Retrieve information about the landing page.",
)
def get_landing_page_info():
    return {"message": "This is the landing page info endpoint"}
