class FileWriter:
    def __init__(self, fileName):
        self.file = open(fileName, "w")

    def write(self, a, b):
        self.file.write("%f %f\n" % (a,b))
        
    def writeTestResult(self, testName, time, delta):
        self.file.write("%s %f %f\n" % (testName, time, delta))

    def __del__(self):
 	self.file.close()