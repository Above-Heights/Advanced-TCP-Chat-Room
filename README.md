# Advanced-TCP-Chat-Room
Real-time multi-client TCP chatroom built with Python socket programming, Flask, and Socket.IO. Features a modern browser-based UI, multiple client support, real-time messaging, sender/receiver chat alignment, and localhost deployment for learning, demonstrations, and networking projects.

## Features

- Multi-client TCP chatroom
- Real-time messaging
- Browser-based UI
- Multiple browser clients support
- Automatic browser launch
- Alias-based chatting
- Modern dark-themed interface
- Sender and receiver message alignment
- Lightweight architecture
- Localhost deployment support

---

## Technologies Used

## Backend

- Python
- Socket Programming
- Threading
- Flask
- Flask-SocketIO

### Frontend

- HTML
- CSS
- JavaScript
- Socket.IO

---

## Project Structure

```text
Advance-chat-room/
│
├── server.py
├── web_bridge.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── app.js
```

---

## Installation

### Step 1: Clone or Download the Project

Place all files inside one project folder.

---

### Step 2: Create Virtual Environment (Optional)

```bash
python -m venv .venv
```

Activate virtual environment:

#### Windows
```bash
.venv\Scripts\activate
```

---

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## requirements.txt

```txt
flask
flask-socketio
```

---

## Running the Project

### Step 1: Start TCP Server

Open terminal inside project folder:

```bash
python server.py
```

You should see:

```text
Server running on localhost:8000
```

---

### Step 2: Start Web Interface

Open another terminal:

```bash
python web_bridge.py
```

Browser will open automatically.

---

## Access Web UI

Open:

```text
http://127.0.0.1:5000
```

---

## Testing Multiple Clients

Open multiple browser tabs/windows.

Enter different aliases:

- tom
- jerry
- alex

Start chatting in real-time.

---

## How It Works

### Architecture

```text
Browser UI
   ↓
Flask + Socket.IO
   ↓
TCP Bridge
   ↓
Python TCP Server
```

The browser communicates with Flask-SocketIO, which acts as a bridge between the web interface and the TCP socket server.

---

## Message Alignment

- Sent messages appear on the right side
- Received messages appear on the left side

---

## Current Capabilities

- Real-time communication
- Multi-user support
- Browser-based messaging
- Local network testing
- Localhost deployment

---

## Limitations

This project is designed for:

- Learning
- Demonstration
- College projects
- Local testing
- Portfolio showcase

It is not optimized for large-scale production deployment.

---

## Future Improvements

Possible future upgrades:

- User authentication
- Private messaging
- Chat history database
- Online users list
- File sharing
- Emojis
- Voice chat
- Video chat
- Docker deployment
- Cloud deployment

---

## Author

ANIKET TOMAR

LinkedIn:  
https://www.linkedin.com/in/aniket-tomar-a17954250/

---

## License

This project is for educational and demonstration purposes.
