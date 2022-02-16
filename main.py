import csv

#Função para encontrar o estado de início correto 
def percorre():
  i=0
  aux=0
  while (lista[i]) == '_':
    i=i+1
    aux=i 
  
  for x in range(len(estados)):
    if estados[x] == 'inic' and str(lido[x]) == str(lista[i]):
      return x,i,aux 

#Função para percorrer os índices
def indice(a,j):
  for x in range(len(estados)):
        if estados[x] == a and lido[x] == lista[j]:          
          return x
           
#Função para computar a MT  
def turing(a,j,aux):   
 print(lista) 
 accept = 'halt-accept'
 
 if str(vai[int(a)]) != str(accept):   
   if str(lido[int(a)]) == str(lista[j]):
     lista[j] = escrito[int(a)]     
     if direcao[int(a)] == 'r':
       j=j+1
       if j <= tam//2:
        salvar.append([int(a), lido[a], escrito[a], 'l', vai[a]])
        lista.insert(0,"_")
        lista.pop()  
        for w in range(1,len(lista)):
          if  lista[-w] == '_':
              pass
          else: break
        for z in range (w,len(lista),1):
          if lista[-z] == salvar[-1][1]:
            lista[-z] = salvar[-1][2]
            sequencia.append(salvar[-1])
            if turing(salvar[-1][0],len(lista)-z,aux) :
              return True
        aux = j+1
       aux = j   
       a = indice(vai[a],aux)
       sequencia.append([estados[a], lido[a], escrito[a], direcao[a], vai[a]])
       if turing(a, j,aux):
         return True
     
     elif direcao[int(a)] == 'l':
       j=j-1
       if j <= tam//2:
        salvar.append([int(a), lido[a], escrito[a], 'l', vai[a]])
        lista.insert(0,"_")
        lista.pop()
        for w in range(1,len(lista)):
          if  lista[-w] == '_':
              pass
          else: break
        for z in range (w,len(lista),1):
          if lista[-z] == salvar[-1][1]:
            lista[-z] = salvar[-1][2]            
            sequencia.append(salvar[-1])
            if turing(salvar[-1][0],len(lista)-z,aux):
              return True      
       aux=j
       a = indice(vai[a],aux)
       sequencia.append([estados[a], lido[a], escrito[a], direcao[a], vai[a]])
       if turing(a, j,aux):
         return True 
       
     elif direcao[int(a)] == '*':
      if j <= tam//2:
       salvar.append([int(a), lido[a], escrito[a], 'l', vai[a]])
       lista.insert(0,"_")
       lista.pop()
       for w in range(1,len(lista)):
         if  lista[-w] == '_':
             pass
         else: break
       for z in range (w,len(lista),1):
         if lista[-z] == salvar[-1][1]:
           lista[-z] = salvar[-1][2]            
           sequencia.append(salvar[-1])
           if turing(salvar[-1][0],len(lista)-z,aux):
             return True
       aux = j+1     
      aux=j
      a = indice(vai[a],aux)
      sequencia.append([estados[a], lido[a], escrito[a], direcao[a], vai[a]])
      if turing(a, j,aux):
        return True                
   else:     
     return False  
 return True
     
 
if __name__=="__main__": 

 #Cria listas
 estados = []
 lido = []
 escrito = []
 direcao = []
 vai = [] 
 salvar = []
 sequencia = []
 configuracao_final = []

#Lê arquivo .in com csv
#sameamount10
 with open('sameamount10.in') as csv_file:
     entrada = csv.reader(csv_file, delimiter=' ')
     for linha in entrada:
       estados.append(linha[0])
       lido.append(linha[1])
       escrito.append(linha[2])
       direcao.append(linha[3])
       vai.append(linha[4])
 
 #Muda nome do estado '0'
 for y in range(len(estados)):
   if estados[y] == '0':
     estados[y] = 'inic'
   if vai[y] == '0':
     vai[y] = 'inic'
 
 #Insere o input da fita,  criando uma fita "infinita" com a variável tam   
 tam = 14
 lista = ['_' for i in range (tam)]
 lista.insert(tam//2,'1')
 lista.insert(1+tam//2,'0')
 #lista.insert(2+tam//2,'1')
 #lista.insert(3+tam//2,'0')
 
 #Recebe os indices do estado inicial que fara a leitura da primeira célula da fita
 x,i,aux = percorre()
 print("Accept" if turing(x,i,aux) else "Reject")

 #A lista 'salvar' guarda as configurações que tentaram passar pelo marcador de início da fita
 #print(salvar) 
 



 #Agora começará "tradução" em si
 
 
 #Insere estados de subrotinas de troca de símbolos, espaço à direita, retorno de fita 
 est = ['0', '0', 'um', 'um', 'um', 'zero', 'zero', 'zero', 'volta', 'volta', 'volta','volta', 'esp', 'esp']
 lid = ['1', '0', '1','0','_','1','0','_','1','0','_','S','1','0']
 esc = ['S', 'S', '1','1','1','0','0','0','1','0','_','S','_','_']
 dir = ['r', 'r', 'r','r','l','r','r','l','l','l','r','r','r','r']
 go =  ['um','zero','um','zero','volta','um','zero','volta','volta','volta','inic','esp','um','zero']
 simbolos = ['%','&','@','!','+','/']



 #Insere as configuraçoes salvas e subrotinas necessárias para a adaptação 
 for i in range(len(salvar)):
   estados.append('volta')
   lido.append(simbolos[i])
   escrito.append("_")
   direcao.append('*')
   vai.append(salvar[i][0])

   est.append('esp')
   lid.append(simbolos[i])
   esc.append('_')
   dir.append('r')
   go.append(simbolos[i])

   est.append('#')
   lid.append(simbolos[i])
   esc.append('_')
   dir.append('*')
   go.append(salvar[i][0])

   escrito[salvar[i][0]] = simbolos[i]
   direcao[salvar[i][0]] = '*'
   vai[salvar[i][0]] = '#'

   #Insere os estados criados para salvar as configurações 
   configuracao_final.append(salvar[i])
  
 # Insere os novos estados na configuração anterior
 for i in range(len(est)):
   estados.append(est[i])
   lido.append(lid[i])
   escrito.append(esc[i])
   direcao.append(dir[i])
   vai.append(go[i])

#Insere os estados para a MT com fita semi-infinita
for i in range(len(estados)):
  configuracao_final.append([estados[i], lido[i], escrito[i], direcao[i], vai[i]]) 

#Cria o aquivo .out
with open('traduzida.out', 'w') as txt:
    for item in configuracao_final:
        txt.write("%s %s %s %s %s \n" % (item[0],item[1],item[2],item[3],item[4]))   

