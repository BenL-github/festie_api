from pydantic import BaseModel

class State(BaseModel):
    state_name: str

class Genre(BaseModel):
    genre_name: str

class User(BaseModel):
    f_name: str
    l_name: str
    email: str
    state_id: int

class Festival(BaseModel):
    festival_name: str
    price: int
    state_id: int

class Artist(BaseModel):
    artist_name: str
    genre_id: int

class UpdateFavoriteArtist(BaseModel):
    score: int

class CreateFavoriteArtist(UpdateFavoriteArtist):
    artist_id: int

class CreateArtistFestival(BaseModel):
    festival_id: int

class DeleteArtistFestival(CreateArtistFestival):
    artist_id: int