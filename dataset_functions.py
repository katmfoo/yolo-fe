import os
import fnmatch

def datasetDirExists():
    if os.path.isdir('datasets'):
        return True
    else:
        return False

def getDatasets():
    if not datasetDirExists():
        return []
    else:
        datasets = []
        all_files = os.listdir('datasets')
        for item in all_files:
            if os.path.isdir('datasets/' + item):
                if os.path.isfile('datasets/' + item + '/' + item + '.names'):
                    datasets.append(item)
        return datasets

def getDataset(dataset):
    if not dataset in getDatasets():
        return False
    else:
        return_obj = []
        all_files = os.listdir('datasets/' + dataset)
        for item in all_files:
            if os.path.isdir('datasets/' + dataset + '/' + item):
                num_txt = len(fnmatch.filter(os.listdir('datasets/' + dataset + '/' + item), '*.txt'))
                num_jpg = len(fnmatch.filter(os.listdir('datasets/' + dataset + '/' + item), '*.jpg'))
                num_jpeg = len(fnmatch.filter(os.listdir('datasets/' + dataset + '/' + item), '*.jpeg'))
                num_png = len(fnmatch.filter(os.listdir('datasets/' + dataset + '/' + item), '*.png'))
                return_obj.append([item, num_jpg + num_jpeg + num_png, num_txt])
        return return_obj