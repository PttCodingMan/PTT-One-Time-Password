![PTTOTP: PTT One-Time Password in Python](https://i.imgur.com/zFxDCU7.png)
# 批踢踢動態密碼
## 此專案已經停止維護

###### 批踢踢動態密碼 (英語：PTT One-Time Password) 是一個專屬於批踢踢的動態密碼系統，您可以在您的電腦上執行此程式，並搭配手機的 Google Authenticator，批踢踢動態密碼就可以提供您的批踢踢帳號更好的安全性
###### 
###### 測試平台: Windows 10, Ubuntu 18.04
###### 原始碼
###### github: https://github.com/Truth0906/PTTOTP
###### Pypi: https://pypi.org/project/PTTOTP/

什麼是動態密碼
-------------------
###### 請參考 [動態密碼](https://zh.wikipedia.org/wiki/%E4%B8%80%E6%AC%A1%E6%80%A7%E5%AF%86%E7%A2%BC) Wiki

為什麼需要批踢踢動態密碼
-------------------
###### 如果您希望提升批踢踢帳號的安全性，防止有人嘗試不合法地存取您的批踢踢帳號，那麼批踢踢動態密碼就是您的首選。
###### 透過動態密碼不斷更換密碼的特性，確保您帳號的存取安全，有效降低您的帳號被盜用的風險。

如何使用
-------------------
###### 您需要一台連接網路的主機，作為批踢踢動態密碼主機
##### 安裝
###### 1. 下載批踢踢動態密碼 [下載](https://github.com/Truth0906/PTTOTP/releases) 與 Google Authenticator [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=zh_TW) or [iOS](https://itunes.apple.com/tw/app/google-authenticator/id388497605?mt=8)
###### 2. 執行 PTTOTP.exe 並輸入您的批踢踢帳號密碼
###### 3. 使用 Google Authenticator 掃描顯示在網頁上的 QR Code，以便將動態密碼金鑰匯進 Google Authenticator 中
###### 4. 保持 PTTOTP.exe 的運作
##### 登入
###### 1. 打開 Google Authenticator
###### 2. 複製 Google Authenticator 上所顯示的動態密碼當作批踢踢帳號的密碼登入
##### 解除
###### 1. 點選執行中的 PTTOTP.exe
###### 2. 按下 Ctrl + C 程式會自動將您的批踢踢帳號密碼恢復原樣

How it works
-------------------
###### 批踢踢動態密碼在保護您的批踢踢帳號期間，會根據標準演算法產生的動態密碼去定期地去修改批踢踢密碼，以達到動態密碼的效果。

重要
-------------------
###### 初始化批踢踢動態密碼後，會產生一個 OTPConfig.txt 檔案，內含所有批踢踢動態密碼相關重要資訊，會自動在程式資料夾還有系統使用者資料夾中備份，以保護您動態密碼金鑰的安全。
###### 一旦遺失所有備份或者硬碟毀損，作者也無法將您的帳號密碼恢復，請洽批踢踢帳號部，協助恢復您的帳號密碼。
###### 如果您的批踢踢動態密碼程式，不幸因為各種原因當機或者關閉，您可以直接重啟程式，批踢踢動態密碼會自動恢復您的動態密碼功能。
###### 批踢踢動態密碼，會顯示並儲存敏感資訊，請勿在公共電腦上執行批踢踢動態密碼。
###### 切勿同時執行兩個以上批踢踢動態密碼程式。

演算法
-------------------
###### 批踢踢動態密碼使用的演算法已經列在 [RFC6238](https://tools.ietf.org/html/rfc6238) 中

版本
-------------------
###### 0.1.3

需求
-------------------
###### Python 3.6

相依函式庫
-------------------
###### [PTTLibrary](https://github.com/Truth0906/PTTLibrary)
###### [pyotp](https://github.com/pyotp/pyotp)

贊助
-------------------
###### 如果這個專案對您很有幫助，您可以贊助我一杯咖啡 :D
###### XMR 贊助位址
###### 448CUe2q4Ecf9tx6rwanrqM9kfCwqpNbhJ5jtrTf9FHqHNq7Lvv9uBoQ74SEaAu9FFceNBr6p3W1yhqPcxPPSSTv2ctufnQ
