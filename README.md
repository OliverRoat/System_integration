# System Integration

## Poetry guide

Hvis det er første gang du bruger projectet skal du køre

```sh
poetry init
```

Ellers kan du starte herfra

```sh
poetry install
```

```sh
poetry shell
```

To run uvicorn server script using poetry run

```sh
poetry run run-server
```

To run the C# server, use the following command:

On Windows:

```bat
.\run_csharp_server.bat
```

## WebSocket Example

### Running the WebSocket Server

To run the WebSocket server, use the following command:

```sh
dotnet run --project 09_WebSocket/WebSocketExample/WebSocketExample.csproj
```

### Testing the WebSocket Server

#### Using `index.html`

1. Open a browser and navigate to `http://localhost:5186/index.html`.
2. You will see a simple form with an input field and a "Send" button.
3. Enter a message in the input field and click "Send".
4. The message will be sent to the WebSocket server, which will echo it back, and the message will be displayed in the list below the form.

#### Using `wscat`

`wscat` is a command-line tool for interacting with WebSocket servers. It allows you to send and receive messages over a WebSocket connection from the terminal.

1. Connect to the WebSocket server using `wscat`:

   ```sh
   wscat -c ws://localhost:5186/ws
   ```

2. Once connected, you can type messages in the terminal and press Enter to send them to the WebSocket server.
3. The server will echo the messages back, and you will see the echoed messages in the terminal.
