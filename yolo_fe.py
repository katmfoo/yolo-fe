import click

@click.group()
def cli():
    pass

@cli.command()
def setup():
    '''Automatically downloads and sets up YOLO in the current directory'''

    # Run script to automatically download and setup YOLO

    print('YOLO has been setup successfully')