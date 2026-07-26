import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from aeris.config import settings


class SdCardHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        print(f"[SD Watcher] New file detected: {event.src_path}")


def watch_sd_card():
    watch_dir = Path(settings.sd_watch_dir)
    watch_dir.mkdir(parents=True, exist_ok=True)
    handler = SdCardHandler()
    observer = Observer()
    observer.schedule(handler, str(watch_dir), recursive=False)
    observer.start()
    print(f"[SD Watcher] Watching {watch_dir}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
