from fastapi import FastAPI

from APIs import route

app = FastAPI()


# define endpoint

@app.get("/")
def home():
    return "Welcome Home"

app.include_router(route.router)