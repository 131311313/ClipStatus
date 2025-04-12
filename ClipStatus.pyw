import time
import psutil
import json
from pypresence import Presence

CLIENT_ID = "1359569869258883072"  # 提供されたDiscord Client ID
RPC = Presence(CLIENT_ID)

# 設定ファイルを読み込む
def load_config():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print("config.json が見つかりません。デフォルト設定を使用します。")
        return {
            "edition": "EX",  # デフォルトエディション
            "language": "jp",  # デフォルトは日本語
            "large_image": "default_icon",  # デフォルトアイコン
            "version": "4.0.0"  # デフォルトバージョン
        }

# ファイル名をコマンドライン引数から取得
def get_csp_process_info():
    """CSPのプロセスからコマンドライン引数を取得"""
    for process in psutil.process_iter(attrs=['name', 'cmdline']):
        if process.info['name'] == "CLIPStudioPaint.exe" and len(process.info['cmdline']) > 1:
            return process.info['cmdline']
    return None

def extract_info_from_cmdline(cmdline):
    """コマンドライン引数からファイルパスを抽出"""
    if cmdline:
        for arg in cmdline:
            if arg.endswith(".clip"):  # .clipファイルを探す
                filename = arg.split("\\")[-1]  # ファイル名を抽出
                return filename
    return "無題"

def get_csp_edition(config):
    """設定ファイルからエディションを取得"""
    return config.get("edition", "EX")  # 設定ファイルからエディションを取得

def is_csp_running():
    """CSPが起動しているかチェック"""
    for process in psutil.process_iter(attrs=['name']):
        if process.info['name'] == "CLIPStudioPaint.exe":
            return True
    return False

def update_rpc(edition, filename, config):
    """Discord Rich Presenceの更新"""
    state_text = f"{filename} を編集中🖌️🎨" if config["language"] == "jp" else f"{filename} Drawing🖌️🎨"  # ファイル名と編集中状態

    # Discord Rich Presence を更新
    RPC.update(
        state=state_text,  # stateに「無題」を編集中として設定
        details=f"EDITION : {edition}",  # detailsにエディションを設定
        large_image=config["large_image"],  # アイコン設定
        large_text=f"Clip Studio Paint {edition} {config['version']}"  # 詳細表示部分：エディションとバージョン
    )
    print(f"ステータスを更新: {filename} 編集中")

def main():
    print("Discord Rich Presence 接続中...")
    RPC.connect()
    print("Discord Rich Presence Connected!")
    
    # 設定ファイルを読み込む
    config = load_config()
    edition = get_csp_edition(config)  # 設定に基づいてエディションを取得

    last_filename = None  # 前回のファイル名を保持

    while True:
        if is_csp_running():
            cmdline = get_csp_process_info()
            if cmdline:
                filename = extract_info_from_cmdline(cmdline)
                
                # ファイル名が変更された場合のみ処理を更新
                if filename != last_filename:
                    print(f"CSP {edition} 起動中: {filename}")

                    # Discord Rich Presence を更新
                    update_rpc(edition, filename, config)
                    last_filename = filename  # 新しいファイル名を記録
            else:
                print("CSPのコマンドライン引数が取得できませんでした。")
                RPC.clear()
                last_filename = None  # CSPが終了した場合、前回のファイル名をリセット
        else:
            print("CSPが起動していない → ステータスクリア")
            RPC.clear()
            last_filename = None  # CSPが終了した場合、前回のファイル名をリセット

        time.sleep(10)  # 10秒ごとに更新

if __name__ == "__main__":
    main()
