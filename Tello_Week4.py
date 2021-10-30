#1

# from djitellopy import Tello

# tello = Tello()

# tello.connect()
# tello.takeoff()

# tello.move_left(50)
# tello.rotate_counter_clockwise(90)
# tello.move_back(50)

# tello.land()


#2

# import cv2
# from djitellopy import Tello

# tello = Tello()
# tello.connect()

# tello.streamon()
# frame_read = tello.get_frame_read()

# tello.takeoff()
# cv2.imwrite("picture.png", frame_read.frame)

# tello.land()


#3

# import time, cv2
# from threading import Thread
# from djitellopy import Tello

# tello = Tello()

# tello.connect()

# keepRecording = True
# tello.streamon()
# frame_read = tello.get_frame_read()

# def videoRecorder():
#     # create a VideoWrite object, recoring to ./video.avi
#     height, width, _ = frame_read.frame.shape
#     video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

#     while keepRecording:
#         video.write(frame_read.frame)
#         time.sleep(1 / 30)

#     video.release()

# # we need to run the recorder in a seperate thread, otherwise blocking options
# #  would prevent frames from getting added to the video
# recorder = Thread(target=videoRecorder)
# recorder.start()

# tello.takeoff()
# tello.move_up(100)
# tello.rotate_counter_clockwise(360)
# tello.land()

# keepRecording = False
# recorder.join()



#4

# simple example demonstrating how to control a Tello using your keyboard.
# For a more fully featured example see manual-control-pygame.py
#
# Use W, A, S, D for moving, E, Q for rotating and R, F for going up and down.
# When starting the script the Tello will takeoff, pressing ESC makes it land
#  and the script exit.

from threading import Thread
from djitellopy import Tello
import cv2, math, time

tello = Tello()
tello.connect()

keepRecording = True
tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()

def videoRecorder():
    # create a VideoWrite object, recoring to ./video.avi
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)

    video.release()

recorder = Thread(target=videoRecorder)
recorder.start()

while True:
    # In reality you want to display frames in a seperate thread. Otherwise
    #  they will freeze while the drone moves.
    # img = frame_read.frame
    # cv2.imshow("drone", img)

    key = cv2.waitKey(1) & 0xff
    if key == 27: # ESC
        break
    elif key == ord('w'):
        tello.move_forward(30)
    elif key == ord('s'):
        tello.move_back(30)
    elif key == ord('a'):
        tello.move_left(30)
    elif key == ord('d'):
        tello.move_right(30)
    elif key == ord('e'):
        tello.rotate_clockwise(30)
    elif key == ord('q'):
        tello.rotate_counter_clockwise(30)
    elif key == ord('r'):
        tello.move_up(30)
    elif key == ord('f'):
        tello.move_down(30)

tello.land()
keepRecording = Fals    
recorder.join() 
