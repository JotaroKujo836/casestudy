import copy
from process import Process
from utils import reset_processes
from schedulers.fcfs import fcfs
from schedulers.sjf import sjf
from schedulers.srt import srt
from schedulers.round_robin import round_robin
from schedulers.priority_np import priority_np
from schedulers.priority_rr import priority_rr

# ==============================
# Main Program
# ==============================
def main():
    while True:
        while True:
            try:
                n = int(input("Enter number of processes (>=3): "))
                if n >= 3:
                    break
                else:
                    print("Minimum of 3 processes required. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        processes = []

        i = 0
        while i < n:
            pid = f"P{i+1}"
            try:
                arrival = int(input(f"{pid} Arrival Time: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer for arrival time.")
                continue
            try:
                burst = int(input(f"{pid} Burst Time: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer for burst time.")
                continue
            if burst <= 0:
                print("Burst time must be positive. Please re-enter.")
                continue
            try:
                priority = int(input(f"{pid} Priority (lower number = higher priority): "))
            except ValueError:
                print("Invalid input. Please enter a valid integer for priority.")
                continue

            processes.append(Process(pid, arrival, burst, priority))
            i += 1

        while True:
            print("\n===== CPU Scheduling Menu =====")
            print("1. FCFS")
            print("2. SJF (Non-preemptive)")
            print("3. SRT (Preemptive)")
            print("4. Round Robin")
            print("5. Priority (Non-preemptive)")
            print("6. Priority + Round Robin")
            print("7. Re-enter process details")
            print("0. Exit")

            try:
                choice = int(input("Select: "))
            except ValueError:
                print("Invalid choice. Please enter a number.")
                continue

            if choice == 0:
                return

            if choice == 7:
                break

            proc_copy = copy.deepcopy(processes)
            reset_processes(proc_copy)

            if choice == 4:
                try:
                    q = int(input("Enter Time Quantum: "))
                    round_robin(proc_copy, q)
                except ValueError:
                    print("Invalid time quantum. Please enter a valid integer.")
                    continue
            elif choice == 1:
                fcfs(proc_copy)
            elif choice == 2:
                sjf(proc_copy)
            elif choice == 3:
                srt(proc_copy)
            elif choice == 5:
                priority_np(proc_copy)
            elif choice == 6:
                try:
                    q = int(input("Enter Time Quantum: "))
                    priority_rr(proc_copy, q)
                except ValueError:
                    print("Invalid time quantum. Please enter a valid integer.")
                    continue
            else:
                print("Invalid choice.")



if __name__ == "__main__":
    main()
