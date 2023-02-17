import tensorflow as tf 
import matplotlib
import numpy as np 
import os 
from matplotlib import pyplot as plt
from tensorflow.keras.models import Sequential , load_model
from tensorflow.keras.layers import Dense ,Flatten, Input

#tensorflow is an nn tool that allows you to use machine learning algorithms 
#keras is a wrapper for tensorflow that makes tensorflow easier to use 

# #loads the data as a numpy array
# (trainImages , trainLabels)  , (testImages , testLabels) = tf.keras.datasets.mnist.load_data() 

# #normalize data

# trainImages = trainImages/255
# testImages = testImages/255


# dumbModel = Sequential ()
# dumbModel.add(Input( trainImages.shape[1:]))
# dumbModel.add(Flatten())
# dumbModel.add(Dense(10 , activation = 'softmax')) #softmax makes all the outputs probabilities that add up to oen 
# #categorical crossentropy is the loss you typically want to be using for multiple classes
# #sparse categorical crossentropy changes the labels into one hot vectors before comparing 
# dumbModel.compile(optimizer =  'adam', loss='sparse_categorical_crossentropy',metrics = ['accuracy'])


# print(dumbModel.summary()) 

# trainLabelsOnehot = tf.one_hot(trainLabels , 10)  
# hist = dumbModel.fit(trainImages, trainLabels, epochs =10, batch_size =128 , validation_data= (testImages, testLabels)  )


# #prediction expects batch size then values for the rest 
# print(dumbModel.predict(testImages[0].reshape(1,28, 28)))

# model = Sequential()
# model.add(Input ( trainImages.shape[1:]))
# model.add(Flatten())    
# model.add(Dense(128, activation = 'relu'))
# model.add(Dense(64 , activation = 'relu'))
# model.add(Dense(10 , activation = 'softmax'))

# model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics=['accuracy'])   

# hist = model.fit(trainImages, trainLabels, epochs =10 , batch_size = 128, validation_data = (testImages, testLabels )  )

# plt.plot (hist.history['loss'], label = 'loss')
# plt.plot (hist.history['val_loss'], label = 'valLoss')

# plt.legend
# plt.show()

# plt.plot (hist.history['accuracy'], label = 'acc')
# plt.plot (hist.history['val_accuracy'], label = 'valAcc')

# plt.legend
# plt.show()
# model.save(os.path.join('models', 'digitClassifierV3.h5'))



