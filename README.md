# yolo-fe (project name)
Command line tool for interfacing with the YOLO system and applying different methods of feature extraction to image datasets. This tool is made specifically to be ran on a computer running Ubuntu 16.04 with a CUDA enabled GPU (with appropriate drivers + CUDA installed).

## Requirements
* Python3
* Python setuptools module (https://pypi.org/project/setuptools/)

## How to install
1. Run `git clone https://github.com/pricheal/yolo-fe.git`
2. Inside repository, run `sudo python3 setup.py develop`
3. Ensure CUDA is in system path with `export PATH="/usr/local/cuda-9.0/bin/:$PATH"` (only needed for GPU)
4. Run `yolo-fe` to use command line tool

## Usage
The command line tool is accessed with `yolo-fe`. Running `yolo-fe --help` will display the various subcommands that can be ran. Running `yolo-fe subcommand --help` will display more information for that particular subcommand.

### Setup command
```
yolo-fe setup [--gpu/--cpu] [--cuda-path=/path/to/cuda/]
```
**WARNING**: CUDA must be added to the system path for the setup subcommand to work with the --gpu option (which is the default option). It can be added with `export PATH="/usr/local/cuda-9.0/bin/:$PATH"`.

The setup subcommand can be ran to automatically download, configure, and install the YOLO system to the yolo/ directory. Run `yolo-fe setup --help` to see all options. `--gpu` or `--cpu` can be appended to setup YOLO in either GPU or CPU mode, GPU mode is default. `--cuda-path /path/to/cuda/` can be used to manually set the system path to CUDA. Default is `/usr/local/cuda-9.0/` which is the resulting location after running the `cuda_gpu_driver_install.sh` GPU driver install script.

### Datasets command
```
yolo-fe datasets
```

The datasets subcommand can be ran to view the datasets within the datasets/ directory. After setting up yolo with the setup subcommand, a datasets/ directory should be created in the root of the repository and loaded with the desired image datasets. An image dataset is simply a folder that contains image files and a corresponding bounds text file for each image with the same name, excluding the file extension. The datasets/ directory and its contents are created manually by the user, and are required to perform the remaining subcommands.

## Cloud instance used for testing

This tool was tested using a Google Cloud instance with the following specifications.
* Region: us-east4
* Machine type: 1vCPU, 3.75 GB memory
* GPU: 1 NVIDIA Tesla P4
* Boot disk: 20GB standard persistent, Ubuntu 16.04 LTS

## Image datasets

The image datasets that we put together can be downloaded [here](https://drive.google.com/open?id=1DnF2nfDQck5OMdCl7pULXLrqlRQqroUJ).

### Downloading image datasets onto Ubuntu
* Download the google drive file with this python script: https://stackoverflow.com/a/39225039
* Install the unzip tool and unzip the downloaded zip file
