import cv2
import numpy
import collections

import mp.VideoCap
import arg_set


def t_h_converter():
    # vin = cv2.VideoCapture(0)
    vin = mp.VideoCap.VideoCap()

    success, frame = vin.read()
    vin_height, vin_width, channels = numpy.shape(frame)
    print(f'{vin_width} {vin_height}')
    while success:
        recordframe = frame
        for x_index in range(0, vin_height-1, arg_set.line_height):
            s, next_frame = vin.read()
            # next_frame = cv2.flip(next_frame, 1)

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


# =============================================================================
frame_queue = collections.deque()


def queue_reader(video_input):
    frame_queue.clear()
    success, frame = video_input.read()
    vin_height, vin_width, channels = numpy.shape(frame)
    print(f'{vin_width} {vin_height}')
    for i in range(vin_height//arg_set.line_height):
        frame_queue.append(frame)
        success, frame = video_input.read()
        print(f'take {i} frames')


def get_next_frame(frame):
    n_frame = frame_queue.popleft()
    frame_queue.append(frame)
    return n_frame


def t_h_converter_type2():
    # vin = cv2.VideoCapture(0)
    # vin = desktop
    vin = mp.VideoCap.VideoCap()
    queue_reader(vin)
    success, frame = vin.read()
    while success:
        success, frame = vin.read()
        normal_frame = frame
        recordframe = get_next_frame(frame)
        for x_index in range(len(frame_queue)):
            rec = x_index * arg_set.line_height
            recordframe[rec:rec + arg_set.line_height, :] = frame_queue[x_index][rec:rec + arg_set.line_height, :]

        # recordframe = cv2.flip(recordframe, 1)
        # normal_frame = cv2.flip(normal_frame, 1)
        cv2.imshow('converted', recordframe)
        cv2.imshow('normal', normal_frame)
        cv2.waitKey(1)
