import rt_keypress

result_Keypress = ''

obj_keypress = rt_keypress.Get_Key()

print("Press keys or Ctrl+C to Exit")

while result_Keypress != 'Ctrl+ C':
    result_Keypress = obj_keypress.keypress()
    print(result_Keypress)

# python3 -m pip install /Users/fausto.branco/OneDrive/Work/Python/ebx_keypress/
