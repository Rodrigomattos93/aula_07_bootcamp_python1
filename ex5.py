#Calcular o desvio padrão de uma lista

while True:
    try:
        lista = input("insira valores de números separados por vírgula: ")


        def calcular_desvio_padrao_de_uma_lista(entrada: list) -> int:
            lista_splittada = entrada.split(",")
            lista_num = list(map(int, lista_splittada))
            numerador_final = 0
            media = sum(lista_num) / len(lista_num)

            for i in lista_num:
                numerador = (i - media)**2
                numerador_final = numerador_final + numerador
            
            dv = (numerador_final/len(lista_num))**0.5
            
            return print(dv)
        
        
        calcular_desvio_padrao_de_uma_lista(lista)
        exit()
    except ValueError:
        print("Valor de entrada não suportado.")     
        