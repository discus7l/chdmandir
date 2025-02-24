import os
from pprint import pprint
import subprocess

# List all directories in the given path
path = os.getcwd()

# List the files and directories in the specified path
rootDir = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

# List the files in the child directories within the root directory
# Get file names from child directory
# Run chdman if cue file is found
for rootI in rootDir:
    childDir = os.listdir(f'{path}/{rootI}')
    for fileNames in childDir:
        if os.path.splitext(fileNames)[1] == '.cue':
            noExtFileName = os.path.splitext(fileNames)[0]
            iFile = f"{path}/{rootI}/{fileNames}"
            oFile = f"{path}/{noExtFileName}.chd"
            subprocess.run(['chdman.exe', 'createcd', '-i', iFile, '-o', oFile])


