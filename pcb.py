pid = 0

class PCB:

    def __init__(self, process, arrival, timeout, priority):
        global pid
        self.pid = pid
        pid += 1
        self.process = process
        self.arrival = arrival
        self.timeout = timeout
        self.priority = priority