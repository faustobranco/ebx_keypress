# Key Press

Python package for capture and return keypress.

### Prerequisites

Developed and tested in Linux and Python 3


### Installing

    pip3 install keypress

or from source:

    python3 -m pip install [your_path]/keypress/


## Functions

### keypress

keypress():
Description: Capture pressed keys and combined keys and return as string

Return: String with pressed key

## Examples of use

```
import keypress

result_Keypress = ''

obj_keypress = keypress.Get_Key()

print "Press keys or Ctrl+C to Exit"

while result_Keypress <> 'Ctrl+ C':
    result_Keypress = obj_keypress.keypress()
    print(result_Keypress)

    
```

## Versioning
```
=======================================================================================
== Log Changes: 
== Date:            2021-06-12
== Author:          Fausto Branco
== Version:         1.0.0
== Description:     Initial Version
=======================================================================================

```




