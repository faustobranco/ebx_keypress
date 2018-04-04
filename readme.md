# KeyPress

Python class for capture and return keypress.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Developed and tested in Linux Ubuntu and Python 2.7


### Installing

A step by step series of examples that tell you have to get a development env running

1. Create a folder called "keypress" inside the folder of your project.
2. Copy the keypress.py and `__init__.py` files to the keypress folder
3. Do class import for your project normally.

* If the import is successful, a file called checklist.pyc must be created, this file (compiled python file) must be maintained.

## Functions

### keypress

keypress():
Description: Capture pressed keys and combined keys and return as string

Return: String with pressed key


## Deployment

Additional notes about how to deploy this on a live system:
Para deploy em ambiente de live:
1) Create a folder called "keypress" inside the folder of your project.
2) Copy the keypress.pyc and `__init__.pyc` files to the keypress folder

Note: Unless you really have experience, do not install directly on /usr/local/lib/python2.7/dist-packages

For next versions will be available installation by setup or pip.

## Examples of use

```
import keypress

result_Keypress = ''

obj_keypress = keypress.Get_Key()

print "Press keys or Ctrl+C to Exit"

while result_Keypress <> 'Ctrl+ C':
    result_Keypress = obj_keypress.keypress()
    print result_Keypress

    
```
[![](https://github.com/faustobranco/keypress/blob/master/Capture.PNG)](https://github.com/faustobranco/keypress/blob/master/Capture.PNG)

## Versioning
```
=======================================================================================
== Log Changes: 
== Date:            2018-04-03
== Author:          Fausto Branco
== Version:         1.0.0
== Description:     Initial Version
=======================================================================================

```
## Authors
```
=======================================================================================
== Script Info:		keypress.py - Class with functions to capture pressed keys 
==
=======================================================================================
== Create Author:	Fausto Branco
== Create Date:		2018-04-03
== Actual Version:  1.0.0
== Description:		
=======================================================================================
== Log Changes:
== Date:            2018-04-03
== Author:          Fausto Branco
== Version:         1.0.0
== Description:     Initial Version
=======================================================================================
```
## License



