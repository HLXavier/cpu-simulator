import matplotlib.pyplot as plt
import json

color_by_state = {
    'ready': '#989898',
    'blocked': '#555555',
    'running': '#000000'
}

class TimeTracker:
    
    def __init__(self, no_log=False):
        self.events = []
        self.no_log = no_log

    def register_event(self, time, pid, state):
        if not self.no_log:
            print(f'time: {time}, process {pid} moving to state {state}')
        
        self.events.append((time, pid, state))
    
    def show_graph(self):
        by_pid = self.group_by_pid()

        fig, gnt = plt.subplots()
        gnt.set_xlabel('Time units')
        gnt.set_ylabel('PID')

        gnt.set_yticks(list(map(lambda x: x * 10 + 5, range(len(by_pid)))))
        gnt.set_yticklabels(range(len(by_pid)))
        gnt.grid(True, 'major', 'x')

        existing_states = []

        for events in by_pid:
            for i in range(len(events) - 1):
                time, pid, state = events[i]
                next_time, _, _ = events[i + 1]

                label = '_'
                if state not in existing_states:
                    existing_states.append(state)
                    label = state
                    
                gnt.broken_barh([(time, next_time - time)], (pid * 10, 9), facecolors=color_by_state[state], label=label)
        
        f = open('./out.json', 'w')
        f.write(json.dumps(by_pid))
        f.close()

        plt.legend()

        plt.show()


    def group_by_pid(self):
        by_pid = {}

        for e in self.events:
            pid = e[1]
            if pid not in by_pid:
                by_pid[pid] = []

            by_pid[pid].append(e)
        

        by_pid = list(by_pid.values())
        by_pid.sort(key=lambda x: x[0][1])

        for events in by_pid:
            events.sort(key=lambda e: e[0])

        return by_pid
            