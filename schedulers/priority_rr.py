from collections import deque
from utils import print_gantt_chart, compute_metrics

# ==============================
# 6. Priority + Round Robin
# ==============================
def priority_rr(processes, quantum):
    time = 0
    schedule = []
    queues = {}

    processes.sort(key=lambda x: x.arrival)
    i = 0

    while i < len(processes) or any(queues.values()):
        while i < len(processes) and processes[i].arrival <= time:
            queues.setdefault(processes[i].priority, deque()).append(processes[i])
            i += 1

        ready_priorities = [p for p, q in queues.items() if q]

        if ready_priorities:
            current_pr = min(ready_priorities)
            queue = queues[current_pr]
            current = queue.popleft()

            if current.start is None:
                current.start = time

            exec_time = min(quantum, current.remaining)

            for _ in range(exec_time):
                schedule.append(current.pid)
                time += 1

            current.remaining -= exec_time

            while i < len(processes) and processes[i].arrival <= time:
                queues.setdefault(processes[i].priority, deque()).append(processes[i])
                i += 1

            if current.remaining > 0:
                queue.append(current)
            else:
                current.finish = time
        else:
            schedule.append("Idle")
            time += 1

    print_gantt_chart(schedule)
    compute_metrics(processes)