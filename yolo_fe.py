import click
from downloader import download

@click.group()
def cli():
    pass

@cli.command()
def setup():
    '''Automatically downloads, configures, and builds YOLO to the yolo/ directory.'''

    # Run script to automatically download and setup YOLO
    download()

    print('YOLO has been setup successfully')
