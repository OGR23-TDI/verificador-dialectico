class VerificadorDialectico:
    def __init__(self):
        # Base de conocimiento: Reglas lógicas para problemas de capacidad
        self.reglas = {
            'capacidad_ali': 120,
            'relacion_john': 8,
            'clases_john': 2
        }
    
    def generar_tesis(self):
        soluciones = [
            {
                'pasos': [
                    "Capacidad de John por clase: 120 / 8 = 15",
                    "Capacidad total de John: 15 * 2 = 30",
                    "Total combinado: 120 + 30 = 150"
                ],
                'respuesta': 150
            },
            {
                'pasos': [
                    "Capacidad total de John: 120 / 8 = 15",
                    "Total combinado: 120 + 15 = 135"
                ],
                'respuesta': 135
            },
            {
                'pasos': [
                    "Capacidad de John: 2 * (120 / 8) = 30",
                    "Total combinado: 120 + 30 = 150"
                ],
                'respuesta': 150
            }
        ]
        return soluciones
    
    def antitesis(self, solucion):
        errores = []
        capacidad_john = None
        
        for paso in solucion['pasos']:
            if "Capacidad de John por clase" in paso:
                if "120 / 8" not in paso:
                    errores.append("Error cálculo capacidad por clase de John.")
                else:
                    capacidad_john = 120 / 8
            if "Capacidad total de John" in paso:
                if capacidad_john is None:
                    errores.append("Falta calcular capacidad por clase de John.")
                elif f"{capacidad_john} * 2" not in paso:
                    errores.append("Error al sumar las dos clases de John.")
        
        return errores
    
    def sintesis(self, soluciones):
        mejor_solucion = None
        max_pasos_correctos = 0
        
        for sol in soluciones:
            errores = self.antitesis(sol)
            if len(errores) == 0:
                if len(sol['pasos']) > max_pasos_correctos:
                    mejor_solucion = sol
                    max_pasos_correctos = len(sol['pasos'])
        
        return mejor_solucion
    
    def resolver(self):
        soluciones = self.generar_tesis()
        mejor = self.sintesis(soluciones)
        return mejor


# Ejecución del verificador
if __name__ == "__main__":
    verificador = VerificadorDialectico()
    solucion_final = verificador.resolver()

    print("=== Solución Dialéctica Integrada ===")
    print("\nPasos:")
    for paso in solucion_final['pasos']:
        print(f"- {paso}")
    print(f"\nRespuesta Final: {solucion_final['respuesta']}")
