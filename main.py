from fastapi import FastAPI, Request
from router import delegate_task

app = FastAPI()

@app.post("/assign-task/")
async def assign(request: Request):
    data = await request.json()
    agent = data.get("agent")
    prompt = data.get("prompt")
    return delegate_task(agent, prompt)