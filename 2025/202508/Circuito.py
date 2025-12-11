from InterfazDistancia import InterfazDistancia

class Circuito(InterfazDistancia):


    def __init__(self, caja1, caja2):
        super().__init__()
        self._lista_cajas = {caja1, caja2}
        self._conexiones = [[caja1, caja2]]

    @property
    def lista_cajas(self):
        return self._lista_cajas

    @property
    def lista_conexiones(self):
        return self._conexiones

    def contain(self, caja):
        if caja in self._lista_cajas:
            return True
        return False

    def __str__(self):
        num_cajas = len(self._lista_cajas)
        num_conexiones =  len(self._conexiones)

        # 1. Generar la lista de representaciones de caja
        # Usamos una comprensión de listas para llamar a str() en cada objeto
        cajas_str = [str(caja) for caja in self._lista_cajas]

        # 2. Unir todas las representaciones con una flecha para mostrar el orden
        ruta_circuito = " -> ".join(cajas_str)

        # 3. Formatear la salida
        return (
            f"Circuito [Total Cajas: {num_cajas}]\n"
            f"  Ruta: {ruta_circuito}"
            f"  Conexiones: {num_conexiones}"
        )

    def crear_conexion(self, caja_interna, caja_nueva):
        conexion = [caja_interna, caja_nueva]
        self._conexiones.append(conexion)

    def poner_conexion(self, conexion):
        self._conexiones.append(conexion)


    def distancia(self, caja_a_comparar) :
        distancia_minima = None
        for caja_a_medir in self.lista_cajas :
            if not(caja_a_comparar == caja_a_medir):
                distancia_medida = caja_a_medir.distancia(caja_a_comparar)
                if(distancia_minima == None or distancia_medida > distancia_minima) :
                    distancia_minima = distancia_medida
        return distancia_minima

    def caja_menor_distancia(self, caja_a_comparar) :
        distancia_minima = None
        caja = None
        for caja_a_medir in self.lista_cajas :
            if not(caja_a_comparar == caja_a_medir):
                distancia_medida = caja_a_medir.distancia(caja_a_comparar)
                if(distancia_minima == None or distancia_medida > distancia_minima) :
                    distancia_minima = distancia_medida
                    caja = caja_a_medir
        return caja

    def poner_nueva_caja(self, nueva_caja):
        #caja_interna = self.caja_menor_distancia(nueva_caja)
        #self.crear_conexion(caja_interna, nueva_caja)
        self.lista_cajas.add(nueva_caja)
