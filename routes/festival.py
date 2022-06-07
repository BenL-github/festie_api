from fastapi import APIRouter
from schemas import Festival
import festie_api as api

router = APIRouter()

@router.get("/festivals", tags = {"festivals"})
def get_festival():
    festivals = api.db.get_table("festival")
    return festivals

@router.post("/festivals", tags = {"festivals"})
def create_festival(festival: Festival):
    api.db.create_festival(festival.festival_name, festival.price, festival.state_id)

@router.put("/festivals/{festival_id}", tags = {"festivals"})
def update_festival(festival_id, festival: Festival):
    api.db.update_festival(festival_id, festival.festival_name, festival.price, festival.state_id)

@router.delete("/festivals/{festival_id}", tags = {"festivals"})
def delete_festival(festival_id):
    api.db.delete_festival(festival_id)
