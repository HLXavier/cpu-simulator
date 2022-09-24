from scheduler import Scheduler

s = Scheduler()

# processos iguais pode dar ruim com o .remove(pcb)
s.add_process('programs/test2', 0, 1)
s.add_process('programs/test2', 2, 1)
s.add_process('programs/test2', 4, 1)

s.run()

print(s.exit)
