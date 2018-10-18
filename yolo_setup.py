# This file contains all of the necessary functions to download, configure, and install
# the YOLO system.

import subprocess
import shutil
import os
import click

def download():
    """Downloads the YOLO system to the yolo/ directory"""

    click.echo("Removing old install directories...")
    if os.path.isdir('darknet'):
        shutil.rmtree('darknet')
    if os.path.isdir('yolo'):
        shutil.rmtree('yolo')

    click.echo("Downloading darknet repository...")
    subprocess.check_output(['git','clone','https://github.com/pjreddie/darknet'])
    subprocess.check_output(['mv', 'darknet', 'yolo'])

def configure(**kwargs):
    """Configures the Makefile of the YOLO system before building"""

    # Setup enable_gpu variable
    if "enable_gpu" in kwargs:
        if kwargs['enable_gpu']:
            click.echo("Enabling GPU in the Makefile...")
        enable_gpu = kwargs['enable_gpu']
    else:
        enable_gpu = True

    # Setup cuda_path variable
    if "cuda_path" in kwargs:
        click.echo("Setting CUDA path to " + kwargs['cuda_path'] + " in the Makefile...")
        cuda_path = kwargs['cuda_path']
    else:
        cuda_path = "/usr/local/cuda-9.0/"

    # Make modifications to Makefile
    with open("yolo/Makefile", "rt") as fin:
        with open("yolo/Makefile_new", "wt") as fout:
            for line in fin:
                if enable_gpu:
                    new_line = line.replace('GPU=0', 'GPU=1')
                else:
                    new_line = line

                new_line = new_line.replace('/usr/local/cuda/', cuda_path)
                fout.write(new_line)

    os.remove('yolo/Makefile')
    os.rename('yolo/Makefile_new', 'yolo/Makefile')

def install():
    """Runs the Makefile for the YOLO system"""

    click.echo("Running make command...")
    subprocess.check_output(['make'], cwd='yolo')
