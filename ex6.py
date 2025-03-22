#Encontrar Valores Ausentes em uma Sequência

while True:
    try:
        lista = input("insira valores de números separados por vírgula: ")


        def calcular_valores_ausentes_numa_sequencia(entrada: list) -> list:
            lista_splittada = entrada.split(",")
            lista_num = list(map(int, lista_splittada))
            min_lista_num = min(lista_num)
            max_lista_num = max(lista_num)
            lista_sequencia = list(range(min_lista_num, max_lista_num+1))
            lista_final = list(set(lista_sequencia) - set(lista_num))
            return print(lista_final)
        
        
        calcular_valores_ausentes_numa_sequencia(lista)
        exit()
    except ValueError:
        print("Valor de entrada não suportado.")     
        