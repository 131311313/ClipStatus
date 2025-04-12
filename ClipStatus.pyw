import time
import psutil
import json
from pypresence import Presence

CLIENT_ID = "1359569869258883072"
RPC = Presence(CLIENT_ID)

def load_config():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("config.json が見つかりません。デフォルト設定を使用します。")
        return {
            "edition": "EX",
            "language": "jp",
            "large_image": "default_icon",
            "version": "4.0.0"
        }

def find_csp_process():
    """CSPプロセスを探して戻す（低負荷）"""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == "CLIPStudioPaint.exe":
            return proc
    return None

def extract_info_from_cmdline(cmdline, language):
    if cmdline:
        for arg in cmdline:
            if arg.endswith(".clip"):
                return arg.split("\\")[-1]
    return "無題" if language == "jp" else "Untitled"

def update_rpc(edition, filename, config):
    lang = config.get("language", "jp")
    state_text = f"{filename} を編集中🖌️🎨" if lang == "jp" else f"Editing {filename} 🖌️🎨"
    detail_text = f"EDITION : {edition}"
    large_text = f"Clip Studio Paint {edition} {config['version']}"
    
    print(f"{'ステータスを更新' if lang == 'jp' else 'Updated status'}: {filename}")

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
    edition = config.get("edition", "EX")
    lang = config.get("language", "jp")

    last_filename = None
    last_pid = None

    while True:
        proc = find_csp_process()

        if proc:
            try:
                cmdline = proc.cmdline()
                filename = extract_info_from_cmdline(cmdline, lang)

                if filename != last_filename:
                    print(f"{'CSP 起動中' if lang == 'jp' else 'CSP running'}: {filename}")
                    update_rpc(edition, filename, config)
                    last_filename = filename
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                print("CSPにアクセスできませんでした。")
                RPC.clear()
                last_filename = None
        else:
            print("CSPが起動していない → ステータスクリア" if lang == "jp" else "CSP is not running → clearing status.")
            RPC.clear()
            last_filename = None

        time.sleep(10)

if __name__ == "__main__":
    main()
