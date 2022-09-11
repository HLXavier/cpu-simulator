class Program:

    CODE_START = '.code'
    CODE_END = '.endcode'

    DATA_START = '.data'
    DATA_END = '.enddata'

    LABEL_END = 'fim:'


    def __init__(self, path):
        self.code = []
        self.data = []
        self.labels = {}

        self.read_file(path)


    def read_file(self, path):
        
        program = convert_file(path)

        self.get_code(program)
        self.get_data(program)
        self.get_labels(program)


    def get_code(self, program):
        start = program.index(self.CODE_START)
        end = program.index(self.CODE_END)
        self.code = program[start+1 : end]
        self.remove_labels()

    
    def remove_labels(self):
        new_code = []
        in_label = False

        for line in self.code:

            if ':' in line and line != self.LABEL_END:
                in_label = True

            if not in_label:
                new_code.append(line)
            
            if line == self.LABEL_END:
                in_label = False    

        self.code = new_code 


    def get_data(self, program):
        start = program.index(self.DATA_START)
        end = program.index(self.DATA_END)
        self.data = program[start+1 : end]


    def get_labels(self, program):
        for i in range(len(program)):
            line = program[i]

            if ':' in line and line != self.LABEL_END:
                start = i
                end = start
                while program[end] != self.LABEL_END:
                    end += 1
                
                self.labels[line[:-1]] = program[start+1 : end]


def convert_file(path):
    file = open(path, 'r')
    file = file.read().split('\n')
    return remove_spaces(file) 


def remove_spaces(file):
    return [line.strip() for line in file if line]