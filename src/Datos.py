
def main():
    
    carros = {'Sedan':3,'Deportivo':1,'Camioneta':2}
    modelos = {'Sedan':{'Corolla':15000,'M3':50000,'JETTA':20000},'Deportivo':{'Mustang':30000,'Camaro':35000,'Ferrari':250000},'Camioneta':{'Ranger':25000,'Taho':45000,'Hilux':40000}}
    caracteristicas_especiales = {'Sedan':{'HB':3000},'Deportivo':{'Descapotable':5000},'Camioneta':{'4x4':4000}}
    caracteristicas = {'Color':{'Blanco':500,'Negro':700,'Gris':600},'Rines':{'De lujo':1200,'Normal':500},'Silleteria':{'Cuero':1000,'Tela':500}}
    
    def bienvenida_usuario():
        nombre = input(str("Por favor ingrese su nombre:  "))
        apellido = input(str('Por favor ingrese su apellido:  '))
        print(f'Bienvenido {nombre} {apellido} a Venta de Carros S.A')
        return nombre, apellido
    
    def mostrar_inventario():
        print("Se tienen los siguientes carros disponibles:  ")
        print(f"1. Sedan:  {carros.get('Sedan')}\n2. Deportivo: {carros.get('Deportivo')} \n3. Camioneta:  {carros.get('Camioneta')}")  
    
    def seleccionar_carro():
        mostrar_inventario()
        opcion = int(input('Por favor seleccione el tipo de carro que desea comprar (1. Sedan, 2. Deportivo, 3. Camioneta):  '))
        tipo_carro = list(carros.keys())[opcion-1]
        
        if carros[tipo_carro] <= 0:
            print('Lo sentimos, no hay stock para este tipo de carro.')
            return None, None
        else:
            print(f"Modelos disponibles para {tipo_carro}: {list(modelos[tipo_carro].keys())}")
            modelo = input(f"Seleccione el modelo de {tipo_carro}: ").title()
            if modelo not in modelos[tipo_carro]:
                print("Modelo no válido. Intente de nuevo.")
                return None, None
            return tipo_carro, modelo
    
    def seleccionar_caracteristicas(tipo_carro):
        total = 0
    
        # Características Generales (pa todos)
        print("\nSeleccione las características adicionales:")
        for categoria, opciones in caracteristicas.items():
            print(f"\n{categoria}:")
            for opcion, precio in opciones.items():
                print(f"- {opcion}: ${precio}")
            seleccion = input(f"Seleccione {categoria}: ").title()
            if seleccion in opciones:
                total += opciones[seleccion]
    
        # Características especiales (de forma especifica)
        if tipo_carro in caracteristicas_especiales:
            for especial, precio in caracteristicas_especiales[tipo_carro].items():
                print(f"\nCaracterísticas especiales: {especial} - ${precio}")
            seleccion_especial = input("Seleccione característica especial (dejar vacío si no desea): ").title()
            if seleccion_especial in caracteristicas_especiales[tipo_carro]:
                total += caracteristicas_especiales[tipo_carro][seleccion_especial]
        
        return total
        
if __name__ == "__main__":
    main()
