# ==============================
# Utility Functions
# ==============================
def reset_processes(processes):
    for p in processes:
        p.remaining = p.burst
        p.start = None
        p.finish = None

def print_gantt_chart(schedule):
    print("\nGantt Chart:")

    labels = [str(p) for p in schedule]
    max_label_len = max((len(label) for label in labels), default=1)
    cell_width = max_label_len + 2

    line = ""
    for label in labels:
        line += "|" + label.center(cell_width)
    line += "|"
    print(line)

    max_num_len = len(str(len(schedule)))
    total_len = len(line) + max_num_len
    number_line = [" "] * total_len
    for i in range(len(schedule) + 1):
        pos = i * (cell_width + 1)
        for j, ch in enumerate(str(i)):
            number_line[pos + j] = ch

    print("".join(number_line).rstrip())

def compute_metrics(processes):
    total_wt = total_tat = 0

    print("\nProcess\tAT\tBT\tPR\tCT\tWT\tTAT")

    for p in processes:
        ct = p.finish
        tat = ct - p.arrival
        wt = tat - p.burst

        total_wt += wt
        total_tat += tat

        print(f"{p.pid}\t{p.arrival}\t{p.burst}\t{p.priority}\t{ct}\t{wt}\t{tat}")

    print("\nAverage Waiting Time:", round(total_wt / len(processes), 2))
    print("Average Turnaround Time:", round(total_tat / len(processes), 2))