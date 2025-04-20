# ClipStatus - Clip Studio Paint Discord Rich Presence

![image](https://github.com/user-attachments/assets/f2c84299-be10-4a4e-9683-308e7b0d6205) ![image](https://github.com/user-attachments/assets/f383561c-3028-464f-9579-3933ce80289a)

## 🌐 Language / 言語

[🇯🇵 日本語版はこちら](#-日本語) / [🇺🇸 English version here](#-english)

---

## 🇺🇸 English

### Overview
This program is a lightweight Python script that implements **Discord Rich Presence** for **Clip Studio Paint**.

> 💡 This code is 99% written by ChatGPT. I did not put much effort into it.  
> I'm not a programmer.  
> The default installation path is:  
> `C:\Program Files (x86)\ClipStatus`

> 🧠 This project was created with ChatGPT, inspired by the following projects:  
> https://github.com/kawaiiepic/csprp  
> https://github.com/Pepijn98/CSP-Discord/

### Features
- Language switching: Japanese / English  
- Edition switching: Debut / Pro / EX  
- Version switching  
- Icon switching (multiple available)  
- Currently not working - Reload function (restart without task kill)
- Hide from system tray (must be enabled via `config.json`)  

> 🔧 All features except “Hide from tray” are configurable directly via the tray menu.

### Known Issues
- When opening `.clip` files directly from File Explorer, the filename may not be detected correctly.
- It works correctly in py, but when built to .exe, reload does not work and resides in task manager
- Start-up does not work → Use this .bat
  https://github.com/131311313/ClipStatus/releases/download/release4/clipstatusfix.bat
- Settings from tray menu might not be applied properly.

This is due to lack of permissions. If you're getting errors trying to overwrite `config.json` with Notepad, this is likely the cause.  
To fix this:
1. Go to `C:\Program Files (x86)\ClipStatus`
2. Right-click the folder > Properties > Security > Edit
3. Grant your user **Full Control** and apply.
4. If the problem persists, add the app to your antivirus whitelist, and repeat the steps for each file individually.

5. Use 1.0.5, it will be installed in appdata/roaming.
Be sure to uninstall the old version

---

### Regarding Issues
I’ll try to respond as much as possible, but please check the **Known Issues** section before submitting anything.

---

## 🇯🇵 日本語

### 概要
このプログラムは、**Clip Studio Paint** の Discord Rich Presence を  
軽量な Python スクリプトで実装することを目的としています。

> 💡 このコードは 99% ChatGPT によって生成されており、私はほとんど努力していません。  
> 私はプログラマーではありません。  
> デフォルトのインストールパスは：  
> `C:\Program Files (x86)\ClipStatus`

> 🧠 以下のプロジェクトから着想を得て、ChatGPTで作成しています：  
> https://github.com/kawaiiepic/csprp  
> https://github.com/Pepijn98/CSP-Discord/

### 機能一覧
- 日本語 / 英語 の切り替え  
- エディションの切り替え（Debut / Pro / EX）  
- バージョンの切り替え  
- アイコンの切り替え（複数種類）  
- 現在動作しません - リロード機能（タスクキルなしで再起動）   
- トレイからウィンドウを隠す（※`config.json`から有効化が必要）  

> 🔧「トレイから隠す」機能以外は、すべてトレイメニューから操作可能です。

### 既知の不具合
- `.clip` ファイルをエクスプローラーから直接開くと、ファイル名が正しく取得されません。
- スタートアップが動作しない →　こちらの.batを使用してください
  https://github.com/131311313/ClipStatus/releases/download/release4/clipstatusfix.bat
  
- pyでは正しく動作しますが.exeにビルドするとreloadが動作せず、タスクマネージャーに常駐します
- ウイルス対策ソフトで除外しないと正しく動作しない場合がある

- トレイから設定しても反映されない場合があります。

これは権限が不足していることが原因です。  
`config.json` をメモ帳で上書き保存しようとしてエラーが出たら、この不具合に該当します。  
以下の手順で修正できます：

1. `C:\Program Files (x86)\ClipStatus` を開く  
2. フォルダを右クリック > プロパティ > セキュリティ > 編集  
3. 自分のユーザーに「フルコントロール」を与えて適用  
4. それでも直らない場合は、ウイルス対策ソフトのホワイトリストに追加し、  
   各ファイルに対して同様の手順を繰り返してください。

1.0.5を使用してください。appdata/roamingにインストールされます。
古いバージョンは必ずアンインストールしてください！
---

### ISSUEについて
可能な限り対応しますが、**まず既知の不具合をご確認ください。**

---

## 🛠️ Build Guide / ビルド手順

### 🇺🇸 English

To build ClipStatus as a standalone executable:

1. Download this repository as a folder from GitHub.  
2. Install [Nuitka](https://nuitka.net/) using pip:

    ```bash
    pip install nuitka
    ```

3. Then run the following command in the project directory:

    ```bash
    nuitka --standalone --onefile --windows-disable-console --windows-icon-from-ico="dark_icon.ico" clipstatus.pyw
    ```

This will create a single `.exe` file you can distribute or run directly.

---

### 🇯🇵 日本語

ClipStatus をスタンドアロンの実行ファイルとしてビルドするには：

1. GitHubからこのリポジトリをフォルダとしてダウンロードしてください。  
2. [Nuitka](https://nuitka.net/) を pip でインストールします：

    ```bash
    pip install nuitka
    ```

3. プロジェクトのディレクトリで以下のコマンドを実行してください：

    ```bash
    nuitka --standalone --onefile --windows-disable-console --windows-icon-from-ico="dark_icon.ico" clipstatus.pyw
    ```

これで、配布可能な単一の `.exe` ファイルが生成されます。

    ```bash
    nuitka --standalone --onefile --windows-disable-console --windows-icon-from-ico="dark_icon.ico" clipstatus.pyw
    ```

これで、配布可能な単一の `.exe` ファイルが生成されます。
