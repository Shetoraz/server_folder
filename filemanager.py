from pathlib import Path
import config

class FileManager():
    
    def dump(self, text):
        with open(config.DB_FILE, "a+") as file:
            file.write(text)