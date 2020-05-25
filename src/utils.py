from typing import Callable


def input_loop(text: str, validation_function: Callable, error_msg: str = "", input_hint: str = ""):
    input_ok = False
    input_text = None

    while not input_ok:
        print(text)
        input_text = input(input_hint)
        input_ok = validation_function(input_text)
        if not input_ok:
            print(error_msg)

    return input_text
