import time
import math

class RunTime:

    # RunTime class is called at Runtime and works as a background process (it it called at each class init
    ProcessID = {} #Needs to be generated at RunTime using src/res/generated/processid.py
    Etime = {}
    def __init__(self,ProcessID):
        self.ProcessID[ProcessID] = 0
        self.ProcessClock = self.ProcessClock()

    class ProcessClock:
        def Start(self, ProcessID):
            # Start The Clock
            RunTime.Etime[ProcessID] = time.time()

        def Stop(self,ProcessID):
            # Stop The Clock and return process time
            StartTime = RunTime.Etime[ProcessID]
            EndTime = time.time()
            ProcessTime = EndTime - StartTime
            RunTime.ProcessID[ProcessID] = ProcessTime #Save the Process Time
            return ProcessTime

