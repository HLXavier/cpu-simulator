class Process: 

    EXIT = 'exit'
    PRINT = 'print'
    INPUT = 'input'

    def __init__(self, program):
        self.program = program
        self.acc = 0
        self.pc = 0
        self.memory = {}

        for line in program.data:
            var, value, *_ = line.split()
            self.memory[var] = int(value)

        self.commands = {
            'add': self.add,
            'sub': self.sub,
            'mult': self.mult,
            'div': self.div,

            'load': self.load,
            'store': self.store,

            'brany': self.brany,
            'brpos': self.brpos,
            'brzero': self.brzero,
            'brneg': self.brneg,

            'syscall': self.syscall,
            'dump': self.dump
        }

    
    def step(self): 

        if self.pc >= len(self.program.code):
            return

        line = self.program.code[self.pc]
        self.pc += 1

        if line[-1] == ':': 
            return 

        command, op, *_ = line.split()

        if command in ['add', 'sub', 'mult', 'div', 'load']:
            op = self.handle_op(op)

        return self.commands[command](op)


    def handle_op(self, op):
        if '#' in op:
            return int(op[1:])
        
        if op in self.memory:
            return self.memory[op]

        return op


    # Arithmetic
    def add(self, op):
        self.acc += op


    def sub(self, op):
        self.acc -= op


    def mult(self, op):
        self.acc *= op


    def div(self, op):
        self.acc //= op


    # Memory
    def load(self, op):
        self.acc = op


    def store(self, op):
        self.memory[op] = self.acc
    

    # Jumps
    def brany(self, op):
        self.jump(op)


    def brpos(self, op):
        if self.acc > 0: 
            self.jump(op)


    def brzero(self, op):
        if self.acc == 0: 
            self.jump(op)


    def brneg(self, op):
        if self.acc < 0: 
            self.jump(op)

    
    def jump(self, op):
        self.pc = self.program.labels[op]


    def dump(self, op):
        print(f'Dump:\n\tMem: {self.memory}\n\tAcc: {self.acc}')
        
        
    # System
    def syscall(self, op):
        if op == '0':
            return self.EXIT
        
        if op == '1':
            print(f'output: {self.acc}')
            return self.PRINT

        if op == '2':
            print('input:')
            self.acc = int(input())
            return self.INPUT
