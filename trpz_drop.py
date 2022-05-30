import requests
import json


class Request:
    auth = 'Bearer sl.BIcKrzv62ZbwcGKOQqIkwsf_t5rizHjFo2ex--dJc9awZmNH8ZsqYkE4Gmr3_oYbIy85G8zqMtYsdHkduko9tmKRRtej42KIjWKd83L4wpPQYM5pYwlFBo1JZz7gvqvHfvQvrc8R'
    method = "POST"

    def __init__(self) -> None:
        self.params1 = {
            'url': "https://content.dropboxapi.com/2/files/upload",
            'headers': {
                'Dropbox-API-Arg': '{"path": "/text.txt","mode": "add","autorename": true,"mute": false,"strict_conflict": false}',
                'Content-Type': 'application/octet-stream',
                'Authorization': self.auth
            }
        }
        self.params2 = {
            'url': "https://api.dropboxapi.com/2/sharing/get_file_metadata",
            'headers': {
                'Content-Type': 'application/json',
                'Authorization': self.auth
            }
        }
        self.params3 = {
            'url': "https://api.dropboxapi.com/2/files/delete_v2",
            'headers': {
                'Content-Type': 'application/json',
                'Authorization': self.auth
            }
        }

    def upload(self, rdata='This is test message for a new file'):
        self.response = requests.request(
            method=self.method,
            url=self.params1['url'],
            headers=self.params1['headers'],
            data=rdata
        )
        self.id = json.loads(self.response.text)['id']

    def get_file(self, id):
        self.response = requests.request(
            method=self.method,
            url=self.params2['url'],
            headers=self.params2['headers'],
            data=json.dumps(
                {
                    "file": f"{id}",
                    "actions": []
                }
            )
        )
        self.file_path = json.loads(self.response.text)['path_display']

    def delete_file(self, file_path):
        self.response = requests.request(
            method=self.method,
            url=self.params3['url'],
            headers=self.params3['headers'],
            data=json.dumps(
                {
                    "path": f"{file_path}"
                }
            )
        )

