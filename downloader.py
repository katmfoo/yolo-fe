#! usr/bin/python3.6

# This script will download the YOLO image classifier tool
# automatically install it in a user specified dir.
# Created by Team Golden Retrievers.

import subprocess
import shutil
from configure_gpu import configure_gpu

def download():
    # This is the main method for this script.
    # It will prompt the user to set the dir
    # that they want python to install the 
    # classifier in and procede to download it
    # and install it in that directory.

    # Remove potential old directories
    shutil.rmtree('darknet')
    shutil.rmtree('yolo')

    print("Beginning download of YOLO tool.")
    subprocess.check_output(['git','clone','https://github.com/pjreddie/darknet'])
    subprocess.check_output(['mv', 'darknet', 'yolo'])
    install()

def install():
    # This function will run the makefile on 
    # the newly downloaded yolo tool.
    configure_gpu()
    print("Running make command on yolo tool.")
    subprocess.check_output(['make'], cwd='yolo')