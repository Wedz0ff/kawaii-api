from fastapi import APIRouter, HTTPException, Query
from src.app.services.words_service import get_random_de_word, get_random_jp_word

router = APIRouter()


@router.get("/random-jp-word")
def fetch_jp_word(
    level: int = Query(None, description="Filter by level (optional)"),
):
    try:
        random_word = get_random_jp_word(level=level)
        return random_word
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/random-de-word")
def fetch_de_word(
    level: str = Query(None, description="Filter by level (optional)"),
):
    try:
        random_word = get_random_de_word(level=level)
        return random_word
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
