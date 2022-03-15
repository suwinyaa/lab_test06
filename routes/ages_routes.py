from fastapi import APIRouter
import datetime
year_api_router = APIRouter()
y = datetime.datetime.now()

@year_api_router.get("/service/getage")
async def get_test(year: int=0):
    if year <= 0:
        return {"msg": "years not less than 0"}
    elif year > (y.year+543) :
        return {"msg": "unable to calculate"}
    else:
        age = (y.year+543) - year
        return {"age": age}