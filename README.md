![PTTOTP: A PTT One-Time Password Bot in Python](https://i.imgur.com/zFxDCU7.png)
# PTT One-Time Password

###### PTT One-Time Password 是一個由 Python 實現的 PTT 動態登入密碼，你可以在你的電腦上執行此程式，就可以享受 PTT One-Time Password 給予的安全性
###### 
###### 測試平台: Windows 10, Ubuntu 18.04
###### 原始碼
###### github: https://github.com/Truth0906/PTTOTP
###### Pypi: https://pypi.org/project/PTTOTP/

什麼是 One-Time Password
-------------------
###### 以下節錄自 [一次性密碼](https://zh.wikipedia.org/wiki/%E4%B8%80%E6%AC%A1%E6%80%A7%E5%AF%86%E7%A2%BC) Wiki
###### 一次性密碼（英語：One Time Password，簡稱OTP），又稱動態密碼或單次有效密碼，是指電腦系統或其他數位裝置上只能使用一次的密碼，有效期為只有一次登錄會話或交易。

為什麼需要 One-Time Password
-------------------
###### 如果您希望提升帳號的安全性，防止有人嘗試不合法地存取您的 PTT帳號，那麼 PTT One-Time Password 就是您的首選。
###### 透過 One-Time Password 不斷更換密碼的特性，確保您帳號的存取安全，有效降低帳號/密碼被盜用的風險。

如何使用
-------------------
##### 安裝
###### 1. 下載 PTT One-Time Password [下載](https://github.com/Truth0906/PTTOTP/releases) 與 Google Authenticator [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=zh_TW) or [iOS](https://itunes.apple.com/tw/app/google-authenticator/id388497605?mt=8)
###### 2. 執行 PTT One-Time Password 並輸入您的 PTT 帳號密碼
###### 3. 使用 Google Authenticator 掃描顯示在網頁上的 QRCode，以將 One-Time Password 金鑰匯進 Google Authenticator 中
###### 4. 保持 PTT One-Time Password 的運作
##### 登入
###### 1. 打開 Google Authenticator
###### 2. 複製 Google Authenticator 上所顯示的 One-Time Password 當作 PTT 帳號的密碼登入
##### 解除
###### 1. 點選執行中的 PTT One-Time Password
###### 2. 按下 Ctrl + C 程式會自動將您的 PTT 帳號密碼恢復原樣

How it works
-------------------
###### 您需要一台連接網路的主機，作為 PTT One-Time Password 主機。
###### PTT One-Time Password 在保護您的 PTT 帳號期間，會根據演算法產生的 One-Time Password 去定期地去修改 PTT 帳號密碼，以達到動態密碼的效果。

重要
-------------------
###### 初始化 PTT One-Time Password 後，會產生 OTPConfig.txt 檔案內含所有 PTT One-Time Password 相關重要資訊，會自動在程式資料夾還有系統使用者資料夾中備份，以保護您 One-Time Password 金鑰的安全。
###### 一旦遺失所有備份或者硬碟毀損，作者也無法將您的帳號密碼恢復，請洽 PTT 帳號部，協助恢復您的帳號密碼。
###### 如果您的 PTT One-Time Password，不幸因為各種原因當機或者關閉，您可以直接重新重啟程式，PTT One-Time Password 會自動恢復您的 One-Time Password 功能。
###### PTT One-Time Password，會顯示並儲存敏感資訊，請勿在公共電腦上執行 PTT One-Time Password。

演算法
-------------------
###### PTT One-Time Password 使用的演算法已經列在 [RFC6238](https://tools.ietf.org/html/rfc6238) 中

版本
-------------------
###### 0.0.3

安裝
-------------------
###### [下載](https://github.com/Truth0906/PTTOTP/releases)

需求
-------------------
###### Python 3.6

相依函式庫
-------------------
###### [PTTLibrary](https://github.com/Truth0906/PTTLibrary)
###### [pyotp](https://github.com/pyotp/pyotp)

未來工作
-------------------

贊助
-------------------
###### 如果這個專案對你很有幫助，你可以贊助我一杯咖啡 :D
###### XMR 贊助位址
###### 448CUe2q4Ecf9tx6rwanrqM9kfCwqpNbhJ5jtrTf9FHqHNq7Lvv9uBoQ74SEaAu9FFceNBr6p3W1yhqPcxPPSSTv2ctufnQ
