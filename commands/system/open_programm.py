import keyboard
import time
import re

def find_next_word_after_keyword(input_string, keyword):
    match = re.search(fr'{re.escape(keyword)}\s+(\w+)', input_string, re.IGNORECASE)

    if match:
        next_word = match.group(1)
        return next_word
    else:
        return None
def start_process(text):

    result = find_next_word_after_keyword(text, "открой")

    keyboard.press_and_release('win+s')
    time.sleep(1)
    keyboard.write(result)
    time.sleep(2)
    keyboard.press('enter')