# Interface Code
import shutil
import os
import src
import sys
import time


if __name__ == '__main__':

    indexer = src.index
    index = indexer.Index(sys.argv)
    index.execute_command()

