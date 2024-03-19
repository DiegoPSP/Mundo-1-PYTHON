a = 5
b = 6
nome =  'Diego'
cores = {'limpa': '\33[m',
         'azul': '\33[34m',
         'amarelo': '\33[33m',
         'pretoebranco': '\33[7;30m'}
print(f"O nome é {cores['azul']}{nome}{cores['limpa']}!!!")
print(f"Agora está assim {cores['amarelo']} {nome} {cores['limpa']}!!!")
print(f"E agora desse jeito {cores['pretoebranco']}{nome}{cores['limpa']}!!!")

print(f"Os valores são \33[0;31;40m {a} \33[m e \33[0;32;40m {b} \33[m!!!")
# Criação da tabela de cores
# \33[style;text;back m
# \33[0-1-4-7; 30/37; 40/47
