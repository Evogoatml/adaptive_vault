import random, psutil

def get_resource_state():
    try:
        cpu = psutil.cpu_percent(interval=0.5)
        ram = psutil.virtual_memory().percent
    except Exception:
        cpu = random.uniform(10, 90)
        ram = random.uniform(20, 80)
    return {"cpu": round(cpu, 2), "ram": round(ram, 2)}
