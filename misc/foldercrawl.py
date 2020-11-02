import os

path = os.path.dirname(os.path.abspath(__file__))

path = os.environ['USERPROFILE']

for d in os.listdir(path):
    if os.path.isdir(d):
        if d[0] != '.':
            print(d)

# print(os.listdir(path))