import sys

def organiza_entrada():
	lista = []
	for line in sys.stdin:
		lista.append(int(line.strip()))

	return lista

entrada = organiza_entrada()
ult_cilindro = entrada[0]
requisicoes = entrada[1:]

# --------------------------------------- FCFS ------------------------------------------------

quant_FCFS = 0
for i in range(len(requisicoes)-1):
	# Cálculo da distância de requisições sequenciais
    calculo = abs(requisicoes[i] - requisicoes[i+1])
    quant_FCFS += calculo

print("FCFS", quant_FCFS)
del quant_FCFS

quant_SSTF = 0

# --------------------------------------- SSTF ------------------------------------------------

requi_SSTF = requisicoes.copy()
head = requi_SSTF[0] # Posição da cabeça de leitura

for i in range(len(requisicoes)-1):
	# Calcula lista das distâncias do cilindro onde está a cabeça de leitura para os outros cilindros
	candidatos = [abs(head-x) for x in requi_SSTF if x != head]
																
	candidato = min(candidatos) # O candidato escolhido é o que estiver mais próximo
	ind_cand = candidatos.index(candidato)

	quant_SSTF += candidato # Incrementa a distância da cabeça para o candidato escolhido

	requi_SSTF.remove(head) # Remove da lista a requisição já analisada
	head = requi_SSTF[ind_cand] # Atualiza a posição da cabeça de leitura

print("SSTF", quant_SSTF)
del quant_SSTF, requi_SSTF, head

# -------------------------------------- ELEVADOR ------------------------------------------------

requi_ELEVADOR = requisicoes.copy()
head = requi_ELEVADOR[0] # Posição da cabeça de leitura

requi_ELEVADOR.sort()

# Cálculo da movimentação total da cabeça de leitura
quant_ELEVADOR = abs(head-requi_ELEVADOR[-1]) + (requi_ELEVADOR[-1]-requi_ELEVADOR[0])
																					 
print("ELEVADOR", quant_ELEVADOR)
del entrada, ult_cilindro, requisicoes, requi_ELEVADOR, head, quant_ELEVADOR