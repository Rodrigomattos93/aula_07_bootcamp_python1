#Calcular Média de Valores em uma Lista

while True:
    try:
        lista = input("insira valores de números separados por vírgula: ")


        def calcular_media_de_uma_lista(entrada: list) -> int:
            lista_splittada = entrada.split(",")
            lista_num = list(map(int, lista_splittada))
            media = sum(lista_num) / len(lista_num)
            return print(media)
        
        
        calcular_media_de_uma_lista(lista)
        exit()
    except ValueError:
        print("Valor de entrada não suportado.")     
        