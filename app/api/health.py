from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/")
def health_check():
    """
    Health endpoint.
    """
    return {
        "status": "UP",
        "application": "Leave Management Portal"
    }
