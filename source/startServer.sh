#!/bin/sh

cd /home/ubuntu/kaushik 
FLASK_APP=server.py /home/ubuntu/anaconda3/bin/flask run -h 0.0.0.0 -p 8000

