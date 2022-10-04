from sqlite3 import Time
from scheduler import Scheduler
from time_tracker import TimeTracker
import sys

enable_log = len(sys.argv) > 1 and sys.argv[1] == '--log-transitions'
tracker = TimeTracker(no_log=not enable_log)
s = Scheduler(tracker)

# processos iguais pode dar ruim com o .remove(pcb)
s.add_process('programs/test', 0, 2, priority=0)
s.add_process('programs/test', 1, 3, priority=0)
s.add_process('programs/test', 1, 1, priority=2)


s.run()

tracker.show_graph()
