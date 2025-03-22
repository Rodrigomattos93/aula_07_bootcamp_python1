#Contar Valores Únicos em uma Lista

while True:
    try:
        lista = input("insira valores separados por vírgula: ")


        def contar_valores_unicos_numa_lista(entrada: list) -> int:
            dicionario = dict()
            lista_splittada = entrada.split(",")
            lista_final = list()
            for i in lista_splittada:
                if i in dicionario.keys():
                    dicionario[i] = dicionario[i] + 1
                else:
                    dicionario[i] = 1
            
            for k, v in dicionario.items():
                if v == 1:
                    lista_final.append(k)
                else:
                    pass
            
            return print(len(lista_final))
        
        def contar_valores_unicos_numa_lista_simplificado(entrada: list) -> int:
            lista_splittada = entrada.split(",")
            lista_final = len(set(lista_splittada))
            return print(lista_final)
        
        
        contar_valores_unicos_numa_lista(lista)
        contar_valores_unicos_numa_lista_simplificado(lista)
        exit()
    except ValueError:
        print("Valor de entrada não suportado.")     
        