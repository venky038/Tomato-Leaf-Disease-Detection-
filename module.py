import tensorflow as tf
from tensorflow.keras.models import load_model, model_from_json
from tensorflow.keras.preprocessing.image import load_img , img_to_array
from PIL import Image,ImageTk,ImageDraw,ImageFont
import PIL
import brisque
import numpy as np
import cv2
print(tf.__version__)

def imageQuality(file_path1):
    img = PIL.Image.open(file_path1)
    return brisque.score(img)

def output(location):
    img = load_img(location, target_size=(256, 256, 3))
    img = img_to_array(img)
    # img=img/255
    img = np.expand_dims(img, [0])
    answer = model.predict(img)
    # print(answer,lab)

    y_class = answer.argmax(axis=-1)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = class_names[y]
    # print(class_names[y])
    t=class_names.index(str(res))
    if (answer.max() * 100 < 70):
        print('healthy But \n')
    print("In module....")
    if(t==9):
        t=3
    if(t>2 and t!=9):
        t-=1
    print(t)
    return str(res),str(answer.max() * 100),t

model = tf.keras.models.load_model(
    "C:/Users/AJAY KUMAR/project/model.h5",
    custom_objects={'Functional':tf.keras.models.Model})

from tensorflow.keras.preprocessing.image import load_img,img_to_array

val_ds=tf.keras.preprocessing.image_dataset_from_directory(
    "C:/Users/AJAY KUMAR/project/val",
    shuffle=True,
    image_size=(256,256),
    batch_size=32
)

class_names= val_ds.class_names


print(class_names)


img='C:/Users/AJAY KUMAR/Downloads/pic2.jpg'
