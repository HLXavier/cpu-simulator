from sqlite3 import Time
from scheduler import Scheduler
from time_tracker import TimeTracker

tracker = TimeTracker(no_log=False)
s = Scheduler(tracker)

# processos iguais pode dar ruim com o .remove(pcb)
s.add_process('programs/test', 0, 1, priority=0)
s.add_process('programs/test', 0, 1, priority=2)
s.add_process('programs/test', 0, 1, priority=2)

s.run()

tracker.show_graph()
