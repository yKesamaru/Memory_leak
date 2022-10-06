"""An example that actually causes a memory leak."""
import os.path
import sys
dir: str = os.path.dirname(__file__)
parent_dir, _ = os.path.split(dir)
sys.path.append(parent_dir)


# Import Memory_leak class
from memory_leak import Memory_leak

# Make instance
# m = Memory_leak(limit = 5, key_type = 'lineno')
# m = Memory_leak(limit = 5, key_type = 'traceback', nframe = 3)
m = Memory_leak(limit = 5, key_type = 'traceback')

# Specify start point
m.memory_leak_analyze_start()


import cv2
import mediapipe as mp
import numpy as np
import numpy.typing as npt
import PySimpleGUI as sg


mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


input = dir + '/assets/ROMAN_HOLIDAY.mp4'
vcap = cv2.VideoCapture(input , cv2.CAP_FFMPEG)


# Make PySimpleGUI layout
#   cv2.imshow() is unstable depending on the environment, so use PySimpleGUI to draw the window.
sg.theme('LightGray')
layout = [
    [sg.Image(filename='', key='display', pad=(0,0))],
    [sg.Button('terminate', key='terminate', pad=(0,10), expand_x=True)]
]
window = sg.Window(
    'MEMORY_LEAK EXAMPLE',
    layout, alpha_channel = 1,
    margins = (10, 10),
    location = (0, 0),
    modal  =  True,
    titlebar_icon = dir + "/assets/icon.png",
    icon = dir + "/assets/icon.png"
)


def bad_code(
        f: object,
        frame: npt.NDArray[np.uint8],
        arg: str
    ) -> object:
    """Specify whether f is closed or not.

    Args:
        f (object): Handle
        frame (cv2.Mat): ndarray
        arg (str): 'close' or 'not_close'
    Return:
        result
    """
    results = f.process(frame)

    # Oh! I forgot `f.close()`...
    if arg == 'close':
        f.close()

    return results


def main(arg):
    """Receive arg, display window.

    Args:
        arg (str): 'close' or 'not_close'
    """    
    while vcap.isOpened():
        ret: bool
        frame: cv2.Mat
        ret, frame = vcap.read()

        if not ret:
            print(f"Can't load {input} any more.")
            break

        frame = cv2.resize(frame, dsize = None, fx = 0.5, fy = 0.5)

        event, _ = window.read(timeout = 1)

        if event == sg.WIN_CLOSED:
            print("The window was closed manually")
            break

        f = mp_face_detection.FaceDetection(
                model_selection=0,
                min_detection_confidence=0.5
            )

        results = bad_code(f, frame, arg)

        # Draw the face detection annotations on the image.
        frame.flags.writeable = True

        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(frame, detection)

        frame.flags.writeable = False

        imgbytes = cv2.imencode(".png", frame)[1].tobytes()
        window["display"].update(data = imgbytes)

        if event =='terminate':
            break

    window.close()


    # cv2.destroyAllWindows()
    vcap.release()


if __name__ == '__main__':

    # You're app
    main('not_close')

    # Specify end point
    m.memory_leak_analyze_stop()

