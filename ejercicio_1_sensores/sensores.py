# Ejercicio 1 - Sanatización y análisis de sensores - EcoTech
def limpiar_registro_sensor(registro_raw):

    # Ejemplo de entrada: {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"}
    # Devuelve un dict nuevo: sensor_id sin espacios, temperatura float sin la C, ubicacion "Sin ubicación" si falta o está vacía

    registro_limpio = {}
    registro_limpio["sensor_id"] = registro_raw.get("sensor_id", "").strip()
    registro_limpio["temperatura"] = float(str(registro_raw.get("temperatura", "0")).strip().upper().replace("C", ""))
    registro_limpio["ubicacion"] = registro_raw.get("ubicacion") or "Sin ubicación"
    return registro_limpio

def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):

    # Recibe la lista de sensores ya limpios y un umbral
    # Devuelve una tupla: (lista de sensor_id que superan el umbral, promedio de temperatura)

    if not lista_sensores_limpios:
        return ([], 0.0)

    sensores_alerta = []
    suma_temperaturas = 0.0

    for sensor in lista_sensores_limpios:
        suma_temperaturas += sensor["temperatura"]
        if sensor["temperatura"] > umbral_temperatura:
            sensores_alerta.append(sensor["sensor_id"])

    promedio_temperatura = suma_temperaturas / len(lista_sensores_limpios)
    return (sensores_alerta, promedio_temperatura)

if __name__ == "__main__":
    datos_crudos = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": "SENSOR-002  ", "temperatura": " 31.2C", "ubicacion": ""},
        {"sensor_id": " SENSOR-003", "temperatura": "28.7c"},
        {"sensor_id": "SENSOR-004 ", "temperatura": "22.0C", "ubicacion": "Planta Sur"},
    ]

    print("--- Etapa de sanitización ---")
    sensores_limpios = []
    for registro in datos_crudos:
        sensores_limpios.append(limpiar_registro_sensor(registro))
    for sensor in sensores_limpios:
        print(sensor)

    print("\n--- Reporte consolidado ---")
    alertas, promedio = generar_resumen_sensores(sensores_limpios, 30)
    print(f"Sensores en alerta (> 30 °C): {alertas}")
    print(f"Promedio de temperatura de la planta: {promedio:.2f} °C")
    