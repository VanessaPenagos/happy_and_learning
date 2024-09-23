'''
open: open files
close: close files
with: context manager
r: read, w: write, a: append, +: read and write
'''

def run():
    with open('files/my_file.txt', 'w') as f:
        for i in range(10):
            f.write(str(i))

if __name__ == '__main__':
    run()
