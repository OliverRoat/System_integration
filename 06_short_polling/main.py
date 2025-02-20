from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import random

app = FastAPI()

# Serve static files from the "public" directory
app.mount("/public", StaticFiles(directory="public"), name="public")

random_numbers = [1, 25, 574]

@app.get("/randomnumbers")
def get_random_numbers():
    return JSONResponse(content={"data": random_numbers})

@app.get("/simulatenewnumbers")
def simulate_new_numbers():
    new_number = random.randint(0, 100)
    random_numbers.append(new_number)
    return JSONResponse(content={"data": new_number})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)


# Pros of Short Polling
# Simplicity:
# Short polling is easy to implement and understand. It uses standard HTTP requests, which are well-supported by most web frameworks and libraries.

# Compatibility:
# Works with any server that supports HTTP, making it highly compatible with existing infrastructure.

# No Server-Side State:
# The server does not need to maintain a persistent connection or state for each client, which can simplify server-side logic.

# Firewall and Proxy Friendly:
# Since it uses standard HTTP requests, it is less likely to be blocked by firewalls or proxies compared to other techniques like WebSockets.


# Cons of Short Polling

# Inefficiency:
# Short polling can be inefficient because it involves frequent HTTP requests, even when there is no new data. This can lead to increased server load and higher bandwidth usage.

# Latency:
# There is an inherent delay between the time new data becomes available and the time the client receives it, depending on the polling interval. This can result in higher latency compared to other techniques like long polling or WebSockets.

# Scalability:
# As the number of clients increases, the number of HTTP requests to the server also increases, which can impact the server's scalability and performance.

# Battery and Resource Consumption:
# Frequent polling can consume more battery and resources on client devices, especially mobile devices, due to the constant network activity.

# Server Load:
# The server must handle a large number of incoming requests, which can lead to increased CPU and memory usage, potentially requiring more powerful hardware or additional servers to handle the load.