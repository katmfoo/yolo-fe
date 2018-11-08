import os
import glob
import math
import dataset_functions

def generateConfigFile(dataset):
    names_file_path = os.path.dirname(os.path.realpath(__file__)) + "/datasets/" + dataset + "/" + dataset + ".names"
    num_classes = getNumClasses(names_file_path)
    new_classes_string = 'classes=' + str(num_classes)

    filters_val = (num_classes + 5) * 3
    new_filters_string = 'filters=' + str(filters_val)

    data_string = "[net]\n# Testing\n# batch=1\n# subdivisions=1\n# Training\nbatch=64\nsubdivisions=16\nwidth=608\nheight=608\nchannels=3\nmomentum=0.9\ndecay=0.0005\nangle=0\nsaturation = 1.5\nexposure = 1.5\nhue=.1\nlearning_rate=0.001\nburn_in=1000\nmax_batches = 500200\npolicy=steps\nsteps=400000,450000\nscales=.1,.1\n[convolutional]\nbatch_normalize=1\nfilters=32\nsize=3\nstride=1\npad=1\nactivation=leaky\n# Downsample\n[convolutional]\nbatch_normalize=1\nfilters=64\nsize=3\nstride=2\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=32\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=64\nsize=3\nstride=1\npad=1\nactivation=leaky\n[shortcut]\nfrom=-3\nactivation=linear\n# Downsample\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=3\nstride=2\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=64\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=3\nstride=1\npad=1\nactivation=leaky\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=64\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=3\nstride=1\npad=1\nactivation=leaky\n[shortcut]\nfrom=-3\nactivation=linear\n# Downsample\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=3\nstride=2\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=3\nstride=1\npad=1\nactivation=leaky\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=3\nstride=1\npad=1\nactivation=leaky\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=3\nstride=1\npad=1\nactivation=leaky\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=3\nstride=1\npad=1\nactivation=leaky\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=3\nstride=1\npad=1\nactivation=leaky\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=3\nstride=1\npad=1\nactivation=leaky\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=3\nstride=1\npad=1\nactivation=leaky\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=3\nstride=1\npad=1\nactivation=leaky\n[shortcut]\nfrom=-3\nactivation=linear\n# Downsample\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=3\nstride=2\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=3\nstride=1\npad=1\nactivation=leaky\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=3\nstride=1\npad=1\nactivation=leaky\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=3\nstride=1\npad=1\nactivation=leaky\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=3\nstride=1\npad=1\nactivation=leaky\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=3\nstride=1\npad=1\nactivation=leaky\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=3\nstride=1\npad=1\nactivation=leaky\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=3\nstride=1\npad=1\nactivation=leaky\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=3\nstride=1\npad=1\nactivation=leaky\n[shortcut]\nfrom=-3\nactivation=linear\n# Downsample\n[convolutional]\nbatch_normalize=1\nfilters=1024\nsize=3\nstride=2\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=1024\nsize=3\nstride=1\npad=1\nactivation=leaky\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=1024\nsize=3\nstride=1\npad=1\nactivation=leaky\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=1024\nsize=3\nstride=1\npad=1\nactivation=leaky\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=1024\nsize=3\nstride=1\npad=1\nactivation=leaky\n[shortcut]\nfrom=-3\nactivation=linear\n######################\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=1\npad=1\nfilters=1024\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=1\npad=1\nfilters=1024\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=1\npad=1\nfilters=1024\nactivation=leaky\n[convolutional]\nsize=1\nstride=1\npad=1\nfilters=255\nactivation=linear\n[yolo]\nmask = 6,7,8\nanchors = 10,13,  16,30,  33,23,  30,61,  62,45,  59,119,  116,90,  156,198,  373,326\nclasses=80\nnum=9\njitter=.3\nignore_thresh = .7\ntruth_thresh = 1\nrandom=1\n[route]\nlayers = -4\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=leaky\n[upsample]\nstride=2\n[route]\nlayers = -1, 61\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=1\npad=1\nfilters=512\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=1\npad=1\nfilters=512\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=1\npad=1\nfilters=512\nactivation=leaky\n[convolutional]\nsize=1\nstride=1\npad=1\nfilters=255\nactivation=linear\n[yolo]\nmask = 3,4,5\nanchors = 10,13,  16,30,  33,23,  30,61,  62,45,  59,119,  116,90,  156,198,  373,326\nclasses=80\nnum=9\njitter=.3\nignore_thresh = .7\ntruth_thresh = 1\nrandom=1\n[route]\nlayers = -4\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=leaky\n[upsample]\nstride=2\n[route]\nlayers = -1, 36\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=1\npad=1\nfilters=256\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=1\npad=1\nfilters=256\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=1\npad=1\nfilters=256\nactivation=leaky\n[convolutional]\nsize=1\nstride=1\npad=1\nfilters=255\nactivation=linear\n[yolo]\nmask = 0,1,2\nanchors = 10,13,  16,30,  33,23,  30,61,  62,45,  59,119,  116,90,  156,198,  373,326\nclasses=80\nnum=9\njitter=.3\nignore_thresh = .7\ntruth_thresh = 1\nrandom=1"

    data_string = data_string.replace('batch=64', 'batch=64')
    data_string = data_string.replace('subdivisions=16', 'subdivisions=32')
    data_string = data_string.replace('classes=80', new_classes_string)
    data_string = data_string.replace('filters=255', new_filters_string)
    data_string = data_string.replace('random=1', 'random=0')

    data_file = open('yolo/yolo-fe.cfg', 'w')
    data_file.write(data_string)
    data_file.close()

    return os.path.dirname(os.path.realpath(__file__)) + "/yolo/yolo-fe.cfg"

