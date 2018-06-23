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

    os.remove(OutputFile)
    subprocess.run(['pyinstaller', '--onefile', '--icon=./PTTOTP/Res/PTTOTP.ico', './PTTOTP/PTTOTP.py'], stdout=subprocess.PIPE).stdout.decode('utf-8')

    if not os.path.isfile(OutputFile):
        print('編譯執行檔失敗')
        sys.exit()
    print('編譯執行檔成功')

    print('目前版本: ' + VersionStr)

    WindowsPackFolder = 'PTTOTP_Windows_' + VersionFileStr

    try:
        shutil.rmtree(WindowsPackFolder)
    except:
        pass
    time.sleep(1)
    os.mkdir(WindowsPackFolder)

    copyfile(OutputFile, WindowsPackFolder + '/' + OutputFileName)

    if not os.path.isfile(WindowsPackFolder + '/' + OutputFileName):
        print('打包失敗')
        sys.exit()

    print('Windows 版本 PTT One-Time Password 打包成功')

PackFileList = [
    ('./PTTOTP/', 'PTTOTP.py'), 
    ('./PTTOTP/', 'eula.txt'),
    ('./PTTOTP/', 'Res'),
]

LinuxPackFolder = 'PTTOTP_Linux_' + VersionFileStr + '/'
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