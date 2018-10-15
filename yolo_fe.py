import click
from yolo_setup import download, configure, install

@click.group()
def cli():
    pass

@cli.command()
@click.option('--gpu/--cpu', default=True, help='Flag to build YOLO to either use the GPU or CPU, GPU if not specified')
@click.option('--cuda-path', default=False, help='Specify the path to CUDA, default is /usr/local/cuda-9.0/')
def setup(gpu, cuda_path):
    '''Automatically downloads, configures, and builds YOLO to the yolo/ directory.'''

    download()

    if cuda_path:
        configure(enable_gpu=gpu, cuda_path=cuda_path)
    else:
        configure(enable_gpu=gpu)

    install()

    print('YOLO has been setup successfully')
