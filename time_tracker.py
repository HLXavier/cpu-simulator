import matplotlib.pyplot as plt

class TimeTracker:
    
    def __init__(self):
        self.events = []

    def register_event(self, time, pid, state):
        print(f'time: {time}, process {pid} moving to state {state}')
        self.events.append((time, pid, state))
    
    def show_graph(self):
        by_pid = self.group_by_pid()

        fig, gnt = plt.subplots()
        gnt.set_xlabel('Time units')
        gnt.set_ylabel('PID')

        gnt.set_yticks(list(map(lambda x: x * 10 + 5, range(len(by_pid)))))
        gnt.set_yticklabels(range(by_pid))

        for events in by_pid:
            for i in range(len(events) - 1):
                time, pid, state = events[i]
                next_time = events[i + 1][0]

                gnt.broken_barh([(time, next_time - time)], (pid * 10, 9), facecolors=('tab:orange'))

        gnt.show()


    def group_by_pid(self):
        by_pid = {}

        for e in self.events:
            pid = e[1]
            if pid not in by_pid:
                by_pid[pid] = []

            by_pid[pid].append(e)
        

        by_pid = list(by_pid.values())
        print(by_pid)

        by_pid.sort(key=lambda x: x[0][1])

        return by_pid
            