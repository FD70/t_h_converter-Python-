import keyboard

import mp.VideoCap
import t_h_converter.arg_set as thc

from t_h_converter import converter
# from t_h_converter_old import converter


def init():
    # keyboard.clear_all_hotkeys()
    # keyboard.add_hotkey('num_7', thc.set_line_count_up)
    # keyboard.add_hotkey('num_4', thc.set_line_count_down)
    keyboard.add_hotkey('num_9', thc.set_line_height_up)
    keyboard.add_hotkey('num_6', thc.set_line_height_down)
    keyboard.add_hotkey('num_0', mp.VideoCap.change_mode)


init()
# converter.t_h_converter()
converter.t_h_converter()
