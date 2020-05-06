nome = str(input('Como se chama? '))
print('Olá, muito prazer {}!'.format(nome))
nasc = int(input('Qual é o seu ano de nascimento? '))
import datetime
idade = datetime.date.today().year - nasc
if idade < 18:
    print('{}, ainda te vais alistar no exército. Mas só daqui a {} ano(s).'.format(nome, (18-idade)))
    print('Você tem {} anos.'.format(idade))
elif idade >= 18 and idade < 30:
    print('{}, podes te alistar no exército. Ainda tens mais {} anos para inscrição'.format(nome, (30-idade)))
    print('Você tem {} anos.'.format(idade))
elif idade >= 30:
    print('{}, seu tempo de alistamento no exército ja passou há {} anos.'.format(nome, (idade-30)))
    print('Você tem {} anos.'.format(idade))
