import psutil

def calcular_fragmentacion_interna():
    memoria_virtual = psutil.virtual_memory()
    memoria_total = memoria_virtual.total
    memoria_disponible = memoria_virtual.available
    fragmentacion_interna = memoria_total - memoria_disponible
    porcentaje_fragmentacion_interna = (fragmentacion_interna / memoria_total) * 100

    return porcentaje_fragmentacion_interna

fragmentacion_interna = calcular_fragmentacion_interna()
print(f"El porcentaje de fragmentación interna es: {fragmentacion_interna}%")
