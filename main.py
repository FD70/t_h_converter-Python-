import cv2
import numpy
import arg_set


def t_h_converter():
    vin = cv2.VideoCapture(0)

    success, frame = vin.read()
    vin_height, vin_width, channels = numpy.shape(frame)
    print(f'{vin_width} {vin_height}')
    while success:
        recordframe = frame
        for x_index in range(0, vin_height-1, arg_set.line_height):
            s, next_frame = vin.read()
            next_frame = cv2.flip(next_frame, 1)

            for i in range(arg_set.line_count):
                rec = x_index + i * vin_height // arg_set.line_count
                if rec > vin_height:
                    rec -= vin_height

                frame_line = next_frame[rec:rec + arg_set.line_height, :]
                recordframe[rec:rec + arg_set.line_height, :] = frame_line[:]

            # imshow
            cv2.imshow('converted', recordframe)
            cv2.imshow('normal', next_frame)
            cv2.waitKey(1)
            # print(x_index)
        cv2.waitKey(1)


arg_set.init()
t_h_converter()
