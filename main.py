from program import Program
from process import Process


program = Program('programs/test')
process = Process(program)

message = ''

while message != 'exit':
    message = process.step()
