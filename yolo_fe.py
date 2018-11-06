import click
import yolo_setup
import dataset_functions
import train_test

DEFAULT_TRAIN_PERCENTAGE = 70

@click.group()
def cli():
    pass

@cli.command()
@click.option('--gpu/--cpu', default=True, help='Flag to build YOLO to either use the GPU or CPU, GPU if not specified')
@click.option('--cuda-path', default=False, help='Specify the path to CUDA, default is /usr/local/cuda-9.0/')
@click.option('--omit-weight-file', is_flag=True, default=False, help='Flag to omit downloading the pretrained convolutional weight file')
def setup(gpu, cuda_path, omit_weight_file):
    '''Automatically download, configure, and build YOLO to the yolo/ directory.'''

    yolo_setup.download()

    if cuda_path:
        yolo_setup.configure(enable_gpu=gpu, cuda_path=cuda_path)
    else:
        yolo_setup.configure(enable_gpu=gpu)

    yolo_setup.install()

    if not omit_weight_file:
        yolo_setup.downloadConvolutionalWeights()

    print('YOLO has been setup successfully')

@cli.command()
def datasets():
    '''List the properly setup datasets within the datasets/ directory.'''

    if not dataset_functions.datasetDirExists():
        print('The datasets/ directory does not exist')
        return
    else:
        datasets = dataset_functions.getDatasets()

        if not datasets:
            print('There are no datasets within the datasets/ directory')
            return
        else:
            for dataset in datasets:
                print(dataset)

@cli.command()
@click.argument('dataset')
def dataset(dataset):
    '''View information about a specific dataset.'''

    dataset_obj = dataset_functions.getDataset(dataset)

    if not dataset_obj:
        print("Dataset '" + dataset + "' does not exist or is not configured properly")
        return
    elif not yolo_setup.yoloSetup():
        print("YOLO has not been setup correctly yet, run the setup command to do so")
    else:
        for class_folder in dataset_obj:
            print("Object class folder '" + class_folder[0] + "' contains " + str(class_folder[1]) + " images and " + str(class_folder[2]) + " bounds files.")

@cli.command()
@click.argument('dataset')
@click.option('--train-percentage', type=int, default=DEFAULT_TRAIN_PERCENTAGE, help='Specify the percentage of dataset to use for training, default first 70% of each (automatically) sorted classification group. Remaining percentage should be used for testing.')
def train(dataset, train_percentage):
    '''Train an image classifier with the given image dataset.'''

    dataset_obj = dataset_functions.getDataset(dataset)

    if not dataset_obj:
        print("Dataset '" + dataset + "' does not exist or is not configured properly")
    else:
        data_file_location = train_test.generateDataFile(dataset, train_percentage)
        print(data_file_location)