import sys
import traceback
import os
import time
import json
import getpass
from time import gmtime, strftime
from PTTLibrary import PTT
import pyotp
import Version
from shutil import copyfile
import webbrowser
import subprocess

def log(InputMessage):
    TotalMessage = "[" + strftime("%m-%d %H:%M:%S") + "][OTP] " + InputMessage
    try:
        print(TotalMessage.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
    except Exception:
        print(TotalMessage.encode('utf-8', "replace").decode('utf-8'))

def getFileTime():
    return strftime("%m.%d_%H.%M.%S")

QRCodeHTMLSample = '''
<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <title>Welcome</title>
</head>
<html>
  <body>
    嗨 ==ID== 感謝您使用 PTT One-Time Password v ==Version== <br/>
    請使用 Google authenticator 或相容 APP 掃描此 QRCode <br/><br/>
    <canvas id="qr"></canvas>
    <script src="./Res/qrious.js"></script>
    <script>
      (function() {
        var qr = new QRious({
          element: document.getElementById('qr'),
          value: '==Value=='
        });
      })();
    </script>
  </body>
</html>
'''

# ID
# Password
# OTPKey
# LastPassword
# PrePassword

# OTPConfig.txt
# 

OTPConfig = {}
ID = ''
Password = ''
LastPassword = ''
PrePassword = ''
OTPKey = ''
OTPKeySystemBackupPath = ''
isWindows = False

def getIDPW():
    global OTPConfig
    global ID
    global Password

    ID = input('請輸入帳號: ')
    Password = getpass.getpass('請輸入密碼: ')
    OTPConfig['ID'] = ID
    OTPConfig['Password'] = Password
def genOTPKey():
    global OTPConfig
    global OTPKey
    global OTPKeySystemBackupPath

    print('產生 OTP 金鑰')
    OTPKey = pyotp.random_base32()
    OTPConfig['OTPKey'] = OTPKey

    with open(OTPKeySystemBackupPath + getFileTime() + '.txt', 'w') as BackupKeyFile:
        BackupKeyFile.write(OTPKey)

    OTPURL = pyotp.totp.TOTP(OTPKey).provisioning_uri(ID, issuer_name="PTT OTP")
    with open('QRCode.html', 'w', encoding='utf-8') as QRCodeFile:
        QRCodeHTML = QRCodeHTMLSample
        QRCodeHTML = QRCodeHTML.replace('==ID==', ID)
        QRCodeHTML = QRCodeHTML.replace('==Version==', Version.Ver)
        QRCodeHTML = QRCodeHTML.replace('==Value==', OTPURL)
        QRCodeFile.write(QRCodeHTML)
    
    ExecutePath = os.path.dirname(os.path.abspath( __file__ ))
    webbrowser.open(ExecutePath + '/QRCode.html')

def setLastPassword():
    global OTPConfig
    global Password
    global LastPassword

    LastPassword = Password
    OTPConfig['LastPassword'] = LastPassword

def detectOS():
    global isWindows
    isWindows = (os.name == 'nt')

def BackupCheck():
    global OTPKeySystemBackupPath
    global isWindows
    if isWindows:
        OTPKeySystemBackupPath = os.getenv('APPDATA') + '/PTTOTP/'
    else:
        print()
        OTPKeySystemBackupPath = os.environ['HOME'] + '/PTTOTP/'

    if not os.path.exists(OTPKeySystemBackupPath):
        os.makedirs(OTPKeySystemBackupPath)

    WriteFileTestFilePath = OTPKeySystemBackupPath + 'WriteFileTest.txt'
    with open(WriteFileTestFilePath, 'w') as WriteFileTestFile:
        WriteFileTestFile.write('If you see this line, write file test is success.')

    if not os.path.isfile(WriteFileTestFilePath):
        print('請確認此程式具備寫檔權限')
        sys.exit()
    
    os.remove(WriteFileTestFilePath)

    if os.path.isfile(WriteFileTestFilePath):
        print('請確認此程式具備刪除權限')
        sys.exit()

def readOTPConfig(FileName):
    global ID
    global OTPKey
    global OTPConfig
    global Password
    global LastPassword
    global PrePassword
    
    try:
        with open(FileName) as OTPConfigFile:
            OTPConfig = json.load(OTPConfigFile)
    except:
        return False
    
    try:
        ID = OTPConfig['ID']
        Password = OTPConfig['Password']
    except:
        getIDPW()
    
    try:
        OTPKey = OTPConfig['OTPKey']
    except:
        genOTPKey()
    
    try:
        LastPassword = OTPConfig['LastPassword']
        PrePassword = OTPConfig['PrePassword']
    except:
        setLastPassword()
    
    return True

print('歡迎使用 PTT OTP v ' + Version.Ver)

detectOS()
BackupCheck()

log('最新版本檢查')

NumberStr = '0123456789'

RemoteVersion = subprocess.run(['pip', 'search', 'PTTOTP'], stdout=subprocess.PIPE).stdout.decode('utf-8')
RemoteVersion = RemoteVersion[RemoteVersion.find('(') + 1 : RemoteVersion.find(')')]

RemoteVersionTemp = RemoteVersion
RemoteVersionTemp = ''.join(c for c in RemoteVersionTemp if c in NumberStr)

CurrentVersionTemp = Version.Ver
CurrentVersionTemp = CurrentVersionTemp[:CurrentVersionTemp.find(' ')]
CurrentVersionTemp = ''.join(c for c in CurrentVersionTemp if c in NumberStr)

# print(RemoteVersionTemp)
# print(CurrentVersionTemp)

if int(RemoteVersionTemp) > int(CurrentVersionTemp):
    log('目前最新版本: ' + RemoteVersion)
    log('目前使用版本: ' + Version.Ver)
    log('已有更新版本，請更新 PTT One-Time Password 至最新版本')
else:
    log('已是最新版本')

if not readOTPConfig('OTPConfig.txt'):
    if os.path.isfile(OTPKeySystemBackupPath + 'OTPConfig.txt'):
        print('發現先前備份的 PTT One-Time Password 金鑰')
        c = input('請問要復原資料嗎? [Y/n] ').lower()
        GenOTPKey = False
        if c == 'y' or c == '':
            if not readOTPConfig(OTPKeySystemBackupPath + 'OTPConfig.txt'):
                print('復原失敗')
                GenOTPKey = True
        else:
            GenOTPKey = True
        
        if GenOTPKey:
            
            with open('eula.txt', encoding='utf-8') as EulaFile:
                Eula = EulaFile.read()
            
            EulaPart = ''
            if not ': yes' in Eula:
                print('請詳閱以下內容')
                for line in Eula.split('\n'):
                    if '========================' in line:
                        break
                    EulaPart += line + '\n'
                    print(line)
                
                C = input('請問您同意以上條款?(yes/no): ').lower()
                print('PTT One-Time Password 感謝您')
                if C != 'yes':
                    sys.exit()
                EulaPart += '請問您同意以上條款? (yes/no)\n: yes'
                
                with open('eula.txt', 'w') as EulaFile:
                    EulaFile.write(EulaPart)
            
            print('初次使用將引導您輸入必要資訊，初始化後請嚴加保存 OTPConfig.txt')
            getIDPW()
            genOTPKey()
            setLastPassword()
        with open('OTPConfig.txt', 'w') as OTPConfigFile:
                json.dump(OTPConfig, OTPConfigFile)
OTP = pyotp.TOTP(OTPKey)
PTTBot = PTT.Library()
ErrCode = PTTBot.login(ID, Password)
if ErrCode != PTT.ErrorCode.Success:
    ErrCode = PTTBot.login(ID, LastPassword)
    if ErrCode != PTT.ErrorCode.Success:
        ErrCode = PTTBot.login(ID, PrePassword)
        if ErrCode != PTT.ErrorCode.Success:
            PTTBot.Log('登入失敗')
            sys.exit()
        LastPassword = PrePassword
    else:
        pass
else:
    LastPassword = Password

isFirstRound = True

try:
    while True:
        CurrentOTP = OTP.now()

        if LastPassword != CurrentOTP:
            
            OTPConfig['LastPassword'] = CurrentOTP
            OTPConfig['PrePassword'] = LastPassword

            copyfile('OTPConfig.txt', OTPKeySystemBackupPath + 'PreOTPConfig.txt')
            with open('OTPConfig.txt', 'w') as OTPConfigFile:
                json.dump(OTPConfig, OTPConfigFile)
            with open(OTPKeySystemBackupPath + 'OTPConfig.txt', 'w') as OTPConfigFile:
                json.dump(OTPConfig, OTPConfigFile)
            
            log('準備更改密碼 ' + LastPassword + ' -> ' + CurrentOTP)

            ErrCode = PTTBot.changePassword(LastPassword, CurrentOTP)
            # ErrCode = PTTBot.changePassword(Password, Password)
            if ErrCode != PTT.ErrorCode.Success:
                log('失敗')
                break

            LastPassword = CurrentOTP

            if not isFirstRound:
                try:
                    time.sleep(27)
                except:
                    break;

            isFirstRound = False

        try:
            time.sleep(0.2)
        except:
            break;

except Exception as e:
        
    traceback.print_tb(e.__traceback__)
    print(e)
    PTTBot.Log('接到例外 啟動緊急應變措施')

ErrCode = PTTBot.changePassword(LastPassword, Password)
if ErrCode != PTT.ErrorCode.Success:
    ErrCode = PTTBot.changePassword(CurrentOTP, Password)
    if ErrCode != PTT.ErrorCode.Success:
        log('還原密碼失敗，請參考 OTPConfig.txt 還原您的密碼')
    else:
        log('密碼已經還原')    
else:
    log('密碼已經還原')
PTTBot.logout()