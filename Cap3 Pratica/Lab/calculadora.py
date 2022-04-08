def calculo(n1, n2, o):
    if o == "1":
        return n1+n2
    elif o == "2":
        return n1-n2
    elif o == "3":
        return n1*n2
    elif o == "4":
        return n1/n2


print("**********  Python Calculator **********")
print("Selecione o número da operação desejada:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
escolha = input("Digite o número da operação desejada (1/2/3/4): ")
if(int(escolha) > 0 and int(escolha) < 5):
    nm1 = float(input("Digite o 1° número: "))
    nm2 = float(input("Digite o 2° número: "))
    operacores = ['+', '-', '*', '/']
    print("%.2f %s %.2f = %.2f" %
      (nm1, operacores[int(escolha)-1], nm2, calculo(nm1, nm2, escolha)))
else:
    print("Operação inválida!")
