![PTTOTP: A PTT One-Time Password Bot in Python](https://i.imgur.com/zFxDCU7.png)
# PTT One-Time Password

###### PTT One-Time Password 是一個由 Python 實現 PTT 動態登入密碼的機器人，你可以在任何支援 python 的電腦執行此程式，
###### 在外就可以享受 PTT One-Time Password 給予的安全性
###### 
###### 測試平台: Windows 10, Ubuntu 18.04
###### 原始碼
###### github: https://github.com/Truth0906/PTTOTP
###### Pypi: https://pypi.org/project/PTTOTP/

How it works
-------------------
###### 您需要一台連接網路的主機，作為 PTT One-Time Password 主機，需要 PTT One-Time Password 保護您的帳號時，需要
###### 保持開啟狀態。
###### PTT One-Time Password 在保護您的 PTT 帳號期間，會根據演算法產生的 One-Time Password 去定期地去修改 PTT 帳號
###### 的密碼，以達到動態密碼的效果。

重要
-------------------
###### 初始化程式後，會在程式資料夾產生一個 OTPConfig.txt 內含所有 PTT One-Time Password 相關重要資訊，請妥當保管備份
###### 如果遺失，作者也無法將您的帳號密碼恢復，請洽 PTT 帳號部，協助恢復您的帳號密碼。
###### 如果您的 PTT One-Time Password，不幸因為各種原因當機或者關閉，您可以直接重新重啟程式，
###### 程式會自動恢復您的 One-Time Password 功能。

版本
-------------------
###### 0.0.2 dev

安裝
-------------------
###### 近期推出安裝包

需求
-------------------
###### Python 3.6

相依函式庫
-------------------
###### PTTLibrary
###### pyotp

未來工作
-------------------

贊助
-------------------
###### 如果這個專案對你很有幫助，你可以贊助我一杯咖啡 :D
###### XMR 贊助位址
###### 448CUe2q4Ecf9tx6rwanrqM9kfCwqpNbhJ5jtrTf9FHqHNq7Lvv9uBoQ74SEaAu9FFceNBr6p3W1yhqPcxPPSSTv2ctufnQ
