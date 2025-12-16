from fastapi import FastAPI

app = FastAPI(
  title="score",
  version="1.0.0",
  description="Rewards API"
)

@app.get("/")
async def api_ok():
  return { "message" : "API ok!"}



