from fastapi import APIRouter
from schemas import User, CreateFavoriteArtist, UpdateFavoriteArtist
import main as api

router = APIRouter()

@router.get("/users", tags = ["users"])
def get_user():
    users = api.db.get_table("app_user")
    return users

@router.post("/users", tags = ["users"], status_code = 201)
def create_user(user: User):
    api.db.create_user(user.f_name, user.l_name, user.email, user.state_id)

@router.put("/users/{user_id}", tags = ["users"])
def update_user(user_id: int, user: User):
    api.db.update_user(user_id, user.f_name, user.l_name, user.email, user.state_id)

@router.delete("/users/{user_id}", tags = ["users"])
def delete_user(user_id: int):
    api.db.delete_user(user_id)

@router.get("/users/{user_id}/favorite_artists", tags = ["users"])
def get_user_favorite_artist(user_id: int):
    favorite_artists = api.db.get_user_favorite_artist(user_id)
    return api.add_details(favorite_artists, ("artist_id", "artist_name", "rating"))

@router.post("/users/{user_id}/favorite_artists", tags = ["users"])
def create_favorite_artist(user_id: int, favorite_artist: CreateFavoriteArtist):
    api.db.create_favorite_artist(user_id, favorite_artist.artist_id, favorite_artist.score)

@router.put("/users/{user_id}/favorite_artists/{artist_id}", tags = ["users"])
def update_favorite_artist(user_id: int, artist_id: int, favorite_artist: UpdateFavoriteArtist):
    api.db.update_favorite_artist(user_id, artist_id, favorite_artist.score)

@router.delete("/users/{user_id}/favorite_artists/{artist_id}", tags = ["users"])
def delete_favorite_artist(user_id: int, artist_id: int):
    api.db.delete_favorite_artist(user_id, artist_id)

@router.get("/users/{user_id}/festival_match", tags = ["users"])
def get_user_festival_match(user_id: int):
    festivals = api.db.find_potential_festivals(user_id)
    return api.add_details(festivals, ("festival_name", "favorites_attending"))

