def validar_titulo(titulo):
    if titulo.strip() != "":
        return True
    else:
        return False
def validar_autor(autor):
    if autor.strip() != "":
        return True
    else:
        return False
def validar_genero(genero):
    if genero.strip() != "":
        return True
    else:
        return False
def valdiar_año(año):
    if año >0:
        return True
    else:
        return False
def validar_editorial(editorial):
    if editorial.strip() != "":
        return True
    else:
        return False
libros = {
'L001': ['Sombras del Sur', 'A. Rojas', 'novela', 2019, 'AndesPress', False],
'L002': ['Python en Ruta', 'M. Diaz', 'tecnología', 2023, 'CodeBooks', True],
'L003': ['Mar y Viento', 'C. Silva', 'poesía', 2017, 'Litoral', False],
'L004': ['Historia Breve', 'J. Pérez', 'historia', 2015, 'Cronos', False],
'L005': ['Mundos Lejanos', 'L. Torres', 'ciencia ficción', 2021, 'Orión', True],
'L006': ['Cocina Simple', 'R. Soto', 'cocina', 2018, 'Sabores', False],
}
prestamos = {
'L001': [500, 4],
'L002': [700, 0],
'L003': [300, 10],
'L004': [400, 2],
'L005': [600, 1],
'L006': [350, 6],
}
def buscar_codigo(codigo):
    codigo_normalizado = codigo.strip().upper()
    for clave in prestamos:
        if clave.strip().upper() == codigo_normalizado:
            return True
    return False
def clave_real(codigo):
    codigo_normalizado = codigo.strip().upper()
    for clave in prestamos:
        if clave.strip().upper() == codigo_normalizado:
            return clave
    return None
def precio_multa(multa):
    if multa >0:
        return True
    else:
        return False
def copias_disponibles(copias):
    if copias >0:
        return True
    else:
        return False
def mostrar_menu():
    print("""========== MENÚ PRINCIPAL ==========
1. Copias por género
2. Búsqueda de libros por rango de multa
3. Actualizar multa de libro
4. Agregar libro
5. Eliminar libro
6. Salir
=====================================""")
def leer_opc():
    while True:
        try:
            op = int(input("Ingrese Una opción: "))
        except ValueError:
            print("Error: La opción debe ser un número entero.")
        else:
            if op >=1 and op <=6:
                return op
            else:
                print("Error:debe estar en el rango de 1 y 6.")
def copias_genero(genero):
    total = 0
    genero_normalizado = genero.strip().lower()
    for codigo, datos in libros.items():
        if datos[2].strip().lower() == genero_normalizado:
            if codigo in libros:
                total += prestamos[codigo][2]
                print(f"El total de copias disponibles es: {total}")
def busqueda_multa(multa_min, multa_max):
    resultados = []
    for codigo, datos in prestamos.items():
        multa = datos[0]
        copias = datos[1]
        if multa_min <= multa <= multa_max and copias != 0:
            if codigo in libros:
                titulo = libros[codigo][0]
                resultados.append(f"{titulo}--{codigo}")
    if resultados:
        resultados.sort()
        print(f"Los libros encontrados son: {resultados}")
    else:
        print("No hay libros en ese rango de multa")
def actualizar_multa(codigo, nueva_multa):
    if buscar_codigo(codigo):
        clave = clave_real(codigo)
        prestamos[clave][0] = nueva_multa
        return True
    return False
def validar_codigo(codigo):
    if codigo.strip() != "":
        return False
    if buscar_codigo(codigo):
        return False
    return True
def validar_titulo(titulo):
    return titulo.strip() != ""
def validar_autor(autor):
    return autor.strip() != ""
def validar_genero(genero):
    return genero.strip() != ""
def validar_año(año):
    return isinstance(año, int) and año >0
def validar_editorial(editorial):
    return editorial.strip() != ""
def validar_es_novedad(valor):
    return valor.strip().lower() in ('s', 'n')
def validar_precio_multa(precio):
    return isinstance(precio, int) and precio >0
def validar_copias_disponibles(copias):
    return isinstance(copias, int) and copias >=0
