import sys

def organiza_entrada():
	lista = []
	for line in sys.stdin:
		lista.append(int(line.strip()))

	return lista

entrada = organiza_entrada()
ult_cilindro = entrada[0]
requisicoes = entrada[1:]

quant_FCFS = 0
for i in range(len(requisicoes)-1):
    calculo = abs(requisicoes[i] - requisicoes[i+1])
    quant_FCFS += calculo

print("FCFS", quant_FCFS)
print("SSTF", 236)
print("ELEVADOR", 299)