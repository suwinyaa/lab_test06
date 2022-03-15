from fastapi import FastAPI
from routes.ages_routes import year_api_router
from routes.todos_route import todo_api_router

app = FastAPI()

app.include_router(year_api_router)
app.include_router(todo_api_router)