import psutil
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime

# Initialize lists for plotting
cpu_usage = []
ram_usage = []
timestamps = []

# Set up figure
fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle("Real-Time CPU and RAM Usage Monitor")

def update(frame):
    # Get system stats
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    time_now = datetime.now().strftime('%H:%M:%S')

    # Append to lists
    cpu_usage.append(cpu)
    ram_usage.append(ram)
    timestamps.append(time_now)

    # Limit list size for performance
    max_length = 30
    if len(cpu_usage) > max_length:
        cpu_usage.pop(0)
        ram_usage.pop(0)
        timestamps.pop(0)

    # Clear previous plots
    ax1.clear()
    ax2.clear()

    # Plot CPU
    ax1.plot(timestamps, cpu_usage, color='blue')
    ax1.set_title("CPU Usage (%)")
    ax1.set_ylim(0, 100)
    ax1.tick_params(axis='x', rotation=45)

    # Plot RAM
    ax2.plot(timestamps, ram_usage, color='green')
    ax2.set_title("RAM Usage (%)")
    ax2.set_ylim(0, 100)
    ax2.tick_params(axis='x', rotation=45)

    # Write to log
    with open("usage_log.txt", "a") as log_file:
        log_file.write(f"{time_now} - CPU: {cpu}% | RAM: {ram}%\n")

# Animate every 1000 ms
ani = animation.FuncAnimation(fig, update, interval=1000)
plt.tight_layout()
plt.show()
