grau = float(input())

if grau == 1:
    a = float(input())
    if a == 0:
        print("A equação é do primeiro grau")
        print('Valor de a inválido')
    else:
        b = float(input())
        if b == 0:
            resul1 = 0
            print("A equação é do primeiro grau")
            print(f"{resul1:.2f}")
        else:
            resul1 = float(-b / a)
            print("A equação é do primeiro grau")
            print(f"{resul1:.2f}")
elif grau == 2:
    a = float(input())
    b = float(input())
    c = float(input())
    resul2 = b*b - 4*a*c
    if a == 0:
        print("A equação é do segundo grau")
        print("Valor de a inválido")
    elif a != 0:
        
        
        print("A equação é do segundo grau")
            
            
        
        if resul2 < 0:
            print("A equação não possui raízes reais")
        elif resul2 == 0:
            print("A equação possui apenas uma raiz real")
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