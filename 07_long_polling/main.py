from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from typing import List
import asyncio

app = FastAPI()

# List to hold the clients
clients: List[JSONResponse] = []

@app.get("/events/subscribe")
async def subscribe(request: Request):
    response = JSONResponse(content={"data": "Subscribed"})
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    response.headers['Connection'] = 'keep-alive'

    clients.append(response)

    # Wait until the client disconnects
    try:
        await request.is_disconnected()
    finally:
        clients.remove(response)

    return response

@app.get("/events/publish")
async def publish():
    message = {"data": "This is a new message"}

    for client in clients:
        client.body = message

    clients.clear()

    return Response(status_code=204)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)


# Pros of Long Polling

# Reduced Latency:
# Long polling reduces the latency between the time new data becomes available and the time the client receives it, compared to short polling. The server responds immediately when new data is available.

# Efficient Use of Resources:
# Long polling is more efficient than short polling because it reduces the number of HTTP requests. The client waits for the server to respond with new data, rather than repeatedly polling at fixed intervals.

# Real-Time Updates:
# Long polling provides near real-time updates to the client, making it suitable for applications that require timely data delivery, such as chat applications or live notifications.

# Compatibility:
# Like short polling, long polling uses standard HTTP requests, making it compatible with existing infrastructure and easy to implement with most web frameworks.

# Firewall and Proxy Friendly:
# Since it uses standard HTTP requests, long polling is less likely to be blocked by firewalls or proxies compared to other techniques like WebSockets.


# Cons of Long Polling

# Server-Side Complexity:
# Long polling requires the server to maintain a connection for each client until new data is available. This can increase the complexity of server-side logic and resource management.

# Scalability:
# Maintaining long-lived connections for multiple clients can impact the server's scalability. The server must handle a large number of concurrent connections, which can increase memory and CPU usage.

# Timeouts and Reconnects:
# Long polling connections may time out, requiring the client to reconnect. This can introduce additional complexity in handling timeouts and ensuring reliable communication.

# Resource Consumption:
# While more efficient than short polling, long polling still consumes resources on both the client and server. The server must manage and maintain long-lived connections, which can be resource-intensive.

# Latency During Reconnects:
# If a long polling connection times out or is closed, there may be a delay while the client reconnects. This can introduce latency in receiving updates during the reconnect period.