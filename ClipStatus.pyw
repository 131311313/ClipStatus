import time
import psutil
import json
from pypresence import Presence
import pystray
from PIL import Image
import threading
import sys
import os


COMMON_VERSIONS = [
    "4.0.0", "3.2.2", "3.2.0", "3.1.4", "3.1.2", "3.1.0",
    "3.0.8", "3.0.2", "3.0.0", "2.3.4", "2.3.2", "2.3.0",
    "2.2.0", "2.1.3", "2.1.0", "2.0.1", "2.0.0"
]

VERSIONS = {
    "EX": COMMON_VERSIONS,
    "PRO": COMMON_VERSIONS,
    "DEBUT": COMMON_VERSIONS
}

CLIENT_ID = "1357259618220249199"
RPC = Presence(CLIENT_ID)

def get_config_path():
    """Get the appropriate config file path based on execution context"""
    if getattr(sys, 'frozen', False):

        return os.path.join(os.path.dirname(sys.executable), "config.json")
    else:
        
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")

def load_config():
    config_path = get_config_path()
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("config.json が見つかりません。デフォルト設定を使用します。")
        default_config = {
            "edition": "EX",
            "language": "jp",
            "large_image": "default_icon",
            "version": "4.0.0"
        }
        
        save_config(default_config)
        return default_config

def save_config(config):
    config_path = get_config_path()
    try:
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
        print(f"設定を保存しました: {config_path}")
    except PermissionError:
        print(f"設定ファイルの書き込み権限がありません: {config_path}")
    except Exception as e:
        print(f"設定保存エラー: {e}")

def find_csp_process():
    """CSPプロセスを探して戻す（低負荷）"""
    try:
        return next(proc for proc in psutil.process_iter(['name']) 
                   if proc.info['name'] == "CLIPStudioPaint.exe")
    except StopIteration:
        return None

def extract_info_from_cmdline(cmdline, language):
    if cmdline:
        for arg in cmdline:
            if arg.endswith(".clip"):
                return arg.split("\\")[-1]
    return "無題" if language == "jp" else "Untitled"

def update_rpc(edition, filename, config):
    lang = config.get("language", "jp")
    state_text = f"{filename} {'を編集中🖌️🎨' if lang == 'jp' else 'Editing 🖌️🎨'}"
    detail_text = f"EDITION : {edition}"
    large_text = f"Clip Studio Paint {edition} {config['version']}"
    
    print(f"{'ステータスを更新' if lang == 'jp' else 'Updated status'}: {filename}")

    RPC.update(
        state=state_text,
        details=detail_text,
        large_image=config["large_image"],
        large_text=large_text
    )

def restart_application():
    """アプリケーションを再起動する"""
    print("アプリケーションを再起動中...")
    try:
        RPC.close()  
    except:
        pass
    
    
    if getattr(sys, 'frozen', False):
        
        executable = sys.executable
    else:
        
        executable = sys.executable
        sys.argv.insert(0, __file__)
    
    
    import subprocess
    subprocess.Popen([executable] + sys.argv[1:], 
                    cwd=os.path.dirname(os.path.abspath(__file__)))
    cleanup()  

def cleanup():
    """アプリケーションのクリーンアップを行う"""
    print("クリーンアップを実行中...")
    try:
        RPC.close()
    except:
        pass

   
    if 'tray_icon' in globals() and tray_icon is not None:
        try:
            tray_icon.stop()
        except:
            pass

   
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)

