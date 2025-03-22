#Filtrar Dados Acima de um Limite

while True:
    try:
        lista = input("insira valores de números separados por vírgula: ")
        var1 = input("insira o limite: ")


        def filtrar_dados_acima_do_limite(entrada: list, limite: int) -> list:
            limite = int(limite)
            lista_splittada = entrada.split(",")
            lista_num = list(map(int, lista_splittada))
            lista_resultado = list()
            for i in lista_num:
                if i >= limite:
                    lista_resultado.append(i)        
            return print(lista_resultado)  


        filtrar_dados_acima_do_limite(lista, var1)
        exit()
    except ValueError:
        print("Valor de entrada não suportado.")     
        