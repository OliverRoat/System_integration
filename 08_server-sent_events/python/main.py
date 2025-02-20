from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
import time
import asyncio

app = FastAPI()

# Serve static files from the "public" directory
app.mount("/public", StaticFiles(directory="public"), name="public")

@app.get("/synchronizetime")
async def synchronize_time(request: Request):
    async def event_generator():
        while True:
            if await request.is_disconnected():
                break
            time_str = time.strftime("%Y-%m-%d %H:%M:%S")
            yield f"data: {time_str}\n\n"
            await asyncio.sleep(1)

    return StreamingResponse(event_generator(), media_type="text/event-stream")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)