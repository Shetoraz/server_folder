import requests
import mimetypes
import config

class Networker:

    def getServer(self):
        request = requests.get(config.PING_SERVER_URL)
        if request.status_code == 200:
            print("Server request done.")
            respone_json = request.json()
            server_name = respone_json['data']['server']
            request.close()
            return server_name
        else:
            print("Server request failed.")
            return None

    def uploadFile(self, server, file):
        fileType = mimetypes.guess_type(file)[0]
        files = {'file':('{}'.format(file), open('{}'.format(file), 'rb'), fileType)}
        request = requests.post('https://{}.gofile.io/uploadFile'.format(server), files=files)
        reponse_json = request.json()
        status = reponse_json['status']
        if status == 'ok':
            file_code = reponse_json['data']['code']
            admin_code = reponse_json['data']['adminCode']
            file_name = reponse_json['data']['fileName']
            print('{} uploaded!.\nFile URL: https://gofile.io/d/{}\nAdmin code: {}'.format(file_name, file_code, admin_code))
        else:
            print("File uploading failed.")
        
