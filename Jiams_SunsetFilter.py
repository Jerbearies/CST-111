#Week 2 - Jeremiah Iams
#CST-111
#6/15/2022
#Code from different pages of chapter 4 of our textbook and Professor Zupan's example.

def getPic():
  file = pickAFile()
  pic = makePicture(file)
  SunsetFilter(pic)
  show(pic)
  
def SunsetFilter(picture):
  lessBlue(picture)
  lessGreen(picture)
  
def lessBlue(picture):
  for pixel in getPixels(picture):
    rgbvalue=getBlue(pixel)
    setBlue(pixel,rgbvalue*0.7)
    
def lessGreen(picture):
  for pixel in getPixels(picture):
    rgbvalue=getGreen(pixel)
    setGreen(pixel,rgbvalue*0.7)

