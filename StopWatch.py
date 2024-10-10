import time
import sys
import select

class StopWatch:
    def __init__(self):
        self.startTime = None
        self.elapsedTime = 0
        self.running = False

    def startWatch(self):
        if not self.running:
            self.startTime = time.time()
            self.running = True
            
    def stopWatch(self):
        if self.running:
            self.elapsedTime = time.time() - self.startTime
            self.running = False
            
    def resetWatch(self):
        self.elapsedTime = 0
        self.running = False

    def returnTotalTime(self):
        totalTime = self.elapsedTime
        if self.running:
            totalTime += time.time() - self.startTime
        return totalTime
