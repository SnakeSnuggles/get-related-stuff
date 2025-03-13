import json

class File:
    def __init__(self,file_path:str):
        self.file_path = file_path
        self.read()
    def __str__(self):
        return self.file_data
    def read(self):
        if self.file_path.split(".")[1] == "json":
            with open(self.file_path,"r") as file:
                self.file_data = json.loads(file.read()) 
                return
        with open(self.file_path,"r") as file:
            self.file_data = file.read()
    def write(self,text):
        with open(self.file_path,"w") as file:
            file.write(text)
        self.read()
    def append(self,text):
        with open(self.file_path,"a") as file:
            file.write(text)
        self.read()
