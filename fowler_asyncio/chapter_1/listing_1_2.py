# однопоточное приложение
import os
import threading

print(f"Исполняется Python-процесс с id: {os.getgid()}")

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f"В данный момент Python исполняет {total_threads} потоков")
print(f"Иия текущего потока {thread_name}")
