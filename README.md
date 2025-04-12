# 🛠️ Clip Studio Paint ディスコードリッチプレゼンス

> **これは 99% ChatGPT によって作成された Python スクリプトです。**  
> 私はほぼ努力をしていません。ただこの機能が欲しかったのでChatGPTを使い作成しました。

🔗 [OpenAI 利用規約](https://openai.com/policies/terms-of-use)

---

## 📦 セットアップ手順

1. **最新の Python** をインストールしてください。  
   ↪ [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. ダウンロードした ZIP ファイルを解凍し、  
   `config.json` を以下のように編集してください：

   - Clip Studio Paint の **バージョン**
   - **エディション**（EX / PRO / DEBUT）
   - **言語**
   - お好みの **ロゴアイコン** (default_icon or dark_icon)



3. `setup.bat` を実行します：
   ```
   setup.bat
   ```

4. PC を再起動するとスタートアップから起動されます。  
   起動したくない場合は、手動で以下のバッチを実行してください：
   ```
   C:\Program Files (x86)\clipstatus\startup.bat
   ```

---

## ❓ よくある質問（FAQ）

### Q. アイコンを切り替える方法は？

**A.** `config.json` 内でdefault_iconとdark_iconお好きなほうを設定してください：


---

### Q. EX / PRO / DEBUT のステータスやバージョンを切り替えるには？

**A.**  
Python ではバージョンやエディションを直接取得できません。  
そのため、以下のように `config.json` を **手動で編集** してください：

```json
"version": "2.2.0",
"edition": "PRO"
```

---




# 🛠️ Clip Studio Paint Discord rich presence script


> **This is a Python script created with 99% help from ChatGPT.**  
> I barely did anything myself—I just wanted this feature, so I used ChatGPT to make it.

🔗 [OpenAI Terms of Use](https://openai.com/policies/terms-of-use)

---

## 📦 Setup Instructions

1. **Install the latest version of Python**  
   ↪ [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Extract the downloaded ZIP file, and edit the `config.json` file with the following:

   - Your Clip Studio Paint **version**
   - **Edition** (EX / PRO / DEBUT)
   - **Language**
   - Your preferred **logo icon**  (default_icon or dark_icon)

3. Run the setup script:
   ```
   setup.bat
   ```

4. After restarting your PC, the program will auto-run on startup.  
   If you prefer not to start it automatically, you can run this manually:
   ```
   C:\Program Files (x86)\clipstatus\startup.bat
   ```

---

## ❓ Frequently Asked Questions (FAQ)

### Q. How do I switch icons?

**A.**  
Edit `config.json` and choose between `default_icon` and `dark_icon` as you like.

---

### Q. How do I switch the version or edition (EX / PRO / DEBUT)?

**A.**  
Since Python can’t directly detect your version or edition,  
you’ll need to manually edit the `config.json` like this:

```json
"version": "2.2.0",
"edition": "PRO"
```

---






