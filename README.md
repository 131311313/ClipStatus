# Overview
<img width="266" height="139" alt="image" src="https://github.com/user-attachments/assets/e61a0299-30b0-42ef-bc63-429514b0dc27" />
<img width="187" height="185" alt="image" src="https://github.com/user-attachments/assets/f5e634ab-fecc-4cc8-ba63-72d5f7aaf5bd" />

This program aims to implement Discord Rich Presence for Clip Studio Paint 
using a lightweight Python script.

💡 This code was generated 99% by ChatGPT, and I did almost no effort.  
I am not a programmer.  
The default installation path is as follows:  
`appdata/roaming/clipstatus`

---

## Features

- Switch between Japanese / English
- Switch between editions (Debut / Pro / EX)
- Switch between versions
- Switch between multiple icons
- Currently not working - Reload functionality (restart without task kill)
- Hide the window from the tray (this needs to be enabled from `config.json`)

🔧 All features, except the "Hide from tray" functionality, can be controlled from the tray menu.

---

## Known Issues

- When opening a `.clip` file directly from Explorer, the file name may not be correctly retrieved.
- Startup may not work in some cases.
- It works correctly when running as a Python script, but when built into an `.exe`, reload does not work, and it stays in the task manager.
- It may not work properly unless excluded from antivirus software.
- Changes made through the tray menu may not be reflected.

    This is due to insufficient permissions.  
    If an error occurs when trying to save `config.json` with Notepad, this issue is relevant.  
    You can fix it by following these steps:

    1. Right-click the `clipstatus` folder > Properties > Security > Edit  
    2. Grant "Full Control" to your user and apply  
    3. If this still doesn't resolve the issue, add it to your antivirus whitelist and repeat the same steps for each file.




# 概要

このプログラムは、Clip Studio Paint の Discord Rich Presence を
軽量な Python スクリプトで実装することを目的としています。

💡 このコードは 99% ChatGPT によって生成されており、私はほとんど努力していません。  
私はプログラマーではありません。  
デフォルトのインストールパスは以下の通りです：  
`appdata/roaming/clipstatus`

---

## 機能一覧

- 日本語 / 英語 の切り替え
- エディションの切り替え（Debut / Pro / EX）
- バージョンの切り替え
- アイコンの切り替え（複数種類）
- 現在動作しません - リロード機能（タスクキルなしで再起動）
- トレイからウィンドウを隠す（※config.jsonから有効化が必要）

🔧「トレイから隠す」機能以外は、すべてトレイメニューから操作可能です。

---

## 既知の不具合

- `.clip` ファイルをエクスプローラーから直接開くと、ファイル名が正しく取得されません。
- スタートアップが動作しない場合があります。
- Python で動作している場合はリロードが正しく動作しますが、.exe にビルドした場合、リロードが動作せず、タスクマネージャーに常駐することがあります。
- ウイルス対策ソフトで除外しないと、正しく動作しない場合があります。
- トレイから設定しても反映されない場合があります。

    これは権限が不足していることが原因です。  
    `config.json` をメモ帳で上書き保存しようとした際にエラーが発生する場合、この不具合に該当します。  
    以下の手順で修正できます：

    1. `clipstatus` フォルダを右クリック > プロパティ > セキュリティ > 編集  
    2. 自分のユーザーに「フルコントロール」を与えて適用  
    3. それでも解決しない場合は、ウイルス対策ソフトのホワイトリストに追加し、各ファイルに対して同様の手順を繰り返してください。