def create_tray_icon(config, update_config_callback):
    def on_reload(icon, item):
        print("Reloading with current config...")
        icon.stop()  
        RPC.close()  
        restart_application()  

    def on_exit(icon, item):
        print("Closing Discord Rich Presence...")
        icon.stop()
        cleanup()

    def change_language(icon, item):
        config["language"] = "jp" if item.text == "日本語" else "en"
        save_config(config)
        update_config_callback(config)

    def change_edition(icon, item):
        config["edition"] = item.text
        if "version" not in config or config["version"] not in VERSIONS[item.text]:
            config["version"] = VERSIONS[item.text][0]  
        save_config(config)
        update_config_callback(config)

    def change_version(icon, item):
        config["version"] = item.text
        save_config(config)
        update_config_callback(config)

    def change_icon_theme(icon, item):
        config["large_image"] = item.text
        save_config(config)
        update_config_callback(config)

    def open_config(icon, item):
        config_path = get_config_path()
        os.startfile(config_path)

    
    icon_path = os.path.join(os.path.dirname(get_config_path()), "icon.png")
    image = Image.open(icon_path)
    
    
    language_menu = pystray.Menu(
        pystray.MenuItem("日本語", change_language, checked=lambda item: config["language"] == "jp"),
        pystray.MenuItem("English", change_language, checked=lambda item: config["language"] == "en")
    )

    def create_version_menu():
        current_edition = config["edition"]
        return pystray.Menu(
            *[pystray.MenuItem(ver, change_version, checked=lambda item, v=ver: config["version"] == v)
              for ver in VERSIONS[current_edition]]
        )

    edition_menu = pystray.Menu(
        pystray.MenuItem("EX", change_edition, checked=lambda item: config["edition"] == "EX"),
        pystray.MenuItem("PRO", change_edition, checked=lambda item: config["edition"] == "PRO"),
        pystray.MenuItem("DEBUT", change_edition, checked=lambda item: config["edition"] == "DEBUT")
    )

    icon_theme_menu = pystray.Menu(
        pystray.MenuItem("dark_icon", change_icon_theme, checked=lambda item: config["large_image"] == "dark_icon"),
        pystray.MenuItem("darkgreen", change_icon_theme, checked=lambda item: config["large_image"] == "darkgreen"),
        pystray.MenuItem("default_icon", change_icon_theme, checked=lambda item: config["large_image"] == "default_icon"),
        pystray.MenuItem("neon_icon", change_icon_theme, checked=lambda item: config["large_image"] == "neon_icon"),
        pystray.MenuItem("neon1_icon", change_icon_theme, checked=lambda item: config["large_image"] == "neon1_icon"),
        pystray.MenuItem("white", change_icon_theme, checked=lambda item: config["large_image"] == "white")
    )


    menu = pystray.Menu(
        pystray.MenuItem("Open Config", open_config),
        pystray.MenuItem("Language", language_menu),
        pystray.MenuItem("Edition", edition_menu),
        pystray.MenuItem("Version", create_version_menu()),
        pystray.MenuItem("Icon Theme", icon_theme_menu),
        pystray.MenuItem("Reload", on_reload),
        pystray.MenuItem("Exit", on_exit)
    )

    icon = pystray.Icon("ClipStatus", image, "ClipStatus", menu)
    return icon

def main():
    print("Connecting to Discord Rich Presence...")
    RPC.connect()
    print("Connected!")

    config = load_config()
    edition = config.get("edition", "EX")
    lang = config.get("language", "jp")
    last_filename = None
    last_pid = None
    force_update = False

    def update_config_callback(new_config):
        nonlocal edition, lang, force_update
        edition = new_config.get("edition", "EX")
        lang = new_config.get("language", "jp")
        force_update = True

    
    tray_icon = None
    if not config.get("hide_tray", False):
        tray_icon = create_tray_icon(config, update_config_callback)
        tray_thread = threading.Thread(target=tray_icon.run)
        tray_thread.daemon = True
        tray_thread.start()
    else:
        print("Tray icon is hidden by config. Running in background...")

    try:
        while True:
            proc = find_csp_process()

            if proc:
                current_pid = proc.pid
                if current_pid != last_pid or force_update:
                    last_pid = current_pid
                    last_filename = None  
                    force_update = False  

                try:
                    cmdline = proc.cmdline()
                    filename = extract_info_from_cmdline(cmdline, lang)
                    
                    if filename != last_filename:
                        last_filename = filename
                        update_rpc(edition, filename, config)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            else:
                if last_filename is not None:
                    last_filename = None
                    last_pid = None
                    RPC.clear()  
            
            time.sleep(1)
    except KeyboardInterrupt:
        cleanup()
    except Exception as e:
        print(f"Error: {e}")
        cleanup()

if __name__ == "__main__":
    main()
