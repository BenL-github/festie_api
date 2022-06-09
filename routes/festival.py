from fastapi import APIRouter
from schemas import Festival
import database 
router = APIRouter()

@router.get("/festivals", tags = {"festivals"})
def get_festival():
    festivals = database.db.get_table("festival")
    return festivals

@router.post("/festivals", tags = {"festivals"})
def create_festival(festival: Festival):
    database.db.create_festival(festival.festival_name, festival.price, festival.state_id)

@router.put("/festivals/{festival_id}", tags = {"festivals"})
def update_festival(festival_id, festival: Festival):
    database.db.update_festival(festival_id, festival.festival_name, festival.price, festival.state_id)

@router.delete("/festivals/{festival_id}", tags = {"festivals"})
def delete_festival(festival_id):
    database.db.delete_festival(festival_id)
