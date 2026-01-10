from fastapi import FastAPI
from score.routes.user import router as user_router

app = FastAPI(
  title="score",
  version="1.0.0",
  description="Rewards API"
)

@app.get("/")
async def api_ok():
  return { "message" : "API ok!"}

app.include_router(user_router, prefix="/user", tags=["user"])

