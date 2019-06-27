#!/usr/bin/bash

clear
rm -f *.pyc designs/*.pyc modules/*.pyc
rm -frd designs/__pycache__ modules/__pycache__
# exit
chmod +x main.py
python3 main.py
#run background
# nohup python3 main.py &
# python -m py_compile main.py
