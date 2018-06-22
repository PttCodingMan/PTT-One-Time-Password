![PTTOTP: A PTT One-Time Password Bot in Python](https://i.imgur.com/zFxDCU7.png)
# PTT One-Time Password

###### PTT One-Time Password 是一個由 Python 實現的 PTT 動態登入密碼，你可以在任何支援 python 的電腦執行此程式，就可以享受 PTT One-Time Password 給予的安全性
###### 
###### 測試平台: Windows 10, Ubuntu 18.04
###### 原始碼
###### github: https://github.com/Truth0906/PTTOTP
###### Pypi: https://pypi.org/project/PTTOTP/

什麼是 One-Time Password
-------------------
###### 以下節錄自 "一次性密碼" Wiki
###### 一次性密碼（英語：One Time Password，簡稱OTP），又稱動態密碼或單次有效密碼，是指電腦系統或其他數位裝置上只能使用一次的密碼，有效期為只有一次登錄會話或交易。OTP 避免了一些與傳統基於（靜態）密碼認證相關聯的缺點；一些實作還納入了雙因素認證，確保單次有效密碼需要存取一個人有的某件事物（如內建 OTP 電腦的小鑰匙掛件裝置）以及一個人知道的某件事物（如 PIN）。

為什麼我需要 One-Time Password
-------------------
###### 簡單來說，如果您希望可以提升帳號的安全性，防止有人嘗試不合法地存取您的 PTT帳號，那麼 PTT One-Time Password 就是你的首選。
###### 透過 One-Time Password 不斷更換的特性，確保帳號存取安全，有效解決帳號/ 密碼被盜用的風險。

How it works
-------------------
###### 您需要一台連接網路的主機，作為 PTT One-Time Password 主機，需要 PTT One-Time Password 保護您的帳號時，需要
###### 保持開啟狀態。
###### PTT One-Time Password 在保護您的 PTT 帳號期間，會根據演算法產生的 One-Time Password 去定期地去修改 PTT 帳號
###### 的密碼，以達到動態密碼的效果。

重要
-------------------
###### 初始化程式後，會在程式資料夾產生一個 OTPConfig.txt 內含所有 PTT One-Time Password 相關重要資訊，請妥當保管備份。
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
