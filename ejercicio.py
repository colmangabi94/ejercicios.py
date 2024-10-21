def ingresar_puntuacion_y_comentario():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5:')
        point = input()

        if point.isdecimal():
            point = int(point)

            if point < 1 or point > 5:
                print('Indíquelo en una escala de 1 a 5')
            else:
                print('Por favor, introduzca un comentario:')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                
                print('Puntuación y comentario guardados.')
                break
        else:
            print('Por favor, introduzca la puntuación en números.')

def comprobar_resultados():
    print('Resultados hasta la fecha:')
    try:
        with open("data.txt", "r") as read_file:
            resultados = read_file.read()
            if resultados:
                print(resultados)
            else:
                print('No hay resultados guardados aún.')
    except FileNotFoundError:
        print('No se ha encontrado el archivo de resultados.')

def finalizar_proceso():
    print('Finalizando')
    exit()

def main():
    while True:
        print('Seleccione el proceso que desea aplicar:')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprobar los resultados obtenidos hasta ahora.')
        print('3: Finalizar')
        num = input()

        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_puntuacion_y_comentario()
            elif num == 2:
                comprobar_resultados()
            elif num == 3:
                finalizar_proceso()
            else:
                print('Introduzca un número del 1 al 3')
        else:
            print('Por favor, introduzca un número del 1 al 3')

if __name__ == "__main__":
    main()