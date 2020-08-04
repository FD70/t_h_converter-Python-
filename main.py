import cv2
import numpy


def t_h_converter():
    vin = cv2.VideoCapture(0)

    success, frame = vin.read()
    vin_height, vin_width, channels = numpy.shape(frame)
    print(f'{vin_width} {vin_height}')
    while success:
        recordframe = frame
        for x_index in range(0, vin_height-1, 10):
            s, next_frame = vin.read()

            next_frame = cv2.flip(next_frame, 1)
            rec = x_index + vin_height//2
            if rec > vin_height:
                rec -= vin_height
            next_chap1 = next_frame[x_index:x_index + 10, :]
            next_chap2 = next_frame[rec:rec + 10, :]

            recordframe[x_index:x_index+10, :] = next_chap1[:]
            recordframe[rec:rec + 10, :] = next_chap2[:]

            # imshow
            cv2.imshow('converted', recordframe)
            cv2.imshow('normal', next_frame)
            cv2.waitKey(1)
            print(x_index)
        cv2.waitKey(1)


t_h_converter()
