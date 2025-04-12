# ClipStatus - Clip Studio Paint Discord Rich Presence

![image](https://github.com/user-attachments/assets/f2c84299-be10-4a4e-9683-308e7b0d6205)

## 🇺🇸 English

### Overview
This program is a lightweight Python script that implements **Discord Rich Presence** for **Clip Studio Paint**.

> 💡 This code is 99% written by ChatGPT. I did not put much effort into it.  
> I'm not a programmer.  
> The default installation path is `C:\Program Files (x86)\ClipStatus`

### Features
- Language switching: Japanese / English  
- Edition switching: Debut / Pro / EX  
- Version switching  
- Icon switching (multiple available)  
- Reload function (restart without task-killing)  
- Hide from system tray (must be enabled via `config.json`)  

> 🔧 All features except “Hide from tray” are configurable directly via the tray menu.

### Known Issues
- When opening `.clip` files directly from File Explorer, the filename may not be detected correctly. 

-  Problem with configurations not being reflected from the tray.

This is due to lack of permissions; if you try to overwrite the config.json with Notepad and get an error, this is the problem.
C:\Program Files (x86)\ClipStatus
Right click on this folder, open properties, click security, edit
Give your user full control and apply it. If that does not work, whitelist it with your antivirus software and then follow the previous steps for each file individually.

---

### Regarding Issues
I will try to respond as much as possible, but please check **known issues** first before submitting.

---

## 🇯🇵 日本語

### 概要
このプログラムは、**Clip Studio Paint** の Discord Rich Presence を軽量な Python スクリプトで実装することを目的としています。

> 💡 このコードは 99% ChatGPT によって生成されており、私はほとんど努力していません。  
> 私はプログラマーではありません。  
> デフォルトのインストールパスは `C:\Program Files (x86)\ClipStatus` です。

### 機能一覧
- 日本語 / 英語 の切り替え  
- エディションの切り替え（Debut / Pro / EX）  
- プロジェクトファイル名取得  
- バージョンの切り替え  
- アイコンの切り替え（複数種類があります）  
- リロード機能（タスクキルなしで再起動）  
- トレイからウィンドウを隠す（※config.jsonから有効にする必要あり）  

> 🔧「トレイから隠す」機能以外は、すべてトレイメニューから操作可能です。

### 既知の不具合
- `.clip` ファイルをエクスプローラーから直接開くと、ファイル名が正しく取得されません。

- トレイから設定しても反映されない問題

これは権限が足りないためです。config.jsonをメモ帳で上書き保存しようとしてみてエラーが出たらこの不具合に当てはまります。
C:\Program Files (x86)\ClipStatus
このフォルダを右クリック、プロパティを開いてセキュリティ、編集をクリック
自分のユーザーにフルコントロールを与えて適用してください、それでもうまくいかない場合ウイルス対策ソフトのホワイトリストに登録した後、ファイル個別に先ほどの手順を行ってください

---

### ISSUEについて
可能な限り対応しますが、**既知の不具合を確認してから**ご報告いただけると助かります。

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



