# ClipStatus - Clip Studio Paint Discord Rich Presence


![image](https://github.com/user-attachments/assets/f2c84299-be10-4a4e-9683-308e7b0d6205)


---

## 🇯🇵 日本語

### 概要
このプログラムは、**Clip Studio Paint** の Discord Rich Presence を軽量な Python スクリプトで実装することを目的としています。

> 💡 このコードは 99% ChatGPT によって生成されており、私はほとんど努力していません。  
> 私はプログラマーではありません。

### 機能一覧
- 日本語 / 英語 の切り替え
- エディションの切り替え（Debut / Pro / EX）
- バージョンの切り替え
- アイコンの切り替え（複数種類があります）
- リロード機能（タスクキルなしで再起動）
- トレイからウィンドウを隠す（※config.jsonから有効にする必要あり）

> 🔧「トレイから隠す」機能以外は、すべてトレイメニューから操作可能です。

### 既知の不具合
- `.clip` ファイルをエクスプローラーから直接開くと、ファイル名が正しく取得されません。
- 正しくトレイから設定を変更できない問題が起きる可能性があります → 1.0.3で修正しました。 1.0.2は使用しないでください

### ISSUEについて
可能な限り対応しますが、**既知の不具合を確認してから**ご報告いただけると助かります。

---

## 🇺🇸 English

### Overview
This program is a lightweight Python script that implements **Discord Rich Presence** for **Clip Studio Paint**.

> 💡 This code is 99% written by ChatGPT. I did not put much effort into it.  
> I'm not a programmer.

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

### Regarding Issues
I will try to respond as much as possible, but please check **known issues** first before submitting.

---

