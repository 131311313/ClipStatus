import time
import psutil
import json
from pypresence import Presence

CLIENT_ID = "1359569869258883072"
RPC = Presence(CLIENT_ID)

def load_config():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print("config.json が見つかりません。デフォルト設定を使用します。")
        return {
            "edition": "EX",
            "language": "jp",
            "large_image": "default_icon",
            "version": "4.0.0"
        }

def get_csp_process_info():
    for process in psutil.process_iter(attrs=['name', 'cmdline']):
        if process.info['name'] == "CLIPStudioPaint.exe" and len(process.info['cmdline']) > 1:
            return process.info['cmdline']
    return None

def extract_info_from_cmdline(cmdline, language):
    if cmdline:
        for arg in cmdline:
            if arg.endswith(".clip"):
                filename = arg.split("\\")[-1]
                return filename
    return "無題" if language == "jp" else "Untitled"

def get_csp_edition(config):
    return config.get("edition", "EX")

def is_csp_running():
    for process in psutil.process_iter(attrs=['name']):
        if process.info['name'] == "CLIPStudioPaint.exe":
            return True
    return False

def update_rpc(edition, filename, config):
    lang = config.get("language", "jp")
    
    if lang == "jp":
        state_text = f"{filename} を編集中🖌️🎨"
        detail_text = f"EDITION : {edition}"
        large_text = f"Clip Studio Paint {edition} {config['version']}"
        print(f"ステータスを更新: {filename} 編集中")
    else:
        state_text = f"Editing {filename} 🖌️🎨"
        detail_text = f"EDITION : {edition}"
        large_text = f"Clip Studio Paint {edition} {config['version']}"
        print(f"Updated status: Editing {filename}")

    RPC.update(
        state=state_text,
        details=detail_text,
        large_image=config["large_image"],
        large_text=large_text
    )

def main():
    print("Connecting to Discord Rich Presence...")
    RPC.connect()
    print("Discord Rich Presence Connected!")

    config = load_config()
    edition = get_csp_edition(config)
    lang = config.get("language", "jp")

    last_filename = None

    while True:
        if is_csp_running():
            cmdline = get_csp_process_info()
            if cmdline:
                filename = extract_info_from_cmdline(cmdline, lang)
                if filename != last_filename:
                    msg = f"CSP {edition} 起動中: {filename}" if lang == "jp" else f"CSP {edition} running: {filename}"
                    print(msg)
                    update_rpc(edition, filename, config)
                    last_filename = filename
            else:
                print("CSPのコマンドライン引数が取得できませんでした。" if lang == "jp" else "Couldn't get command line arguments from CSP.")
                RPC.clear()
                last_filename = None
        else:
            print("CSPが起動していない → ステータスクリア" if lang == "jp" else "CSP is not running → clearing status.")
            RPC.clear()
            last_filename = None

        time.sleep(10)

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
