from watchdog.events import FileSystemEventHandler
import Network

network = Network.Networker()

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            print("New directory created")
            
        elif event.event_type == 'created':
            server_name = network.getServer()
            print('Received created event - {}.'.format(event.src_path))
            network.uploadFile(server_name, event.src_path)