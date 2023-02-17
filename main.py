import tensorflow as tf 
from tensorflow.keras.models import load_model
import os 
import matplotlib
import numpy as np 
from matplotlib import pyplot as plt 
from tkinter import *
from tkinter import filedialog, messagebox, colorchooser
import PIL  
from PIL import ImageDraw, ImageOps

mnist= tf
model = load_model(os.path.join('models','digitClassifierV3.h5'))
WIDTH, HEIGHT = 125   , 125 
center = WIDTH//2 
WHITE = (255,255,255)

#for the model the image that is taken from the gui has to be rezied to 1, 28, 28 ]
nums = ['0','1','2','3','4','5','6','7','8','9']
positions = range(len(nums))

#now need to make a gui that lets us draw and guess the images that we drew 
#thanks to this video to the gui tut: https://www.youtube.com/watch?v=x_t292uiH5Q&t=78s
class PaintCanvas : 
    def __init__(self) : 
        self.root = Tk() 
        self.root.title("HandWrittenDigitClassifier")

        self.brush_width = 2
        self.currentColor = '#FFFFFF'

        self.cnv = Canvas(self.root, width = WIDTH-10 , height = HEIGHT- 10, bg='black') 
        self.cnv.pack()
        self.cnv.bind("<B1-Motion>", self.paint)    #binds the first mouse buttong to the paint function 
        
        self.image = PIL.Image.new("L", (WIDTH, HEIGHT) ,255)
        self.draw = ImageDraw.Draw(self.image)

        #define button frame 
        self.btnFrame = Frame(self.root)
        self.btnFrame.pack(fill=X)

        #two buttons ; Clear and Guess 
        self.btnFrame.columnconfigure(0, weight=1 )
        self.btnFrame.columnconfigure(1, weight=1 )

        self.clear = Button(self.btnFrame, text ='Clear', command = self.clear)
        self.clear.grid(row=0, column=0, sticky=W+E)

        self.guess = Button(self.btnFrame, text ='Guess', command = self.guess)
        self.guess.grid(row=0, column=1, sticky=E+W)


        #run main loop 
        self.root.protocol("WM_DELETE_WINDOW", self.onClose())
        self.root.attributes("-topmost", True)
        self.root.mainloop()
    #calls when we close the program 
    def onClose(self):
        pass
    def paint(self,event): #paints whenever we hold the mouse button 
        x1 , y1 = (event.x -1 ) , (event.y -1 )
        x2 , y2 = (event.x +1 ) , (event.y +1 )
        self.cnv.create_rectangle(x1, y1, x2,y2, outline=self.currentColor, fill=self.currentColor, width = self.brush_width)
        self.draw.rectangle([x1,y1,x2+self.brush_width, y2+self.brush_width], outline=self.currentColor, fill=self.currentColor,  width=self.brush_width)

    #have the ai predict on the drawing 
    #first we have to save the image 
    #then resize 
    #then predict 
    def guess(self):
        #i think there is no need to save to an image since we can just use the image object from pil already
        snapShot = self.image.resize((28,28))
        snapShot = np.asarray(snapShot)
        snapShot = snapShot/255
        snapShot = snapShot.reshape(1,28,28)    
        

        prediction = model.predict(snapShot)
       
        predictionList = []
        plt.close()
        for i in range(10 ): 
            predictionList.append(prediction[0][i])
        plt.bar(positions, predictionList)
        plt.show()
        
        
        
    
    def clear(self):
        #could find a better way to do this in the future 
        self.cnv.delete("all")
        self.draw.rectangle([0,0,1000,1000], fill='black')



canvas = PaintCanvas()
