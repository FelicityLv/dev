#!/usr/bin/env python3
from http.client import HTTPConnection
import uuid
import json

guid = str(uuid.uuid4())


# class Connect():
#     def __init__(self, path):
#         # guid = str(uuid.uuid4())
#         h = HTTPConnection("localhost:8000")
#         h.request("GET", path)

#         r = h.getresponse()
#         if r.status != 200:
#             print(r.status)

#         self.data = json.loads(r.read().decode())


class CycloneAPI():
    def __init__(self, url):
        self.h = HTTPConnection(url)

    def connect(self, path):
        self.h.request("GET", path)

        r = self.h.getresponse()
        if r.status != 200:
            print(r.status)

        self.data = json.loads(r.read().decode())

    def system_info(self):
        result = self.connect("/system")
        print(f"system_info: \n{json.dumps(result.data, indent=4)}\n")

    def topics(self):
        result = self.connect("/topic")
        print(f"topics: \n{json.dumps(result.data, indent=4)}\n")

    def local_participants(self):
        result = self.connect("/local/participant")
        print(f"local_participants: \n{json.dumps(result.data, indent=4)}\n")

    def remote_participants(self):
        result = self.connect("/remote/participant")
        print(f"remote_participants: \n{json.dumps(result.data, indent=4)}\n")

    def local_participant(self):
        result = self.connect(f"/local/participant/{guid}")
        print(f"local_ participant: \n{json.dumps(result.data, indent=4)}\n")

    def remote_participant(self):
        result = self.connect(f"/remote/participant/{guid}")
        print(f"remote_participant: \n{json.dumps(result.data, indent=4)}\n")

    def local_participant_readers(self):
        result = self.connect(f"/local/participant/{guid}/readers")
        print(f"local_participant_readers: \n{json.dumps(result.data, indent=4)}\n")

    def local_participant_writers(self):
        result = self.connect(f"/local/participant/{guid}/writers")
        print(f"local_participant_writers: \n{json.dumps(result.data, indent=4)}\n")

    def remote_participant_readers(self):
        result = self.connect(f"/remote/participant/{guid}/readers")
        print(f"remote_participant_readers: \n{json.dumps(result.data, indent=4)}\n")

    def remote_participant_writers(self):
        result = self.connect(f"/remote/participant/{guid}/writers")
        print(f"remote_participant_writers: \n{json.dumps(result.data, indent=4)}\n")

    def local_readers(self):
        result = self.connect("/local/reader")
        print(f"local_readers: \n{json.dumps(result.data, indent=4)}\n")

    def remote_readers(self):
        result = self.connect("/remote/reader")
        print(f"remote_readers: \n{json.dumps(result.data, indent=4)}\n")

    def local_writers(self):
        result = self.connect("/local/writer")
        print(f"local_writers: \n{json.dumps(result.data, indent=4)}\n")

    def remote_writers(self):
        result = self.connect("/remote/writer")
        print(f"remote_writers: \n{json.dumps(result.data, indent=4)}\n")

    def local_reader(self):
        result = self.connect(f"/local/reader/{guid}")
        print(f"local_reader: \n{json.dumps(result.data, indent=4)}\n")

    def remote_reader(self):
        result = self.connect(f"/remote/reader/{guid}")
        print(f"remote_reader: \n{json.dumps(result.data, indent=4)}\n")

    def local_writer(self):
        result = self.connect(f"/local/writer/{guid}")
        print(f"local_writer: \n{json.dumps(result.data, indent=4)}\n")

    def remote_writer(self):
        result = self.connect(f"/remote/writer/{guid}")
        print(f"remote_writer: \n{json.dumps(result.data, indent=4)}\n")


api = CycloneAPI("localhost:8000")
api.system_info()

# if __name__ == "__main__":
#     system_info()
#     topics()
#     local_participants()
#     remote_participants()
#     local_participant()
#     remote_participant()
#     local_participant_readers()
#     local_participant_writers()
#     remote_participant_readers()
#     remote_participant_writers()
#     local_readers()
#     remote_readers()
#     local_writers()
#     remote_writers()
#     local_reader()
#     remote_reader()
#     local_writer()
#     remote_writer()
