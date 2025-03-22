#Converter Celsius para Fahrenheit em uma Lista

#Calcular Média de Valores em uma Lista

while True:
    try:
        lista = input("insira valores de temperatura em Celsius separados por vírgula: ")


        def converter_de_celsius_para_fahrenheit(entrada: list) -> list:
            lista_splittada = entrada.split(",")
            lista_num = list(map(int, lista_splittada))
            for i in range(0,len(lista_num)):
                lista_num[i] = lista_num[i] * 1.8 + 32

            return print(lista_num)
        
        
        converter_de_celsius_para_fahrenheit(lista)
        exit()
    except ValueError:
        print("Valor de entrada não suportado.")     
        