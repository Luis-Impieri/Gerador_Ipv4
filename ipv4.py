import ipaddress
import random


tipo = input('Escolha qual tipo de IPV4 irá querer')

def octetos():
 if tipo in ['A', 'B', 'C']:
     return [random.randint(1, 223), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
 elif tipo in ['D']:
     return [random.randint(224, 239), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
 elif tipo in ['E']:
     return [random.randint(240, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 254)]
 else:
     print('ERRO: escolha uma opção valida')

if tipo == 'A':
     oct1, oct2, oct3, oct4 = octetos()
     ipv4_adress = f'{oct1}.{oct2}.{oct3}.{oct4} /8'
     print("Endereço Ipv4 tipo A: ", ipv4_adress)

elif tipo == 'B':
     oct1, oct2, oct3, oct4 = octetos()
     ipv4_adress = f'{oct1}.{oct2}.{oct3}.{oct4} /16'
     print("Endereço Ipv4 tipo B: ", ipv4_adress)

elif tipo == 'C':
     oct1, oct2, oct3, oct4 = octetos()
     ipv4_adress = f'{oct1}.{oct2}.{oct3}.{oct4} /24'
     print("Endereço Ipv4 tipo C: ", ipv4_adress)

elif tipo == 'D':
     oct1, oct2, oct3, oct4 = octetos()
     ipv4_adress = f'{oct1}.{oct2}.{oct3}.{oct4} /32'
     print("Endereço Ipv4 tipo D: ", ipv4_adress)

elif tipo == 'E':
    oct1, oct2, oct3, oct4 = octetos()
    ipv4_adress = f'{oct1}.{oct2}.{oct3}.{oct4} /32'
    print("Endereço Ipv4 do tipo E: ", ipv4_adress)
else:
     print('Escolha uma opção valida')
