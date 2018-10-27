import os
import fnmatch

def listFiles():
    if not os.path.isdir('datasets'):
        return False
    else:
        datasets = []
        subsets = os.listdir('datasets')
        for sets in subsets:
            if os.path.isdir('datasets/' + sets):
                num_txt = len(fnmatch.filter(os.listdir('datasets/' + sets), '*.txt'))
                num_jpg = len(fnmatch.filter(os.listdir('datasets/' + sets), '*.jpg'))
                num_jpeg = len(fnmatch.filter(os.listdir('datasets/' + sets), '*.jpeg'))
                num_png = len(fnmatch.filter(os.listdir('datasets/' + sets), '*.png'))
                datasets.append([sets, num_jpg + num_jpeg + num_png, num_txt])
        return datasets