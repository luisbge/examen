import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model

longitud, altura = 150, 150
modelo = './modelo/modelo.h5'
pesos_modelo = './modelo/pesos.h5'
cnn = load_model(modelo)
cnn.load_weights(pesos_modelo)

def predict(file):
  x = load_img(file, target_size=(longitud, altura))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = cnn.predict(x)
  result = array[0]
  answer = np.argmax(result)
  if answer == 0:
    print("pred: Carne 1")
  elif answer == 1:
    print("pred: Carne 2")
  elif answer == 2:
    print("pred: Carne 3")
  if answer == 3:
    print("pred: Carne 4")
  elif answer == 4:
    print("pred: Carne 5")
  elif answer == 5:
    print("pred: Carne 6")
  elif answer == 6:
    print("pred: Carne 7")
  elif answer == 7:
    print("pred: Carne 8")
  return answer
