from time import sleep
from progress.bar import Bar

file = open('main.py', 'r')
# while True:
#     c = file.read(1)
#     if not c: break
#     print(c, end='')
#     sleep(0.1)
    

# numberOfCharacters = len(file.read())
# print(numberOfCharacters)

with Bar('Processing', max=len(file.read())) as bar:
    file.seek(0)
    while True:
        c = file.read(1)
        if not c: break
        # sleep(0.1)
        bar.next()