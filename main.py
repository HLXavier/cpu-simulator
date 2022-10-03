from sqlite3 import Time
from scheduler import Scheduler
from time_tracker import TimeTracker

tracker = TimeTracker(no_log=False)
s = Scheduler(tracker)

# processos iguais pode dar ruim com o .remove(pcb)
s.add_process('programs/test', 0, 4)
s.add_process('programs/test', 2, 2)
s.add_process('programs/test', 4, 1)

s.run()

tracker.show_graph()
