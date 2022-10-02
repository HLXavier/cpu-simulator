from scheduler import Scheduler
from time_tracker import TimeTracker

tracker = TimeTracker()
tracker.register_event(0, 0, 'running')
tracker.register_event(1, 0, 'blocked')
tracker.register_event(2, 0, 'ready')
tracker.register_event(3, 0, 'running')
tracker.register_event(4, 0, 'exited')
tracker.show_graph()
exit()

s = Scheduler()

# processos iguais pode dar ruim com o .remove(pcb)
s.add_process('programs/test', 0, 1)
s.add_process('programs/test', 2, 1)
s.add_process('programs/test', 4, 1)

s.run()
