class Program:

    CODE_START = '.code'
    CODE_END = '.endcode'

    DATA_START = '.data'
    DATA_END = '.enddata'


    def __init__(self, path):
        self.code = []
        self.data = []
        self.labels = {}

        self.read_file(path)
        

    def read_file(self, path):
        
        program = convert_file(path)

        self.get_code(program)
        self.get_data(program)
        self.get_labels()


    def get_code(self, program):
        start = program.index(self.CODE_START)
        end = program.index(self.CODE_END)
        self.code = program[start+1 : end]


    def get_data(self, program):
        start = program.index(self.DATA_START)
        end = program.index(self.DATA_END)
        self.data = program[start+1 : end]

    
    def get_labels(self):
        for i in range(len(self.code)):
            line = self.code[i]

            if line[-1] == ':':
                self.labels[line[:-1]] = i


def convert_file(path):
    file = open(path, 'r')
    file = file.read().split('\n')
    return [line.strip() for line in file if line]
