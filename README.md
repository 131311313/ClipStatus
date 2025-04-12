# 🛠️ Clip Studio Paint ステータス切り替えスクリプト

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
   - お好みの **ロゴアイコン**



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

