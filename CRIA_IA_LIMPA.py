#DECLARE USED LIBRARIES
import math
import numpy as np
import os
import csv
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense 
import matplotlib.pyplot as plt



#READ THE CSVs FILES FOR TRAINING
arquivos_csv= os.listdir('./Dados500')
index_arquivos=len(arquivos_csv)

#CREATE THE TRAINING MATRIX
contador=0 
for a in arquivos_csv:
    obj= "./Dados500/" + a
    aux=[]
    with open(obj, newline='') as file:
        reader = csv.reader(file)
        res = list(map(tuple, reader))
        for j2 in range(len(res)):
            aux.append(res[j2]) 
            
    aux1=np.array(aux)
    aji=len(aux1) 
    bji=len(aux1[0])
    matrix = np.empty(shape=(aji-1,bji),dtype='object')
    h=(aji-1, index_arquivos)
    matrix2=np.zeros(h) 

    for i in range(aji):
        if i == 0:
            print('')
        else:
            vet=aux1[i]
            for j in range(bji):
                if vet[j] == 'False': 
                    c=0
                elif vet[j] == 'True':
                    c=1
                else:
                    c = vet[j]
                matrix2[i-1][arquivos_csv.index(a)]= 1
                matrix[i-1][j]= float(c) 
    if contador:
        contador +=1
        saida=np.concatenate((saida, matrix2))
        matrix3=np.concatenate((matrix3, matrix))
    else:
        contador +=1
        saida=matrix2
        matrix3=matrix
matrix=matrix3
index_csv=len(matrix[0])

#RANDOMIZA OS DADOS
a=np.array(matrix)
b=np.array(saida)
c = np.c_[a.reshape(len(a), -1), b.reshape(len(b), -1)]
np.random.shuffle(c)
entrada3= c[:, :a.size//len(a)].reshape(a.shape)
saida3= c[:, a.size//len(a):].reshape(b.shape)

#CRIA A IA NO KERAS
entrada=np.matrix(matrix).astype(float) 
entrada1= tf.keras.utils.normalize(entrada, axis =1) 
entrada2=np.array(matrix)
saida=np.array(saida)
neuronios=18
camadas=2 
classificador = Sequential()
classificador.add(Dense(units=18, activation= 'relu', input_dim=index_csv)) 
classificador.add(Dense(units=14, activation= 'relu')) 
#classificador.add(Dense(units=neuronios, activation= 'relu'))
classificador.add(Dense(units=index_arquivos, activation= 'sigmoid')) 
classificador.compile(optimizer ='adam', loss='binary_crossentropy',metrics=['accuracy'])

#TREINA A IA
entrada3=np.matrix(entrada3).astype(float) 
entrada3= tf.keras.utils.normalize(entrada3, axis=1)
hist = classificador.fit(entrada3,saida3, 
                       validation_split=0.1,
                       verbose=1,
                       shuffle=True,
                       batch_size=4,
                       epochs=45)

# visualização com keras, acessando o conteudo do historico
print(hist.history, '\n conteudo do dictionary')
preci=hist.history['accuracy']
print(preci)
perdas=hist.history['loss']
print(perdas)

b=[i for i in range(len(preci))]

plt.plot(b, preci), plt.grid(True)
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

plt.plot(b, perdas), plt.grid(True)
plt.ylabel('Losses')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()


#SAVE MODEL
classificador.save("model.h5")

print("Saved model to disk")