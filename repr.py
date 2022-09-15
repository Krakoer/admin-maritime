from models import *

def read_context(path):
    with open(path, 'r') as f:
        conf_text = f.readlines()

    