from handler import Handler
from watchdog.observers import Observer
import config
import time

class Watcher:
    
    monitoring_dir = config.MONITORING_PATH

    def __init__(self):
        self.observer = Observer()
    
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.monitoring_dir, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print('Timing error!')

        self.observer.join()