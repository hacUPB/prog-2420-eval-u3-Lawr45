
def main():
    
    carros = {'Sedan':3,'Deportivo':1,'Camioneta':2}
    modelos = {'Sedan':['Corolla','M3','JETTA'],'Deportivo':['Mustang','Camaro','Ferrari'],'Camioneta':['Ranger','Taho','Hilux']}
    caracteristicas_especiales = {'Sedan':'HB','Deportivo':'Descapotable','Camioneta':'4x4'}
    caracteristicas = {'Color':{'Blanco':1,'Negro':1,'Gris':2},'Rines':{'De lujo':2,'Normal':3},'Silleteria':{'Cuero':3,'Tela':2}}
    
    def bienvenida_usuario():
        nombre = input(str("Por favor ingrese su nombre:  "))
        apellido = input(str('Por favor ingrese su apellido:  '))
        print(f'Bienvenido {nombre} {apellido} a Venta de Carros S.A')
        return nombre, apellido
    
    def mostrar_inventario():
        print("Se tienen los siguientes carros disponibles:  ")
        print(f"1. Sedan:  {carros.get('Sedan')}\n2. Deportivo {carros.get('Deportivo')} \n3. Camioneta:  {carros.get('Camioneta')}")  
    
    def seleccionar_carro():
        opcion = input(int('Por favor selecccione el tipo de carro que desea comprar:  '))
        carros_lista = list(carros.keys())
        if carros_lista[opcion] <=0:
            print('Carro no disponible')
        else:
            pass


if __name__ == "__main__":
    main()
