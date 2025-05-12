#algoritmos de ordenamiento

def bubble_sort(array):
    #ordenamiento que compara elementos consecutivos y los intercambia si estan en orden incorrecto
    n = len(array)
    for i in range(n):
        for j in range(n-i-1): #para reducir iteraciones
            if array[j] > array[j+1]:
                array[j], array[j+1]= array[j+1], array[j]
    return array

def selection_sort(array):
    #ordenamiento secuencial: selecciona al menor y lo pone al inicio.
    n=len(array)
    for i in range(n):
        min_index= i
        for j in range(i+1,n):
            if array[j] < array[min_index]: #si se encuentra un número mas pequeño se actualiza
                min_index = j
        array[min_index], array[i] = array[i], array[min_index] #intercambio
    return array

def quick_sort(array):
    #mediante recursión compara el de la mitad con los menores y mayoress, luego al unirse, usa la misma función para ordenarlos
    if len(array)<=1:
        return array
    pivot= array[len(array)//2]
    menores= [x for x in array if x < pivot]
    iguales= [x for x in array if x == pivot]
    mayores = [x for x in array if x > pivot]
    return quick_sort(menores) + [pivot] + quick_sort(mayores)
#menu interactivo
def menu():
    print("\n===== MENÚ DE ORDENAMIENTO =====")
    print("1. Método Burbuja")
    print("2. Método Secuencial")
    print("3. Método Quicksort")
    print("4. Salir")
#función principal
def main():
    while True:
        menu()
        opcion= input("Seleccione una opcion del 1-4: ")
        if opcion=="4":
            print("Adios...")
            break
        entrada = input("Ingrese una lista de números separados por comas: ")
        numeros = list(map(int, entrada.split(",")))
        if opcion == "1":
            bubble_sort(numeros)
            print("Ordenado con Burbuja:", numeros)
        elif opcion == "2":
            selection_sort(numeros)
            print("Ordenado con Secuencial:", numeros)
        elif opcion == "3":
            resultado = quick_sort(numeros)
            print("Ordenado con Quicksort:", resultado)
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__=="__main__":
    main()


