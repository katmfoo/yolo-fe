import os
import glob
import math
import dataset_functions

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

def generateTestFile(dataset, test_percentage):
    print('test file')