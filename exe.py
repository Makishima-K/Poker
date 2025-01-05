import subprocess

# Пути к файлам приложений
apps = ["poker.py", "poker2.py", "finall.py"]

# Список для хранения процессов
processes = []

try:
    # Запуск каждого приложения в отдельном процессе
    for app in apps:
        process = subprocess.Popen(["python", app])
        processes.append(process)
        print(f"Запущено: {app} (PID: {process.pid})")

    # Ожидание завершения всех процессов
    for process in processes:
        process.wait()

except KeyboardInterrupt:
    # Обработка прерывания (Ctrl+C) и завершение процессов
    print("\nПрерывание! Завершаем все процессы...")
    for process in processes:
        process.terminate()
    print("Все процессы завершены.")
