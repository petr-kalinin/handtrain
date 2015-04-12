from TestController import TestController

class TestSequence:
    seq = []
    
    def __init__(self, joystick1, joystick2, timer):
        self.joystick1 = joystick1
        self.joystick2 = joystick2
        self.timer = timer
        
    def append(self, test, writer):
        self.seq.append(TestController(self.joystick1,
                                        self.joystick2,
                                        self.timer,
                                        test,
                                        writer
                                       )
                        )
    
    def run(self):
        self.resDelta = []
        for controller in self.seq:
            controller.run()
            self.resDelta.append((controller.elapsedTime, controller.delta))
        return self.resDelta
                    
        
    