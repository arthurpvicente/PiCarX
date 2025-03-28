# PiCarX

This project was developed as part of a college assignment to control a PiCar-X robot using Python. The project integrates socket programming for communication between a client and server, and OpenCV for camera functionalities.

## Project Structure

The project is organized into two main components:

### 1. **picar-server**
This folder contains the server-side code that runs on the PiCar-X. It listens for commands from the client and performs actions accordingly.

- **`move.py`**: Demonstrates basic movement and servo control of the PiCar-X.
- **`picar-server.py`**: Implements a UDP server to receive commands (e.g., forward, backward, left, right) and execute them.
- **`test-move.py`**: A simple script to test the movement functionality of the PiCar-X.

### 2. **picar-client**
This folder contains the client-side code that sends commands to the server and handles camera functionalities.

- **`picar-client.py`**: Implements a client to send movement commands to the server and includes OpenCV-based camera functionality to display video feed.

## Features

- **Remote Control**: The client sends commands (e.g., forward, backward, left, right) to the server via UDP.
- **Camera Integration**: OpenCV is used to display the video feed from the PiCar-X's camera.
- **Server Control**: The server-side code demonstrates servo motor control for both direction and camera angles.

## How to Run

### Server
1. Navigate to the `picar-server` directory.
2. Run the server script:
   ```bash
    python picar-server.py
    ```

### Client

1. Navigate to the `picar-client` directory.
2. Run the clien script:
    ```bash
    python picar-client.py
    ```
3. Use the arrow keys to control the PiCar-X:
 - **Up Arrow**: Move forward
 - **Down Arrow**: Move backward
 - **Left Arrow**: Turn left
 - **Right Arrow**: Turn right
 - **Q**: Quit the client

### Camera
The client also includes a camera feed feature using OpenCV. The video feed from the PiCar-X's camera is displayed on the client. Press q to exit the video feed.

### Requirements
- Python 3.x
- OpenCV
- Readchar library
- Raspberry Pi with PiCar-X
- PiCamera module

### Acknowledgments
This project was a great learning experience in:

- Socket programming for client-server communication.
- Using OpenCV for real-time video processing.
- Controlling hardware components like motors and servos with Python.