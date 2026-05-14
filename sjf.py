from utils import print_gantt_chart, compute_metrics

# ==============================
# 2. SJF (Non-preemptive)
# ==============================
def sjf(processes):
    time = 0
    completed = []
    schedule = []

    while len(completed) < len(processes):
        ready = [p for p in processes if p.arrival <= time and p not in completed]

        if ready:
            ready.sort(key=lambda x: x.burst)
            current = ready[0]

            for _ in range(current.burst):
                schedule.append(current.pid)

            current.start = time
            time += current.burst
            current.finish = time
            completed.append(current)
        else:
            schedule.append("Idle")
            time += 1

    print_gantt_chart(schedule)
    compute_metrics(processes)