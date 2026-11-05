from django.shortcuts import render

from .emisiones import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):
    # Datos simulados de consumo por planta (la consigna permite datos inventados)
    registros = [
        {"planta": "Planta Norte", "consumo_kwh": 1500},
        {"planta": "Planta Sur", "consumo_kwh": 2300},
        {"planta": "Planta Norte", "consumo_kwh": 900},
        {"planta": "Planta Oeste", "consumo_kwh": 1200},
    ]

    metricas = obtener_metricas_consumo(registros)

    contexto = {
        "titulo": "Panel de Sustentabilidad - EcoTech",
        "registros": registros,
        "total_emisiones": metricas["total_emisiones"],
        "planta_mayor_consumo": metricas["planta_mayor_consumo"],
        "consumo_mayor": metricas["consumo_mayor"],
    }
    return render(request, "sustentabilidad/panel.html", contexto)

