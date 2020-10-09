import cv2
import numpy
import collections

import mp.VideoCap
import t_h_converter.arg_set as my


frame_queue = collections.deque()


def queue_reader(video_input):
    frame_queue.clear()
    success, frame = video_input.read()
    vin_height, vin_width, channels = numpy.shape(frame)
    print(f'{vin_width} {vin_height}')
    chap_frame_count = vin_height//my.line_height
    for i in range(chap_frame_count):
        frame_queue.append(frame)
        success, frame = video_input.read()
        # print(f'take {i} frames')
        print(f'{(i+1)/chap_frame_count * 100:.1f} %')


def queue_resize(video_input):
    # проверить разницу в количестве кусков кадра
    # если количество кусков больше чем нужно - уменьшить,
    # или увеличить если меньше чем нужно
    pass


def get_next_frame(frame):
    n_frame = frame_queue.popleft()
    frame_queue.append(frame)
    return n_frame


def t_h_converter():
    # vin = cv2.VideoCapture(0)
    vin = mp.VideoCap.VideoCap()
    queue_reader(vin)
    success, frame = vin.read()
    while success:
        success, frame = vin.read()
        normal_frame = frame
        recordframe = get_next_frame(frame)
        for x_index in range(len(frame_queue)):
            rec = x_index * my.line_height
            recordframe[rec:rec + my.line_height, :] = frame_queue[x_index][rec:rec + my.line_height, :]

        cv2.imshow('converted', recordframe)
        cv2.imshow('normal', normal_frame)
        cv2.waitKey(1)
