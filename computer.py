class Computer: 

    def __init__(self):
        self.acc = 0
        self.pc = 0
        self.op = 0
        self.memory = {}
    

    def add_variable(self, variable, value):
        self.memory[variable] = value


    # Arithmetic
    def add(self):
        self.acc += self.op


    def sub(self):
        self.acc -= self.op


    def mult(self):
        self.acc *= self.op


    def div(self):
        self.acc /= self.op


    # Memory
    def load(self):
        self.acc = self.op


    def store(self):
        self.op = self.acc
    

    # Jumps
    def brany(self):
        self.pc = self.op


    def brpos(self):
        if self.acc > 0:
            self.pc = self.op


    def brzero(self):
        if self.acc == 0:
            self.acc = self.op


    def brneg(self):
        if self.acc < 0:
            self.acc = self.op
        
        
    # System
    def syscall(self):
        if self.op == 0:
            exit()
        
        if self.op == 1:
            print(self.acc)

        # where to store?
        if self.op == 2:
            self.op = input()