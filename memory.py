import psutil
import threading
import multiprocessing
import os


def mostrar_procesos():
    for p in psutil.process_iter():
        print(f"Nombre: {p.name}")
        print(f"ID: {p.pid}")
        print(f"Estado: {p.status}")
        print(f"Memoria: {p.memory_info().rss / 1024**2} MB")


def crear_hilo():
    threading.Thread(target=mostrar_procesos).start()


def crear_proceso():
    multiprocessing.Process(target=mostrar_procesos).start()


if __name__ == "__main__":
    mostrar_procesos()
    crear_hilo()
    crear_proceso()
