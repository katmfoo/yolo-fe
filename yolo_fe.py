import click
from yolo_setup import download, configure, install
from listFiles import listFiles
import os

DEFAULT_TRAIN_PERCENTAGE = 70

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

@cli.command()
def datasets():
    '''Lets you view the datasets within the datasets/ directory.'''
    data = listFiles()

    if data == False:
        print('The datasets/ directory does not exist')
    else:
        if not data:
            print('There are no datasets within the datasets/ directory')
        else:
            num = 1
            for dataset in data:
                print(str(num) + ". Dataset '" + dataset[0] + "' has " + str(dataset[1]) + " images and " + str(dataset[2]) + " bounds")
                num = num + 1

@cli.command()
@click.argument('dataset')
@click.option('--train-percentage', type=int, default=DEFAULT_TRAIN_PERCENTAGE, help='Specify the percentage of dataset to use for training, default first 70% of each (automatically) sorted classification group. Remaining percentage should be used for testing.')
def train(dataset, train_percentage):
    '''Lets you train an image classifier with the given image dataset.'''

    if not os.path.isdir('datasets/' + dataset):
        print("Dataset '" + dataset + "' does not exist")
        return