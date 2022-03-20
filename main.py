from fastapi import FastAPI
from routes.years_route import year_api_router
from routes.students_route import students_api_router



app = FastAPI()

app.include_router(year_api_router)
app.include_router(students_api_router)