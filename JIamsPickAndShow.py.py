#Jeremiah Iams
#CST-111
#6/8/2022
#This code was from the textbook page 72 and swapped the order of commands from myself
def DisplayAndPlay():
  PicFile = pickAFile()
  SoundFile = pickAFile()
  myLopeJPG = makePicture(PicFile)
  myLopeGrunt = makeSound(SoundFile)
  show(myLopeJPG)
  play(myLopeGrunt)