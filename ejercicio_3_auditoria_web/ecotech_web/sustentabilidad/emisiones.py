# Ejercicio 3 - Cálculo de huella de carbono - EcoTech


def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    # Calcula las emisiones de CO2 (kg) a partir del consumo en kWh
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo.")
    return consumo_kwh * factor_emision

def obtener_metricas_consumo(registros):
    # registros: lista de dicts {"planta": nombre, "consumo_kwh": número}
    # Devuelve el total global de emisiones y la planta de mayor consumo
    if not registros:
        return {"total_emisiones": 0, "planta_mayor_consumo": "Ninguna", "consumo_mayor": 0}

    total_emisiones = 0
    consumo_por_planta = {}

    for registro in registros:
        planta = registro["planta"]
        consumo = registro["consumo_kwh"]
        total_emisiones += calcular_emisiones_carbono(consumo)

        if planta in consumo_por_planta:
            consumo_por_planta[planta] += consumo
        else:
            consumo_por_planta[planta] = consumo

    planta_mayor = ""
    consumo_mayor = -1
    for planta, consumo in consumo_por_planta.items():
        if consumo > consumo_mayor:
            consumo_mayor = consumo
            planta_mayor = planta

    return {
        "total_emisiones": round(total_emisiones, 2),
        "planta_mayor_consumo": planta_mayor,
        "consumo_mayor": consumo_mayor,
    }

