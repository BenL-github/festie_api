from pydantic import BaseModel

"""
STATE
"""

class State(BaseModel):
    state_name: str

"""
GENRE 
"""
class Genre(BaseModel):
    genre_name: str

"""
USER
"""
class User(BaseModel):
    f_name: str
    l_name: str
    email: str
    state_id: int

"""
FESTIVAL
"""
class Festival(BaseModel):
    festival_name: str
    price: int
    state_id: int

"""
ARTIST
"""
class Artist(BaseModel):
    artist_name: str
    genre_id: int

"""
FAVORITE ARTIST
"""
class UpdateFavoriteArtist(BaseModel):
    score: int

class CreateFavoriteArtist(UpdateFavoriteArtist):
    artist_id: int

"""
ARTIST FESTIVAL
"""
class CreateArtistFestival(BaseModel):
    festival_id: int

class DeleteArtistFestival(CreateArtistFestival):
    artist_id: int