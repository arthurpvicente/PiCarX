import socket
import readchar
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

HOST = "nwcpicar2"
SERVER_PORT = 12000

def send_to_server(command: str):
    """Send command to picar"""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(1)
        packet = f"{command}"

        # Send message
        s.sendto(packet.encode(), (HOST, SERVER_PORT))

def run_client():
    # Listen for input
    while True:
        key = readchar.readkey()

        if key == readchar.key.UP:
            picar_command = "forward"
        if key == readchar.key.DOWN:
            picar_command = "backward"
        if key == readchar.key.LEFT:
            picar_command = "left"
        if key == readchar.key.RIGHT:
            picar_command = "right"
        if key == "q":
            picar_command = "quit"
            send_to_server(picar_command)
            break
        
        print(picar_command)
        send_to_server(picar_command)

def camera_stuffs():
    # Initialize the camera.
    with PiCamera() as camera:
        # Set camera resolution.
        camera.resolution = (640, 480)
        camera.framerate = 24
        rawCapture = PiRGBArray(camera, size=(640, 480))

        #Allow the camera to warm up
        time.sleep(0.1)

        # Set up a camera object for the program to use.
        cap = cv2.VideoCapture()
        cap.open(camera.capture_continuous(rawCapture, format="bgr", use_video_port=True))

        while True:
            # Capture a frame from the camera.
            # @success is a boolean generated when capturing a frame declaring whether the capture was successful or not.
            # @capture is the frame captured by the camera.
            success, capture = cap.read()

            # Display the frame captured to the client.
            cv2.imshow("PiCam", capture) # Possibly replace this with code to send the capture to the server?

            # Check if 'q' has been pressed. If it has, exit the loop.
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

            #Clear the stream in preparation for the next frame.
            rawCapture.truncate(0)

        # Release the camera and close the video feed.
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    run_client()
    
