from utils import print_gantt_chart, compute_metrics

# ==============================
# 3. SRT (Preemptive SJF)
# ==============================
def srt(processes):
    time = 0
    completed = 0
    schedule = []

    while completed < len(processes):
        ready = [p for p in processes if p.arrival <= time and p.remaining > 0]

        if ready:
            ready.sort(key=lambda x: x.remaining)
            current = ready[0]

            schedule.append(current.pid)

            if current.start is None:
                current.start = time

            current.remaining -= 1
            time += 1

            if current.remaining == 0:
                current.finish = time
                completed += 1
        else:
            schedule.append("Idle")
            time += 1

    print_gantt_chart(schedule)
    compute_metrics(processes)