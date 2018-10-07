import os

def configure_gpu():
    print('Now configuring YOLO to utilize GPU...')
    with open("yolo/Makefile", "rt") as fin:
        with open("yolo/Makefile_new", "wt") as fout:
            for line in fin:
                new_line = line.replace('GPU=0', 'GPU=1')
                new_line = new_line.replace('/usr/local/cuda/', '/usr/local/cuda-9.0/')
                fout.write(new_line)
    os.remove('yolo/Makefile')
    os.rename('yolo/Makefile_new', 'yolo/Makefile')