import time
from FileWriter import FileWriter

class FileWriterProvider:
    def __init__(self, name):
        self.name = name
        
    def getWriter(self, testName):
        times = time.strftime("%Y-%m-%d_%H-%M-%S")
        fileName = self.name + "_" + testName + "_" + times + ".txt"
        return FileWriter(fileName)