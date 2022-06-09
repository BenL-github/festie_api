from fastapi import APIRouter
from schemas import Artist, CreateArtistFestival
import main as api

router = APIRouter()

@router.get("/artists", tags = ["artists"])
def get_artist():
    artists = api.db.get_table("artist")
    return artists

@router.post("/artists", tags = ["artists"])
def create_artist(artist: Artist):
    api.db.create_artist(artist.artist_name, artist.genre_id)

@router.put("/artists/{artist_id}", tags = ["artists"])
def update_artist(artist_id: int, artist: Artist):
    api.db.update_artist(artist_id, artist.artist_name, artist.genre_id)

@router.delete("/artists/{artist_id}", tags = ["artists"])
def delete_artist(artist_id: int):
    api.db.delete_artist(artist_id)

@router.get("/artists/{artist_id}/festivals", tags = ["artists"])
def get_artist_festival(artist_id: int):
    festivals = api.db.get_artist_festival(artist_id)
    return api.add_details(festivals, ("festival_id", "festival_name", "price", "state"))

@router.post("/artists/{artist_id}/festivals", tags = ["artists"])
def create_artist_festival(artist_id: int, artist_festival: CreateArtistFestival):
    api.db.create_artist_festival(artist_id, artist_festival.festival_id)

@router.delete("/artists/{artist_id}/festivals/{festival_id}", tags = ["artists"])
def delete_artist_festival(artist_id: int, festival_id: int):
    api.db.delete_artist_festival(artist_id, festival_id)
