import cv2
import numpy


import mp.VideoCap
import t_h_converter_old.arg_set as my


def t_h_converter():
    # vin = cv2.VideoCapture(0)
    vin = mp.VideoCap.VideoCap()

    success, frame = vin.read()
    vin_height, vin_width, channels = numpy.shape(frame)
    print(f'{vin_width} {vin_height}')
    while success:
        recordframe = frame
        for x_index in range(0, vin_height-1, my.line_height):
            s, next_frame = vin.read()

            for i in range(my.line_count):
                rec = x_index + i * vin_height // my.line_count
                if rec > vin_height:
                    rec -= vin_height

                frame_line = next_frame[rec:rec + my.line_height, :]
                recordframe[rec:rec + my.line_height, :] = frame_line[:]

            # imshow
            cv2.imshow('converted', recordframe)
            cv2.imshow('normal', next_frame)
            cv2.waitKey(1)
            # print(x_index)
        cv2.waitKey(1)
