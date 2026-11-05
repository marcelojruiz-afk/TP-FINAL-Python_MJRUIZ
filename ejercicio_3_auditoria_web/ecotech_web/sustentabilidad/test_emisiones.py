# Ejercicio 3 - Punto A: Auditoría del cálculo de emisiones con unittest
import unittest

from sustentabilidad.emisiones import calcular_emisiones_carbono, obtener_metricas_consumo


class TestCalculoEmisiones(unittest.TestCase):

    def test_valor_nominal(self):
        # 100 kWh * 0.4 = 40.0 kg de CO2
        self.assertAlmostEqual(calcular_emisiones_carbono(100), 40.0)

    def test_factor_personalizado(self):
        # 250 kWh * 0.5 = 125.0
        self.assertAlmostEqual(calcular_emisiones_carbono(250, 0.5), 125.0)

    def test_consumo_cero(self):
        self.assertEqual(calcular_emisiones_carbono(0), 0)

    def test_consumo_negativo_lanza_error(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-10)

    def test_metricas_planta_mayor(self):
        registros = [
            {"planta": "Planta Norte", "consumo_kwh": 1500},
            {"planta": "Planta Sur", "consumo_kwh": 2300},
            {"planta": "Planta Norte", "consumo_kwh": 900},
        ]
        metricas = obtener_metricas_consumo(registros)
        self.assertAlmostEqual(metricas["total_emisiones"], 1880.0)
        self.assertEqual(metricas["planta_mayor_consumo"], "Planta Norte")
        