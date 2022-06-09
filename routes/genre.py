from fastapi import APIRouter
from schemas import Genre
import main as api

router = APIRouter()

@router.get("/genres", tags = ["genres"])
def get_genre():
    genres = api.db.get_table("genre")
    return genres

@router.post("/genres", tags = ["genres"], status_code = 201)
def post_genre(genre: Genre):
    api.db.insert_genre(genre.genre_name)
    return {"Entry":genre.genre_name}

@router.put("/genres/{genre_id}", tags = ["genres"], status_code = 204)
def update_genre(genre_id: int, genre: Genre):
    api.db.update_genre(genre_id, genre.genre_name)

@router.delete("/genres/{genre_id}", tags = ["genres"], status_code = 200)
def delete_genre(genre_id: int):
    api.db.delete_genre(genre_id)
