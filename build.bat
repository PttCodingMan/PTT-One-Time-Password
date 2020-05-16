@echo off
cls

pyinstaller --name=PttOneTimePasswordDemo --icon=src/PTTOTP.ico --windowed --onefile src/ptt_otp.py

