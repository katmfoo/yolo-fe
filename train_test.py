import os
import glob
import math
import dataset_functions

def generateDataFile(dataset, train_percentage):
    train_file_path = generateTrainFile(dataset, train_percentage)
    test_file_path = generateTestFile(dataset, 100 - train_percentage)

    names_file_path = os.path.dirname(os.path.realpath(__file__)) + "/datasets/" + dataset + "/" + dataset + ".names"

    num_classes = 0
    for line in open(names_file_path,"r").readlines():
        if line != "":
            num_classes = num_classes + 1
    
    data_file = open('yolo/yolo-fe.data', 'w')
    data_file.write('classes = ' + str(num_classes) + "\n")
    data_file.write('train = ' + train_file_path + "\n")
    data_file.write('valid = ' + test_file_path + "\n") 
    data_file.write('names = ' + names_file_path + "\n")
    data_file.write('backup = backup')
    data_file.close()

    return os.path.dirname(os.path.realpath(__file__)) + "/yolo/yolo-fe.data"

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