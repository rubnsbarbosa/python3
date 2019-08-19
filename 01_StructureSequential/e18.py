# 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo = float(input('Digite o tamanho do arquivo para download em MB: '))
velocidade = float(input('Digite a velocidade em Mbps: '))

# tempo para download em segundos
tempo_download = tamanho_arquivo / velocidade
# tempo para download em minutos
tempo_download = tempo_download / 60
print('O tempo aproximado de download do arquivo: {} minutos'.format(tempo_download))