def agregar_libro(codigo, titulo, autor, genero, año, editorial, es_novedad, precio_multa, copias):
    if buscar_codigo(codigo):
        return False
    libros[codigo] = [titulo, autor, genero, año, editorial, es_novedad]
    prestamos[codigo] = [precio_multa, copias]
    return True
def eliminar_libro(codigo):
    if buscar_codigo(codigo):
        clave = clave_real(codigo)
        del libros[clave]
        del prestamos[clave]
        return True
    return False
def op_copias_genero():
    genero = input("Ingrese género a consultar: ")
    copias_genero(genero)
def soli_raqngo_multa():
    while True:
        try:
            multa_min = int(input("ingrese multa mínima: "))
            multa_max = int(input("Ingrese multa máxima: "))
        except ValueError:
            print("Debe ingresar valores enteros.")
            continue
        if multa_min <0 or multa_max <0:
            print("Debe ingresar valores enteros.")
            continue
        if multa_min > multa_max:
            print("Debe ingresar valores enteros.")
            continue
        return multa_min, multa_max
def op_busqueda_multa():
    multa_min, multa_max = soli_raqngo_multa()
    busqueda_multa(multa_min,multa_max)

def soli_nueva_multa():
    while True:
        try:
            nueva_multa = int(input("Ingrese nueva multa: "))
        except ValueError:
            print("Debe ingresar un valor entero.")
            continue
        if nueva_multa <= 0:
            print("La multa debe ser un número entero o mayor que cero.")
            continue
        return nueva_multa
def op_actualizar_multa():
    codigo = input("Ingrese código del libro: ")
    nueva_multa = soli_nueva_multa()
    if actualizar_multa(codigo,nueva_multa):
        print("Multa Actualizada")
    else:
        print("El codigo no existe")
def op_agregar_libro():
    codigo = input("Ingrese codigo: ")
    titulo = input("Ingrese titulo: ")
    autor = input("Ingrese autor:")
    genero= input("Ingrese genero: ")
    añostr= input("ingrese año")
    editorial = input("ingrese editorial: ")
    novedad = input("¿Es novedad? (s/n)")
    multa = int(input("Ingreser precio de multa: "))
    copias = int(input("Ingrese copias disponibles: "))
    if not validar_codigo(codigo):
        print("El codigo no es valido o ya existe")
    if not validar_titulo(titulo):
        print("El titulo no es valido")
    if not validar_autor(autor):
        print("El autor no es valido")
    if not validar_genero(genero):
        print("El genero no es valido")
    if not validar_editorial(editorial):
        print("El editorial no es valido")
    if not validar_es_novedad(novedad):
        print("El valor de novedad debe ser 's' o 'n'")
    año = None
    try:
        añ = int(añostr)
        if not validar_año(añ):
            print("El año debe ser un número mayor que cero.")
    except ValueError:
        print("El año debe ser un número entero mayor que cero.")
    precio_multa = None
    try:
        precio_multa = int(multa)
        if not validar_precio_multa(precio_multa):
            print("El precio de la multa debe ser un número mayor que cero")
    except ValueError:
        print("El precio de la multa debe ser un número entero mayor que cero")
    copias_disponibles =None
    try:
        copias_disponibles = int(copias)
        if not validar_copias_disponibles(copias_disponibles):
            print("Las copias disponibles deben ser un número entero mayor o igual a cero")
    except ValueError:
        print("Las copias disponibles deben ser un número entero mayor o igual a cero")

    es_novedad = novedad.strip().lower() == 's'
    if agregar_libro(codigo, titulo, autor, genero, año, editorial,es_novedad, precio_multa, copias_disponibles):
        print("Libro agregado")
    else:
        print("El código ya existe")
def op_eliminar_libro():
    codigo = input("Ingrese codigo del libro a eliminar: ")
    if eliminar_libro(codigo):
        print("Libro eliminado")
    else:
        print("El codigo no existe")
def main():
    while True:
        mostrar_menu()
        op = leer_opc()
        match op:
            case 1:
                op_copias_genero()
            case 2:
                op_busqueda_multa()
            case 3:
                op_actualizar_multa()
            case 4:
                op_agregar_libro()
            case 5:
                op_eliminar_libro()
            case 6:
                print("Programa finalizado")
                break
main()