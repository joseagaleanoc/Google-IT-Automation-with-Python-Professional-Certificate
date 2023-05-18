#!/usr/bin/env python3
import psutil
import shutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free

def check_cpu_usage():
    usage = psutil.cpu_percent(60)
    return usage

du = check_disk_usage("/")
cpu = check_cpu_usage()

if du < 20 or cpu > 75:
    print(f"ERROR!")
else:
    print("Everything is OK!")

print(f"Disk: {du}")
print(f"CPU: {cpu}")
