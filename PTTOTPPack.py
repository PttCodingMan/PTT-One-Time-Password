import os
import sys
import subprocess
import shutil
from shutil import copyfile

import time

with open('./PTTOTP/Version.py') as VersionFile:
    VersionStr = VersionFile.read()

VersionStr = VersionStr[VersionStr.find('\'') + 1 : ]
VersionStr = VersionStr[:VersionStr.find('\'')]

VersionFileStr = VersionStr.replace(' ', '_')

if os.name == 'nt':
    OutputFileName = 'PTTOTP.exe'
    OutputFile = './dist/' + OutputFileName
    try:
        shutil.rmtree('dist')
    except:
        pass
    time.sleep(1)
    subprocess.run(['pyinstaller', '--onefile', '--icon=./PTTOTP.ico', './PTTOTP/PTTOTP.py'], stdout=subprocess.PIPE).stdout.decode('utf-8')

    if not os.path.isfile(OutputFile):
        print('編譯執行檔失敗')
        sys.exit()
    print('編譯執行檔成功')

    print('目前版本: ' + VersionStr)

    WindowsPackFolder = 'PTTOTP_Windows_' + VersionFileStr + '/'

    try:
        shutil.rmtree(WindowsPackFolder)
    except:
        pass
    time.sleep(1)
    os.mkdir(WindowsPackFolder)

    PackFileList = [
        ('./dist/', 'PTTOTP.exe'), 
        ('./PTTOTP/', 'eula.txt'),
        ('./PTTOTP/', 'Res'),
    ]

    for Path, File in PackFileList:
        if os.path.isfile(Path + File):
            copyfile(Path + File, WindowsPackFolder + File)
    else:
        shutil.copytree(Path + File, WindowsPackFolder + File)

    print('Windows 版本 PTT One-Time Password 打包成功')
else:
    PackFileList = [
        ('./dist/', 'PTTOTP'),
        ('./PTTOTP/', 'eula.txt'),
        ('./PTTOTP/', 'Res'),
    ]

    LinuxPackFolder = 'PTTOTP_Linux_' + VersionFileStr + '/'

    try:
        shutil.rmtree('dist')
    except:
        pass
    time.sleep(1)
    subprocess.run(['pyinstaller', '--onefile', './PTTOTP/PTTOTP.py'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    
    try:
        shutil.rmtree(LinuxPackFolder)
    except:
        pass
    time.sleep(1)
    os.mkdir(LinuxPackFolder)

    for Path, File in PackFileList:
        if os.path.isfile(Path + File):
            copyfile(Path + File, LinuxPackFolder + File)
        else:
            shutil.copytree(Path + File, LinuxPackFolder + File)

    print('Linux 版本 PTT One-Time Password 打包成功')