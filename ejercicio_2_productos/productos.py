# Ejercicio 2 - Productos, excepciones y persistencia - EcoTech

import json


class StockInvalidoError(Exception):
    """Se lanza cuando se intenta asignar un stock negativo."""
    pass


class DispositivoEcológico:
    # Clase base de los productos ecológicos: nombre, precio y stock
    # El stock es privado (__stock) y se valida con @property y setter: si es negativo lanza StockInvalidoError

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock  # Usamos el setter para validar 

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise StockInvalidoError(f"Stock inválido para {self.nombre}: {valor}. No puede ser negativo.")
        self.__stock = valor

    def ficha_tecnica(self):
        return f"{self.nombre} | Precio: ${self.precio} | Stock: {self.stock}"

    def to_dict(self):
        return {"tipo": "Dispositivo", "nombre": self.nombre, "precio": self.precio, "stock": self.stock}

class PanelSolar(DispositivoEcológico):
    # Clase hija: hereda nombre, precio y stock, y agrega potencia y eficiencia

    def __init__(self, nombre, precio, stock, potencia_w, eficiencia):
        super().__init__(nombre, precio, stock)
        self.potencia_w = potencia_w
        self.eficiencia = eficiencia

    # Polimorfismo: redefine la ficha técnica del padre
    def ficha_tecnica(self):
        return f"☀️ PANEL SOLAR {self.nombre} | Potencia: {self.potencia_w} W | Eficiencia: {self.eficiencia}% | Precio: ${self.precio} | Stock: {self.stock}"

    def to_dict(self):
        datos = super().to_dict()
        datos["tipo"] = "PanelSolar"
        datos["potencia_w"] = self.potencia_w
        datos["eficiencia"] = self.eficiencia
        return datos

class GestorInventario:
    # Guarda la lista de dispositivos en un archivo JSON

    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):
        datos = []
        for dispositivo in lista_dispositivos:
            datos.append(dispositivo.to_dict())

        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        print(f"Catálogo guardado en '{ruta_archivo}'")

if __name__ == "__main__":
    catalogo = []

    print("--- Cargando catálogo ---")
    try:
        panel1 = PanelSolar("SolarMax 400", 250000, 10, 400, 21.5)
        catalogo.append(panel1)
        print("Panel 1 creado con éxito.")
    except StockInvalidoError as e:
        print(f"Error inesperado: {e}")

    try:
        panel2 = PanelSolar("SolarMini 100", 90000, 0, 100, 18.0)
        catalogo.append(panel2)
        print("Panel 2 creado con éxito (stock 0 es válido).")
    except StockInvalidoError as e:
        print(f"Error inesperado: {e}")

    print("\nIntentando crear un panel con stock -3...")
    try:
        panel_malo = PanelSolar("SolarFail", 50000, -3, 50, 15.0)
        catalogo.append(panel_malo)
    except StockInvalidoError as e:
        print(f"✅ Error controlado: {e}")

    print("\nIntentando cambiar el stock del panel 1 a -1...")
    try:
        panel1.stock = -1
    except StockInvalidoError as e:
        print(f"✅ Error controlado: {e}")

    print("\n--- Catálogo válido ---")
    for dispositivo in catalogo:
        print(dispositivo.ficha_tecnica())

    gestor = GestorInventario()
    gestor.guardar_catalogo_json(catalogo, "catalogo_ecotech.json")
    