def generateDataFile(dataset, train_percentage):
    train_file_path = generateTrainFile(dataset, train_percentage)
    test_file_path = generateTestFile(dataset, 100 - train_percentage)

    names_file_path = os.path.dirname(os.path.realpath(__file__)) + "/datasets/" + dataset + "/" + dataset + ".names"

    num_classes = getNumClasses(names_file_path)
    
    data_file = open('yolo/yolo-fe.data', 'w')
    data_file.write('classes = ' + str(num_classes) + "\n")
    data_file.write('train = ' + train_file_path + "\n")
    data_file.write('valid = ' + test_file_path + "\n") 
    data_file.write('names = ' + names_file_path + "\n")
    data_file.write('backup = backup')
    data_file.close()

    return os.path.dirname(os.path.realpath(__file__)) + "/yolo/yolo-fe.data"

def getNumClasses(names_file_path):
    num_classes = 0
    for line in open(names_file_path,"r").readlines():
        if line != "":
            num_classes = num_classes + 1
    return num_classes

def generateTrainFile(dataset, train_percentage):

    dataset_obj = dataset_functions.getDataset(dataset)
    class_files = []
    current_path = os.path.dirname(os.path.realpath(__file__))

    for object_class in dataset_obj:
        all_class_files = []
        all_class_files.extend(glob.glob('datasets/' + dataset + '/' + object_class[0] + "/*.jpg"))
        all_class_files.extend(glob.glob('datasets/' + dataset + '/' + object_class[0] + "/*.jpeg"))
        all_class_files.extend(glob.glob('datasets/' + dataset + '/' + object_class[0] + "/*.png"))

        all_class_files.sort()

        last_file_num = math.floor(len(all_class_files) * (train_percentage / 100))

        for x in range(0, last_file_num):
            class_files.append(current_path + "/" + all_class_files[x])

    with open('yolo/train.txt', 'w') as the_file:
        i = 0
        for line in class_files:
            if i < len(class_files) - 1:
                the_file.write(line + '\n')
            else:
                the_file.write(line)
            i = i + 1
    return current_path + "/yolo/train.txt"

def generateTestFile(dataset, test_percentage):
    
    dataset_obj = dataset_functions.getDataset(dataset)
    class_files = []
    current_path = os.path.dirname(os.path.realpath(__file__))

    for object_class in dataset_obj:
        all_class_files = []
        all_class_files.extend(glob.glob('datasets/' + dataset + '/' + object_class[0] + "/*.jpg"))
        all_class_files.extend(glob.glob('datasets/' + dataset + '/' + object_class[0] + "/*.jpeg"))
        all_class_files.extend(glob.glob('datasets/' + dataset + '/' + object_class[0] + "/*.png"))

        all_class_files.sort()

        first_file_num = math.floor(len(all_class_files) * ((100 - test_percentage) / 100))

        for x in range(first_file_num, len(all_class_files)):
            class_files.append(current_path + "/" + all_class_files[x])

    with open('yolo/test.txt', 'w') as the_file:
        i = 0
        for line in class_files:
            if i < len(class_files) - 1:
                the_file.write(line + '\n')
            else:
                the_file.write(line)
            i = i + 1
    return current_path + "/yolo/test.txt"