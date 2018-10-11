# yolo-fe
Command line tool for interfacing with the YOLO system and applying different methods of feature extraction to image datasets. This tool is made specifically to be ran on a computer running Ubuntu 16.04 with a CUDA enabled GPU (with appropriate drivers + CUDA installed).

## Requirements
* Python3
* Python setuptools module (https://pypi.org/project/setuptools/)

## How to install
1. Run `git clone https://github.com/pricheal/yolo-fe.git`
2. Inside repository, run `sudo python3 setup.py develop`
3. Run `yolo-fe` to use command line tool

## Usage
The command line tool is accessed with `yolo-fe`. Running `yolo-fe --help` will display the various subcommands that can be ran. Running `yolo-fe subcommand --help` will display more information for that particular subcommand.

#### yolo-fe setup

The setup subcommand can be ran to automatically download, configure, and install the YOLO system to the yolo/ directory.

## Cloud instance used for testing

This tool was tested using a Google Cloud instance with the following specifications.
* Region: us-east4
* Machine type: 1vCPU, 3.75 GB memory
* GPU: 1 NVIDIA Tesla P4
* Boot disk: 20GB standard persistent, Ubuntu 16.04 LTS
