from PIL import ImageGrab
import cv2
import numpy

import main_arg_set


# 1280x720
# 1360x768
# 1366x768
# 1600x900
# 1920x1080

# d_output_shape = (800, 450)
d_output_shape = main_arg_set.OUTPUT_FRAME
d_cap_box = (0, 170, 900, 660)


def get_desktop_frame():
    pillow_img = numpy.asarray(ImageGrab.grab(bbox=d_cap_box))
    img = cv2.resize(pillow_img, d_output_shape)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def change_mode():
    """Change stream mode Vebcam <==> Desktop"""
    modes = ('vebcam', 'desktop')
    VideoCap._cap_mode = 0 if VideoCap._cap_mode else 1
    print(f'mode changed to {modes[VideoCap._cap_mode]}')


class VideoCap:
    # 0 - vedcam 1 - desktop
    _cap_mode = 0

    _vebcam_stream = cv2.VideoCapture(0)

    def __init__(self, mode=0):
        VideoCap._cap_mode = mode

    def read(self):
        if self._cap_mode:
            return True, get_desktop_frame()
        else:
            success, frame = self._vebcam_stream.read()
            resized = cv2.resize(frame, d_output_shape)
            resized = cv2.flip(resized, 1)
            return success, resized
