import click
from yolo_setup import download, configure, install

@click.group()
def cli():
    pass

@cli.command()
@click.option('--gpu/--cpu', default=True)
@click.option('--cuda-path', default=False)
def setup(gpu, cuda_path):
    '''Automatically downloads, configures, and builds YOLO to the yolo/ directory.'''

    download()

    if cuda_path:
        configure(enable_gpu=gpu, cuda_path=cuda_path)
    else:
        configure(enable_gpu=gpu)

    install()

    print('YOLO has been setup successfully')
