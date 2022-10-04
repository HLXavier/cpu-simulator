from scheduler import Scheduler
from time_tracker import TimeTracker
import sys

enable_log = '--log-transitions' in sys.argv
tracker = TimeTracker(no_log=not enable_log)
s = Scheduler(tracker)

s.add_process('programs/test', 0, 2, priority=0)
s.add_process('programs/test', 1, 3, priority=0)
s.add_process('programs/test', 1, 1, priority=2)

s.run()

display_graph = '--no-gantt' not in sys.argv
if display_graph:
    tracker.show_graph()
