grau = float(input())

if grau == 1:
    
    if a == 0:
        print('Valor de a inválido')
    else:
        b = float(input())
        resul1 = -b / a
        print(f"{resul1:.2f}")
elif grau == 2:
    a = float(input())
    if a != 0:
        b = float(input())
        c = float(input())
        resul2 = b*b - 4*a*c
        if resul2 < 0:
            print("A equação não possui raízes reais")
        elif resul2 == 0:
            print("A equação possui apenas uma raiz real")
            resul3 = -b / 2*a
            print(f"{resul3:.2f}")
        elif resul2 > 0:
            x1 = -b + resul2**(0.5) / 2*a
            x2 = -b - resul2**(0.5) / 2*a
            print(f"{x1:.2f} e {x2:.2f}") 

else:
    print("Grau inválido")     