from TestController import TestController

class TestSequence:
    seq = []
    
    def __init__(self, joystick1, joystick2, timer, writerProvider):
        self.joystick1 = joystick1
        self.joystick2 = joystick2
        self.timer = timer
        self.writerProvider = writerProvider
        self.writer = writerProvider.getWriter("result")
        
    def append(self, test):
        self.seq.append(TestController(self.joystick1,
                                        self.joystick2,
                                        self.timer,
                                        test,
                                        self.writerProvider.getWriter(test.name())
                                       )
                        )
    
    def run(self):
        self.resDelta = []
        for controller in self.seq:
            controller.run()
            self.resDelta.append((controller.elapsedTime, controller.delta))
            self.writer.writeTestResult(controller.test.name(), controller.elapsedTime, controller.delta)
        return self.resDelta
    
                    
        
    