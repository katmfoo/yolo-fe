from setuptools import setup

setup(
    name='yolo-fe',
    version='1.0',
    py_modules=['yolo-fe'],
    install_requires=[
        'click',
        'opencv-python'
    ],
    entry_points='''
        [console_scripts]
        yolo-fe=yolo_fe:cli
    '''
)
