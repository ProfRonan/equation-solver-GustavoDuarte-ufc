grau = float(input())

#Equação do primeiro grau
if grau == 1:
    print("A equação é do primeiro grau")
    a = float(input())

    if a == 0:
        print('Valor de a inválido')
    else:
        b = float(input())
        
        if b == 0:
            resul1 = 0
            print("A equação é do primeiro grau",f"{resul1:.2f}")
        else:
            resul1 = float(-b / a)
            print("A equação é do primeiro grau",f"{resul1:.2f}")

#Equação do segundo grau
elif grau == 2:
    print("A equação é do segundo grau")
    a = float(input())

    if a == 0:
        print("Valor de a inválido")
    elif a != 0:
        print("A equação é do segundo grau")
        b = float(input())
        c = float(input())
        resul2 = b*b - 4*a*c
            
        if resul2 < 0:
            print("A equação não possui raízes reais")
        elif resul2 == 0:
            print("A equação possui uma raiz real")
            if b == 0 or a == 0:
                x1 = 0
                print(f"{x1:.2f}")
            else:
                x1 = -b / 2 * a
                print(f"{x1:.2f}")

        elif resul2 > 0:
            print("A equação possui duas raízes reais")
            x1 = -b + resul2**(0.5) / 2 * a
            x2 = -b - resul2**(0.5) / 2 * a

            if c == 0 and b != 0 and a != 0:
                
                x1 = 0
                x2 = -b / a
                if x1 < x2:
                    print(f"{x1:.2f} e {x2:.2f}")
                else:
                    print(f"{x2:.2f} e {x1:.2f}")
        
            elif a != 0 and c != 0 and b == 0:
            
                calc = -c / a
                x1 = -calc**(0.5)
                x2 = calc**(0.5)
                if x1 < x2:
                    print(f"{x1:.2f} e {x2:.2f}")
                else:
                    print(f"{x2:.2f} e {x1:.2f}")

else:
    print("Grau inválido")     