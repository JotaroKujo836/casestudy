from utils import print_gantt_chart, compute_metrics

# ==============================
# 1. FCFS
# ==============================
def fcfs(processes):
    processes.sort(key=lambda x: x.arrival)
    time = 0
    schedule = []

    for p in processes:
        if time < p.arrival:
            for _ in range(p.arrival - time):
                schedule.append("Idle")
            time = p.arrival

        p.start = time
        for _ in range(p.burst):
            schedule.append(p.pid)
        time += p.burst
        p.finish = time

    print_gantt_chart(schedule)
    compute_metrics(processes)