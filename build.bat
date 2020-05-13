@echo off
cls

pyinstaller --name=PttOneTimePassword --icon=PTTOTP.ico --windowed --onefile PTTOTP/ptt_otp.py

