class PCB:

    def __init__(self, process, arrival, quantum, priority):
        self.process = process
        self.arrival = arrival
        self.quantum = quantum
        self.priority = priority