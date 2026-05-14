from collections import deque
from utils import print_gantt_chart, compute_metrics

# ==============================
# 4. Round Robin
# ==============================
def round_robin(processes, quantum):
    time = 0
    queue = deque()
    schedule = []

    processes.sort(key=lambda x: x.arrival)
    i = 0

    while i < len(processes) or queue:
        while i < len(processes) and processes[i].arrival <= time:
            queue.append(processes[i])
            i += 1

        if queue:
            current = queue.popleft()

            if current.start is None:
                current.start = time

            exec_time = min(quantum, current.remaining)

            for _ in range(exec_time):
                schedule.append(current.pid)
                time += 1

            current.remaining -= exec_time

            while i < len(processes) and processes[i].arrival <= time:
                queue.append(processes[i])
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