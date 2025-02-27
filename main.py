import os
import subprocess

# List all directories in the given path
# path = "C:/Users/yk/Desktop/temp/GAME/ROMs/saturn"
path = os.getcwd()

# Create .hidden dir for multi-disc games
if not os.path.exists(f'{path}/.hidden'):
    os.makedirs(f'{path}/.hidden')

# List the files and directories in the specified path
rootDir = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

# List the files in the child directories within the root directory
# Get file names from child directory
# Run chdman if cue file is found
for rootI in rootDir:
    childDir = os.listdir(f'{path}/{rootI}')

    cueCounter = 0
    multiDiscFileList = []
    for fileNames in childDir:
        if (os.path.splitext(fileNames)[1].casefold() == '.cue') or (os.path.splitext(fileNames)[1].casefold() == '.gdi'):
            cueCounter += 1

    # Write m3u file and place chd in .hidden dir if multidisc detected
    if cueCounter > 2:
        for fileNames in childDir:
            if (os.path.splitext(fileNames)[1].casefold() == '.cue') or (os.path.splitext(fileNames)[1].casefold() == '.gdi'):
                noExtFileName = os.path.splitext(fileNames)[0]
                multiDiscFileList.append(f'.hidden/{noExtFileName}.chd')
                iFile = f"{path}\{rootI}\{fileNames}"
                oFile = f"{path}\.hidden\{noExtFileName}.chd"
                subprocess.run(['chdman.exe', 'createcd', '-i', iFile, '-o', oFile])

        with open(f'{path}/{rootI}.m3u', 'w') as f:
            for disc in multiDiscFileList:
                f.write(f'{disc}\n')

    else:
        for fileNames in childDir:
            if (os.path.splitext(fileNames)[1].casefold() == '.cue') or (os.path.splitext(fileNames)[1].casefold() == '.gdi'):
                noExtFileName = os.path.splitext(fileNames)[0]
                iFile = f"{path}\{rootI}\{fileNames}"
                oFile = f"{path}\{noExtFileName}.chd"
                subprocess.run(['chdman.exe', 'createcd', '-i', iFile, '-o', oFile])

input('Press any key to exit.')
