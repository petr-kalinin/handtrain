from TestController import TestController

class TestSequence:
    seq = []
    
    def __init__(self, joysticks, timer, writerProvider, requiredTime = 5000):
        self.joysticks = joysticks
        self.timer = timer
        self.writerProvider = writerProvider
        self.writer = writerProvider.getWriter("result")
        self.requiredTime = requiredTime
        
    def append(self, test):
        self.seq.append(TestController(self.joysticks,
                                        self.timer,
                                        test,
                                        self.writerProvider.getWriter(test.name()),
                                        self.requiredTime
                                       )
                        )
    
    def run(self):
        self.resDelta = []
        for controller in self.seq:
            controller.run()
            self.resDelta.append((controller.elapsedTime, controller.delta))
            self.writer.writeTestResult(controller.test.name(), controller.elapsedTime, controller.delta)
        return self.resDelta
    
                    
        
    