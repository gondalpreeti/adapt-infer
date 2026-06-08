# utils/controller.py
import psutil

def check_system_ram():
    available_ram_gb = psutil.virtual_memory().available / (1024**3)
    print(f"Your machine currently has {available_ram_gb:.2f} GB of RAM available.")
    return available_ram_gb

if __name__ == "__main__":
    check_system_ram()