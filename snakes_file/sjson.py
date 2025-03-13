import json

class sjson:
    def __init__(self,path):
        self.path = path
        self.content = {} 
        with open(self.path,"r") as file:
            self.content = json.loads(file.read())
    def __get__(self):
        ...
    def __set__(self):
        ...
