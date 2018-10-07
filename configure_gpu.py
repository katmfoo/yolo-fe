def configure_gpu():
    print('Now configuring YOLO to utilize GPU...')
    with open("Makefile", "rt") as fin:
        with open("Makefile", "wt") as fout:
            for line in fin:
                fout.write(line.replace('GPU=0', 'GPU=1'))