from sklearn import tree
import time

inicio = time.time()
x = 0
hits = 0
MODERADO = 0
ALTO = 1
MUITOALTO = 2

#vetor de Alerta Emitido 2018 como base de treino
vetorDesastre = [[85,24,50,1],[223,24,52,1],[84,48,78,24],[51,1,150,96],
                 [78,1,177,24],[92,24,88,3],[30,1,263,96],[39,1,93,24],
                 [55,1,123,24],[25,1,74,24],[68,24,155,48]]

resultado = [MODERADO,ALTO,MODERADO,ALTO,ALTO,MODERADO,ALTO,MODERADO,
             ALTO,MODERADO,MODERADO]

#vetor de Alerta Emitido 2017 com base de teste
listAlertaEmitidos = [[80,24,154,96],[44,1,63,3],
                 [79,24,18,1],[80,96,41,1],[168,6,30,1],[170,72,29,1],
                 [92,72,39,1],[50,1,70,3],[125,72,40,1],[142,72,104,48],
                 [69,24,176,96]]
ResultadoAlerta = [ALTO,MODERADO,MODERADO,MODERADO,ALTO,MUITOALTO,
                   MODERADO,MODERADO,MODERADO,ALTO,MODERADO]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(vetorDesastre, resultado)

elementos_lista = len(listAlertaEmitidos)
while(x < elementos_lista):
 resultadoAlerta = clf.predict([listAlertaEmitidos[x]])
 print(ResultadoAlerta[x])

 if resultadoAlerta == ResultadoAlerta[x]:
  hits+=1
 if resultadoAlerta == 0:
        print('Alerta Moderado')
 elif resultadoAlerta == 1:
        print('Alerta Alto')
 else:
        print('Alerta Muito Alto')   
 x+=1

print('Acuracia')
print((100*hits)/len(ResultadoAlerta))
print('Tempo de execucao')
fim = time.time()
print(fim - inicio)
  


