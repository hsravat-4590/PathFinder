import time
import glob
import os


class ProcessID:
    # A process ID is a hexadecimal string which is formed using the time and sender
    ProcedureKey = 'key'
    Sender = ''
    def __init__(self,Sender):
        self.Sender = Sender
        self.GenerateKey = self.GenerateKey()
        self.ProcessClean = self.ProcessClean()

    def GenerateKey(self):
        tim = time.time()
        tim = tim.__hash__()
        print(tim)
        sender = self.Sender
        senderhex = sender.encode('utf-8')
        senderhex = id(senderhex)
        senderhex = senderhex.__hash__()
        print (senderhex)
        processKey = tim + senderhex
        processKey = processKey.__str__()
        #Save the Key
        dir = "res/generated/keys/" + processKey
        keyDoc = open(dir, 'x')
        keyDoc.write(processKey)
        keyDoc.close()
        return processKey

    def ProcessClean(self):
        # Cleans the Process Cache DO NOT DO IF PROCESSES ARE IN ACTION OR IT WILL BREAK THE RUNTIME
        files = glob.glob('res/generated/keys/*')
        for f in files:
            os.remove(f)
