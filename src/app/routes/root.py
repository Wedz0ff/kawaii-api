from fastapi import APIRouter

router = APIRouter()


@router.get("/", include_in_schema=False)
def root():
    return "Service is running, yay!"
