@echo off
cls

pyinstaller --name=PttOneTimePasswordDemo --icon=PTTOTP.ico --windowed --onefile PTTOTP/ptt_otp.py

