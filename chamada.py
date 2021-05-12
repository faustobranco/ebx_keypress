
import pydevd_pycharm
pydevd_pycharm.settrace('localhost', port=12345, stdoutToServer=True, stderrToServer=True)

import src.keypress as keypress

result_Keypress = ''

obj_keypress = keypress.Get_Key()

print("Press keys or Ctrl+C to Exit")

while result_Keypress != 'Ctrl+ C':
    result_Keypress = obj_keypress.keypress()
    print(result_Keypress)

# python3 -m pip install /Users/fausto.branco/OneDrive/Work/Python/keypress/
