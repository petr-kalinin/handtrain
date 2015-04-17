from Patient import Patient

class ConsolePatient(Patient):
    def __init__(self):
        print(self.prompt)
        self.name = input()
        