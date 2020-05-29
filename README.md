![PTTOTP: PTT One-Time Password in Python](https://i.imgur.com/zFxDCU7.png)
# 批踢踢動態密碼

###### 批踢踢動態密碼 (英語：PTT One-Time Password) 是一個專屬於批踢踢的動態密碼系統，您需要在您的電腦上執行此程式，並搭配手機的 Google Authenticator，批踢踢動態密碼就可以提供您的批踢踢帳號更好的安全性
###### 
###### 測試平台: Windows 10

什麼是動態密碼
-------------------
###### 請參考 [動態密碼](https://zh.wikipedia.org/wiki/%E4%B8%80%E6%AC%A1%E6%80%A7%E5%AF%86%E7%A2%BC) Wiki

為什麼需要批踢踢動態密碼
-------------------
###### 批踢踢因為系統的限制，密碼欄位最長只有八碼，以現在的角度來看可以提供的安全性其實很低
###### 如果您希望提升批踢踢帳號的安全性，防止有人嘗試不合法地存取您的批踢踢帳號，那麼批踢踢動態密碼就是您的首選。
###### 透過動態密碼每三十秒更換密碼的特性，確保您帳號的存取安全，可以有效降低您的帳號被盜用的風險。

如何使用
-------------------
###### 您需要一台連接網路的電腦，作為批踢踢動態密碼主機
###### 使用前，建議您熟悉信箱重設帳密操作流程，以免有意外導致無法恢復
##### 安裝與註冊
###### 1. 下載批踢踢動態密碼 [下載](https://github.com/PttCodingMan/PTT-One-Time-Password/releases) 與 Google Authenticator [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=zh_TW) or [iOS](https://itunes.apple.com/tw/app/google-authenticator/id388497605?mt=8)
###### 2. 執行 PttOneTimePassword.exe 並輸入您的批踢踢帳號密碼
###### 3. 閱讀守則之後，同意點願意遵守
###### 4. 使用 Google Authenticator 掃描 QR Code，以便將動態密碼金鑰匯進 Google Authenticator 中
###### 5. 您看到的六位數數字就是您目前的批踢踢密碼，點選兩下就會自動複製到您的剪貼簿中
###### 6. 保持 PttOneTimePassword.exe 的運作
##### 登入批踢踢
###### 1. 打開 Google Authenticator
###### 2. 複製 Google Authenticator 上所顯示的動態密碼當作批踢踢帳號的密碼登入
##### 解除
###### 1. 點選系統列批踢踢動態密碼圖示，點選離開就可以暫時解決批踢踢動態密碼的保護

回報問題
-------------------
#### 開個 [issue](https://github.com/PttCodingMan/PTT-One-Time-Password/issues/new) 追蹤問題也可以直接問我 [![chatroom icon](https://patrolavia.github.io/telegram-badge/chat.png)](https://t.me/PyPtt)

重要
-------------------
###### 1. 註冊批踢踢動態密碼後，會產生帳號專屬檔案在 data 資料夾，內含所有批踢踢動態密碼相關重要資訊，建議備份此資料夾，以保護您動態密碼金鑰的安全。
###### 一旦遺失所有備份或者硬碟毀損，作者也無法將您的帳號密碼恢復，請使用信箱重設密碼功能，以恢復您的帳號密碼。
###### 2. 如果您的批踢踢動態密碼程式，不幸因為各種原因當機或者關閉，您可以直接重啟程式，批踢踢動態密碼會自動恢復您的動態密碼功能。
###### 3. 批踢踢動態密碼，會顯示並儲存敏感資訊，請勿在公共電腦上執行批踢踢動態密碼。
###### 4. 切勿同時執行兩個以上批踢踢動態密碼程式。

演算法
-------------------
###### 批踢踢動態密碼使用的演算法已經列在 [RFC6238](https://tools.ietf.org/html/rfc6238) 中

版本
-------------------
###### 0.2.0

需求
-------------------
###### Python 3.6

相依函式庫
-------------------
###### [PyPtt](https://github.com/PttCodingMan/PyPtt)
###### [pyotp](https://github.com/pyotp/pyotp)
###### [PyQt5](https://www.riverbankcomputing.com/software/pyqt/)
###### [python-qrcode](https://github.com/lincolnloop/python-qrcode)


贊助
-------------------
###### 如果這個專案對您很有幫助，您可以贊助我一杯咖啡 :D
###### XMR 贊助位址
###### 448CUe2q4Ecf9tx6rwanrqM9kfCwqpNbhJ5jtrTf9FHqHNq7Lvv9uBoQ74SEaAu9FFceNBr6p3W1yhqPcxPPSSTv2ctufnQ
