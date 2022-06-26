'''
This file includes all the graphics and UI (modes, buttons, user input, etc.) for my program, Jam and Jelly
This is the file that should be run!
'''

from cmu_112_graphics import *
import random
from rando import *

#setup/names of modes adapted from 112 course notes: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#usingModes
##########################################
# Splash Screen Mode
##########################################

def splashScreenMode_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.image))
    canvas.create_text(app.width/2, app.height/3, text = "Jam and Jelly Playlist Maker", font = font, fill = app.sGreen)
    canvas.create_text(app.width/2, app.height/2, text = "press any button to start!", font = 'Arial 13 bold', fill = app.sGreen)

def splashScreenMode_keyPressed(app, event):
    app.mode = 'introMode'

##########################################
# New Splash Mode
##########################################

def newSplashMode_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.image))
    canvas.create_text(app.width/2, app.height/3, text = "Jam and Jelly Playlist Maker", font = font, fill = app.sGreen)
    canvas.create_text(app.width/2, app.height/3 + 60, text = "you now have options!", font = app.medFont, fill = app.sGreen)
    canvas.create_text(app.width/2, app.height/3 + 100, text = "the left button generates a playlist for you based on your last created playlist", font = app.medFont, fill = app.sGreen)
    canvas.create_text(app.width/2, app.height/3 + 140, text = "the right button allows you to make/edit your own playlist again", font = app.medFont, fill = app.sGreen)
    
    canvas.create_rectangle(325, 400, 475, 450, width = 3, fill = app.sGreen)
    canvas.create_text(400, 425, text = "generate", font = app.sFont, fill = "black")

    canvas.create_rectangle(725, 400, 875, 450, width = 3, fill = app.sGreen)
    canvas.create_text(800, 425, text = "proceed without", font = app.sFont, fill = "black")

def newSplashMode_mousePressed(app, event):
  app.cx = event.x
  app.cy = event.y
  if (325 < app.cx < 475 and 400 < app.cy < 450):
    print("left")
    app.list = makeGraph(app.list)
    print(app.list)
    app.mode = "ranMode"

  elif(725 < app.cx < 875 and 400 < app.cy < 450):
    print("right")
    app.artistList = []
    app.list = []
    app.data = []
    app.mode = "introMode"

##########################################
# Random Mode
##########################################
def ranMode_redrawAll(app, canvas):

 #snapshot code cited from 112 course notes: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#getAndSaveSnapshot
  canvas.create_text(110, 20, text='press s to save snapshot', font = app.sFont, fill = app.sGreen)
  canvas.create_text(app.width/2, 30, text = f"randomized {app.data[0]} playlist!", font = app.font, fill = app.sGreen)
  if (app.data[3] == 10):
    dif = 35
    for i in range(len(app.list)):
      x, y = app.list[i]
      canvas.create_text(app.width/20, (i*dif) + 100, text = i+1, font = app.mFont)
      canvas.create_text(app.width/3.5 + 40, (i*dif) + 100, text = x, font = app.mFont)
      canvas.create_text(app.width/2 + 300, (i*dif) + 100, text = y, font = app.mFont)

  elif(app.data[3] == 18):
    dif = 20
    for i in range(len(app.list)):
      x, y = app.list[i]
      canvas.create_text(app.width/20, (i*dif)+80, text = i+1, font = app.medFont)
      canvas.create_text(app.width/3.5, (i*dif)+80, text = x, font = app.medFont)
      canvas.create_text(app.width/2 + 300, (i*dif)+80, text = y, font = app.medFont)

  else:
    dif = 16
    for i in range(len(app.list)):
        x, y = app.list[i]
        canvas.create_text(app.width/20, (i*dif)+60, text = i + 1, font = app.tFont)
        canvas.create_text(app.width/3.5, (i*dif)+60, text = x, font = app.tFont)
        canvas.create_text(app.width/2 + 300, (i*dif)+60, text = y, font = app.tFont)
    
  canvas.create_rectangle(100, 500, 250, 550, width = 3)
  canvas.create_text(175, 525, text = "randomize", font = app.sFont, fill = app.sGreen)

  canvas.create_rectangle(300, 500, 550, 550, width = 3)
  canvas.create_text(425, 480, text = "move songs:", font = app.sFont, fill = app.sGreen)

  canvas.create_rectangle(300, 560, 550, 580, width = 3)
  canvas.create_text(425, 570, text = "update", font = app.sFont, fill = app.sGreen)

  canvas.create_rectangle(650, 500, 900, 550, width = 3)
  canvas.create_text(775, 480, text = "delete songs:", font = app.sFont, fill = app.sGreen)

  canvas.create_rectangle(650, 560, 900, 580, width = 3)
  canvas.create_text(775, 570, text = "update", font = app.sFont, fill = app.sGreen)

  canvas.create_rectangle(950, 500, 1100, 550, width = 3)
  canvas.create_text(1025, 525, text = "next", font = app.sFont, fill = app.sGreen)

  if (app.songToMove != 0):
    canvas.create_text(425, 525, text=f"{app.songToMove} {app.newSpot}" , font = app.font, fill = app.sGreen)
  if (app.delete != 0):
    canvas.create_text(775, 525, text=f"{app.delete}" , font = app.font, fill = app.sGreen)

def ranMode_mousePressed(app, event):
  app.cx = event.x
  app.cy = event.y
  if (100 < app.cx < 250 and 500 < app.cy < 550):
      random.shuffle(app.list)
      app.orLen = len(app.list)

  elif (300 < app.cx < 550 and 500 < app.cy < 550): #change orders
    print("bout to change order")
    app.changeOrder = True
    app.deleteSong = False

  elif(650 < app.cx < 900 and 500 < app.cy < 550):
    print("bout to delete songs")
    app.changeOrder = False
    app.toDel = True
  
  elif (300 < app.cx < 550 and 560 < app.cy < 580): #left update button pressed 
    if (app.secondVal and (0 < app.songToMove <= len(app.list)) and (0 < app.newSpot <= len(app.list))):
      currSong = app.list[app.songToMove - 1]
      app.list.pop(app.songToMove - 1)
      app.list.insert(app.newSpot - 1, currSong)
    app.songToMove = 0
    app.newSpot = 0
    app.firstVal = True
    app.secondVal = False
    app.firstDig = 0
    app.secondDig = 0
    app.delList = []  

  elif(650 < app.cx < 900 and 560 < app.cy < 580): #right update button pressed
    app.toDel = False
    if (0 < app.delete <= len(app.list)):
      app.delList.append(app.list.pop(app.delete - 1))
      app.list = makeList(app.data[0], app.data[1], app.data[2], app.data[3], app.list, app.delList, [], [], [], [], app.data[3], 50, 1)
    app.delete = 0
    app.delTen = 0

  elif (950 < app.cx < 1100 and 500 < app.cy < 550): #next button pressed - "restart" app
    if (app.songToMove == 0 and app.newSpot == 0 and app.delete == 0):
      app.mode = 'newSplashMode'

def ranMode_keyPressed(app, event):
    acceptedVals = "abcdefghijklmnopqrstuvwxyz1234567890"
    nums = "1234567890"

    #snapshot code cited from cmu 112 course notes: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#getAndSaveSnapshot
    if (event.key == 's'):
        app.saveSnapshot()

    #checking "delete songs" part
    print(app.toDel, event.key in nums)
    if (app.toDel and event.key in nums):
        app.delete = app.delete*(10**app.delTen) + int(event.key)
        app.delTen += 1

    #checking move songs condition
    if(event.key in acceptedVals and app.changeOrder):
      if (app.firstVal and event.key in nums):
        app.songToMove = app.songToMove*(10**app.firstDig) + int(event.key)
        if (app.songToMove > len(app.list)):
          app.leftValid = False
        else:
          app.leftValid = True
        app.firstDig += 1
        #print(f"song moving: {app.songToMove}")
      elif(app.secondVal and event.key in nums):
        app.newSpot = app.newSpot*(10**app.secondDig) + int(event.key)
        app.secondDig += 1

        if (app.newSpot > len(app.list)):
          app.leftValid = False
        else:
          app.leftValid = True
        #print(f"new spot: {app.newSpot}")

    elif(event.key == "Space" and app.changeOrder):
      app.firstVal = False
      app.secondVal = True

##########################################
# Intro Mode
##########################################

def introMode_redrawAll(app, canvas):
  canvas.create_text(app.width/2,  100, text = "welcome! excited for us to craft a playlist?!", font = app.medFont)
  canvas.create_text(app.width/2,  160, text = "we'll make it based on three factors: artist, genre, and mood", font = app.medFont)
  canvas.create_text(app.width/2,  220, text = "please enter or select only one of each", font = app.medFont)
  canvas.create_text(app.width/2,  280, text = "when you get to the playlist display page, you must click inside the textbox before typing songs to move/delete", font = app.medFont)
  canvas.create_text(app.width/2,  340, text = "correct format for moving songs is: 'song to move' ~a space~ and then 'new location'", font = app.medFont)
  canvas.create_text(app.width/2,  400, text = "for example: '10 1' moves song at position 10 to position 1", font = app.medFont)
  canvas.create_text(app.width/2,  460, text = "to delete, simply type the index of the song to delete and we'll regenerate a new one for you!", font = app.medFont)
  canvas.create_text(app.width/2,  520, text = "press any button to proceed", font = app.medFont)

def introMode_keyPressed(app, event):
  app.mode = 'artistMode'

##########################################
# Artist Mode
##########################################

def artistMode_redrawAll(app, canvas):
  font = 'Arial 24 bold'
  canvas.create_text(app.width/2, 100, text = "fav artist?", font = app.font)
  canvas.create_rectangle(200, 200, 1000, 300, fill = "white", width = 3)


  canvas.create_rectangle(325, 500, 475, 550, width = 3, fill = "white")
  canvas.create_text(400, 525, text = "back", font = app.sFont, fill = app.sGreen)

  canvas.create_rectangle(725, 500, 875, 550, width = 3, fill = "white")
  canvas.create_text(800, 525, text = "next", font = app.sFont, fill = app.sGreen)

  canvas.create_text(app.width/2,  250, text=app.artistList, font = app.font, fill = app.sGreen)
  print(app.artistList)

def artistMode_mousePressed(app, event):
  app.cx = event.x
  app.cy = event.y

  if (325 < app.cx < 475 and 500 < app.cy < 550):
    app.data.pop()
    app.mode = 'introMode'

  elif(725 < app.cx < 875 and 500 < app.cy < 550):
    app.artistPage = True
    artist = ""
    for i in app.artistList:
      artist += i
    if (artist != ""):
      app.data.append(artist)
      app.mode = 'genreMode'

def artistMode_keyPressed(app, event):
    acceptedVals = "abcdefghijklmnopqrstuvwxyz1234567890"
    if(event.key in acceptedVals):
      app.artistList+=event.key
    elif(event.key == 'Backspace' or event.key == 'Delete'):
      if (len(app.artistList) > 0):
        app.artistList.pop()

##########################################
# Genre Mode
##########################################

#pop, electronic, hip hop, Country, Rock, classical, indie, k-pop, latin

def genreMode_redrawAll(app, canvas):
  canvas.create_text(app.width/2, app.height/7, text = "fav genre?", font = app.font)
  canvas.create_text(app.width/2, app.height/7 + 40, text = "pick one", font = app.sFont)
  #row 1
  if (app.kPSelect):
    canvas.create_rectangle(50, 200, 250, 300, width = app.bold, fill = app.sGreen)
  else:
    canvas.create_rectangle(50, 200, 250, 300, width = app.narrow)
  canvas.create_text(150, 250, text = "k-pop", font = app.font)

  if (app.latSelect):
    canvas.create_rectangle(350, 200, 550, 300, width = app.bold, fill = app.sGreen)
  else: 
    canvas.create_rectangle(350, 200, 550, 300, width = app.narrow)
  canvas.create_text(450, 250, text = "latin", font = app.font)

  if (app.indieSelect):
    canvas.create_rectangle(650, 200, 850, 300, width = app.bold, fill = app.sGreen)
  else: 
    canvas.create_rectangle(650, 200, 850, 300, width = app.narrow)
  canvas.create_text(750, 250, text = "indie", font = app.font)

  if (app.classSelect):
    canvas.create_rectangle(950, 200, 1150, 300, width = app.bold, fill = app.sGreen)
  else: 
    canvas.create_rectangle(950, 200, 1150, 300, width = app.narrow)
  canvas.create_text(1050, 250, text = "classical", font = app.font)

  #row 2
  if (app.pSelect):
    canvas.create_rectangle(50, 350, 250, 450, width = app.bold, fill = app.sGreen)
  else: 
    canvas.create_rectangle(50, 350, 250, 450, width = app.narrow)
  canvas.create_text(150, 400, text = "pop", font = app.font)

  if (app.eSelect):
    canvas.create_rectangle(350, 350, 550, 450, width = app.bold, fill = app.sGreen)
  else:
    canvas.create_rectangle(350, 350, 550, 450, width = app.narrow)
  canvas.create_text(450, 400, text = "electronic", font = app.font)

  if (app.hSelect):
    canvas.create_rectangle(650, 350, 850, 450, width = app.bold, fill = app.sGreen)
  else:
    canvas.create_rectangle(650, 350, 850, 450, width = app.narrow)
  canvas.create_text(750, 400, text = "hip hop", font = app.font)

  if (app.countrySelect):
    canvas.create_rectangle(950, 350, 1150, 450, width = app.bold, fill = app.sGreen)
  else:
    canvas.create_rectangle(950, 350, 1150, 450, width = app.narrow)
  canvas.create_text(1050, 400, text = "country", font = app.font)

  canvas.create_rectangle(325, 500, 475, 550, width = 3)
  canvas.create_text(400, 525, text = "back", font = app.sFont, fill = app.sGreen)

  canvas.create_rectangle(725, 500, 875, 550, width = 3)
  canvas.create_text(800, 525, text = "next", font = app.sFont, fill = app.sGreen)

def genreMode_mousePressed(app, event):
  app.cx = event.x
  app.cy = event.y

  if (50 < app.cx < 250 and 200 < app.cy < 300):
    app.kPSelect = not app.kPSelect
  elif (350 < app.cx < 550 and 200 < app.cy < 300):
    app.latSelect = not app.latSelect
  elif (650 < app.cx < 850 and 200 < app.cy < 300):
    app.indieSelect = not app.indieSelect
  elif (950 < app.cx < 1150 and 200 < app.cy < 300):
    app.classSelect = not app.classSelect
  elif (50 < app.cx < 250 and 350 < app.cy < 450):
    app.pSelect = not app.pSelect
  elif (350 < app.cx < 550 and 350 < app.cy < 450):
    app.eSelect = not app.eSelect
  elif (650 < app.cx < 850 and 350 < app.cy < 450):
    app.hSelect = not app.hSelect
  elif (950 < app.cx < 1150 and 350 < app.cy < 450):
    app.countrySelect = not app.countrySelect

  app.genres = [app.kPSelect, app.latSelect, app.indieSelect, app.classSelect, app.pSelect,
  app.eSelect, app.hSelect, app.countrySelect]
  print(app.genres)

  if (325 < app.cx < 475 and 500 < app.cy < 550):
    app.data.pop()
    print(app.data)
    app.mode = 'artistMode'

  elif(725 < app.cx < 875 and 500 < app.cy < 550):
    trueCount = app.genres.count(True)
    list = ["kpop", "latin", "indie", "classical", "pop", "electronic", "hiphop", "country"]
    if (trueCount == 1):
      c = 0
      for x in range(len(app.genres)):
        if (app.genres[x]):
          selectGenre = list[c]
        c += 1

      app.data.append(selectGenre)
      print(app.data)
      app.genrePage = True
      app.mode = 'moodMode'

##########################################
# Mood Mode
##########################################

#happy, sad, study, angry, workout, party, holiday spirit

def moodMode_redrawAll(app, canvas):
  canvas.create_text(app.width/2, app.height/7, text = "how ya feelin?", font = app.font)
  canvas.create_text(app.width/2, app.height/7 + 40, text = "pick one", font = app.sFont)

  if (app.hMood):
    canvas.create_rectangle(200, 200, 400, 300, width = app.bold, fill = app.sGreen)
  else: 
    canvas.create_rectangle(200, 200, 400, 300, width = app.narrow)
  canvas.create_text(300, 250, text = "happy", font = app.font)

  if (app.sadMood):
    canvas.create_rectangle(500, 200, 700, 300, width = app.bold, fill = app.sGreen)
  else: 
    canvas.create_rectangle(500, 200, 700, 300, width = app.narrow)
  canvas.create_text(600, 250, text = "sad", font = app.font)

  if (app.sMood): 
    canvas.create_rectangle(800, 200, 1000, 300, width = app.bold, fill = app.sGreen)
  else:
    canvas.create_rectangle(800, 200, 1000, 300, width = app.narrow)
  canvas.create_text(900, 250, text = "study", font = app.font)

  if (app.aMood):
    canvas.create_rectangle(50, 350, 250, 450, width = app.bold, fill = app.sGreen)
  else: 
    canvas.create_rectangle(50, 350, 250, 450, width = app.narrow)
  canvas.create_text(150, 400, text = "angry", font = app.font)

  if (app.wMood):
    canvas.create_rectangle(350, 350, 550, 450, width = app.bold, fill = app.sGreen)
  else:
    canvas.create_rectangle(350, 350, 550, 450, width = app.narrow)
  canvas.create_text(450, 400, text = "workout", font = app.font)

  if (app.pMood):
    canvas.create_rectangle(650, 350, 850, 450, width = app.bold, fill = app.sGreen)
  else:
    canvas.create_rectangle(650, 350, 850, 450, width = app.narrow)
  canvas.create_text(750, 400, text = "party!", font = app.font)

  if (app.jollyMood):
    canvas.create_rectangle(950, 350, 1150, 450, width = app.bold, fill = app.sGreen)
  else:
    canvas.create_rectangle(950, 350, 1150, 450, width = app.narrow)
  canvas.create_text(1050, 400, text = "holidays", font = app.font)

  canvas.create_rectangle(325, 500, 475, 550, width = 3)
  canvas.create_text(400, 525, text = "back", font = app.sFont, fill = app.sGreen)

  canvas.create_rectangle(725, 500, 875, 550, width = 3)
  canvas.create_text(800, 525, text = "next", font = app.sFont, fill = app.sGreen)

def moodMode_mousePressed(app, event):
  app.cx = event.x
  app.cy = event.y

  if (200 < app.cx < 400 and 200 < app.cy < 300):
    app.hMood = not app.hMood
  elif (500 < app.cx < 700 and 200 < app.cy < 300):
    app.sadMood = not app.sadMood
  elif (800 < app.cx < 1000 and 200 < app.cy < 300):
    app.sMood = not app.sMood
  elif (50 < app.cx < 250 and 350 < app.cy < 450):
    app.aMood = not app.aMood
  elif (350 < app.cx < 550 and 350 < app.cy < 450):
    app.wMood = not app.wMood
  elif (650 < app.cx < 850 and 350 < app.cy < 450):
    app.pMood = not app.pMood
  elif (950 < app.cx < 1150 and 350 < app.cy < 450):
    app.jollyMood = not app.jollyMood

  app.moods = [app.hMood, app.sadMood, app.sMood, app.aMood, app.wMood, app.pMood, app.jollyMood]
  print(app.moods)

  if (325 < app.cx < 475 and 500 < app.cy < 550):
    app.data.pop()
    print(app.data)
    app.mode = 'genreMode'

  elif(725 < app.cx < 875 and 500 < app.cy < 550):
    trueCount = app.moods.count(True)
    print(trueCount)
    mood = ["happy", "sad", "study", "angry", "workout", "party", "holiday"]

    if (trueCount == 1):
      c = 0
      for x in range(len(app.moods)):
        if (app.moods[x]):
          selectMood = mood[c]
        c += 1
        
      app.data.append(selectMood)
      print(app.data)
      app.moodPage = True
      app.mode = 'playlistSizeMode'
  
##########################################
# Playlist Size Mode
##########################################

# small: 10, medium: 18, large: 25 songs

def playlistSizeMode_redrawAll(app, canvas):
  canvas.create_text(app.width/2, app.height/3, text = "how many songs in the playlist?", font = app.font)

  if (app.sList):
    canvas.create_rectangle(200, 300, 400, 400, width = app.bold, fill = app.sGreen)
  else:
    canvas.create_rectangle(200, 300, 400, 400, width = app.narrow)
  canvas.create_text(300, 350, text = "10", font = app.font)

  if (app.mList):
    canvas.create_rectangle(500, 300, 700, 400, width = app.bold, fill = app.sGreen)
  else:
    canvas.create_rectangle(500, 300, 700, 400, width = app.narrow)
  canvas.create_text(600, 350, text = "18", font = app.font)

  if (app.lList):
    canvas.create_rectangle(800, 300, 1000, 400, width = app.bold, fill = app.sGreen)
  else:
    canvas.create_rectangle(800, 300, 1000, 400, width = app.narrow)
  canvas.create_text(900, 350, text = "25", font = app.font)

  canvas.create_rectangle(325, 500, 475, 550, width = 3)
  canvas.create_text(400, 525, text = "back", font = app.sFont, fill = app.sGreen)

  canvas.create_rectangle(725, 500, 875, 550, width = 3)
  canvas.create_text(800, 525, text = "next", font = app.sFont, fill = app.sGreen)

def playlistSizeMode_mousePressed(app, event):
  app.cx = event.x
  app.cy = event.y

  if (200 < app.cx < 400 and 300 < app.cy < 400):
    app.sList = not app.sList
  elif (500 < app.cx < 700 and 300 < app.cy < 400):
    app.mList = not app.mList
  elif (800 < app.cx < 1000 and 300 < app.cy < 400):
    app.lList = not app.lList

  app.listSizes = [app.sList, app.mList, app.lList]
  sizes = [10, 18, 25]

  if (325 < app.cx < 475 and 500 < app.cy < 550):
    app.data.pop()
    print(app.data)
    app.mode = 'moodMode'
 
  elif(725 < app.cx < 875 and 500 < app.cy < 550):
    trueCount = app.listSizes.count(True)
    if (trueCount == 1):
      c = 0
      for x in range(len(app.listSizes)):
        if (app.listSizes[x]):
          selectGenre = sizes[c]
        c += 1

      app.data.append(selectGenre)
      print(app.data)

      app.sizePage = True
      app.list = getPlaylist(app)
      app.mode = 'playlistMode'

def getPlaylist(app):
  playlist = makeList(app.data[0], app.data[1], app.data[2], app.data[3], [], [], [], [], [], [], 0, app.data[3] + 10, 1)
  print(playlist)
  return playlist

##########################################
# Display Playlist Mode
##########################################

def playlistMode_redrawAll(app, canvas):
  #snapshot code cited from 112 course notes: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#getAndSaveSnapshot
  canvas.create_text(110, 20, text='press s to save snapshot', font = app.sFont, fill = app.sGreen)

  if (app.image1 != None):
      canvas.create_image(1050, 65, image=ImageTk.PhotoImage(app.image1))

  canvas.create_text(app.width/2, 30, text = f"{app.data[2]} {app.data[0]} playlist!", font = app.font, fill = app.sGreen)

  if (app.data[3] == 10):
    dif = 35
    for i in range(len(app.list)):
      x, y = app.list[i]
      canvas.create_text(app.width/20, (i*dif) + 100, text = i+1, font = app.mFont)
      canvas.create_text(app.width/3.5 + 40, (i*dif) + 100, text = x, font = app.mFont)
      canvas.create_text(app.width/2 + 300, (i*dif) + 100, text = y, font = app.mFont)

  elif(app.data[3] == 18):
    dif = 20
    for i in range(len(app.list)):
      x, y = app.list[i]
      canvas.create_text(app.width/20, (i*dif)+80, text = i+1, font = app.medFont)
      canvas.create_text(app.width/3.5, (i*dif)+80, text = x, font = app.medFont)
      canvas.create_text(app.width/2 + 300, (i*dif)+80, text = y, font = app.medFont)
  else:
    dif = 16
    for i in range(len(app.list)):
        x, y = app.list[i]
        canvas.create_text(app.width/20, (i*dif)+60, text = i + 1, font = app.tFont)
        canvas.create_text(app.width/3.5, (i*dif)+60, text = x, font = app.tFont)
        canvas.create_text(app.width/2 + 300, (i*dif)+60, text = y, font = app.tFont)
    
  canvas.create_rectangle(100, 500, 250, 550, width = 3)
  canvas.create_text(175, 525, text = "randomize", font = app.sFont, fill = app.sGreen)

  canvas.create_rectangle(300, 500, 550, 550, width = 3)
  canvas.create_text(425, 480, text = "move songs:", font = app.sFont, fill = app.sGreen)

  canvas.create_rectangle(300, 560, 550, 580, width = 3)
  canvas.create_text(425, 570, text = "update", font = app.sFont, fill = app.sGreen)

  canvas.create_rectangle(650, 500, 900, 550, width = 3)
  canvas.create_text(775, 480, text = "delete songs:", font = app.sFont, fill = app.sGreen)

  canvas.create_rectangle(650, 560, 900, 580, width = 3)
  canvas.create_text(775, 570, text = "update", font = app.sFont, fill = app.sGreen)

  canvas.create_rectangle(950, 500, 1100, 550, width = 3)
  canvas.create_text(1025, 525, text = "next", font = app.sFont, fill = app.sGreen)

  if (app.songToMove != 0):
    canvas.create_text(425, 525, text=f"{app.songToMove} {app.newSpot}" , font = app.font, fill = app.sGreen)
  if (app.delete != 0):
    canvas.create_text(775, 525, text=f"{app.delete}" , font = app.font, fill = app.sGreen)
 
def playlistMode_mousePressed(app, event):
  app.cx = event.x
  app.cy = event.y
  if (100 < app.cx < 250 and 500 < app.cy < 550):
      random.shuffle(app.list)
      app.orLen = len(app.list)

  elif (300 < app.cx < 550 and 500 < app.cy < 550): #change orders
    print("boutta change order")
    app.changeOrder = True
    app.deleteSong = False

  elif(650 < app.cx < 900 and 500 < app.cy < 550):
    print("boutta delete songs")
    app.changeOrder = False
    app.toDel = True
  
  elif (300 < app.cx < 550 and 560 < app.cy < 580): #left update button pressed 
    if (app.secondVal and (0 < app.songToMove <= len(app.list)) and (0 < app.newSpot <= len(app.list))):
      currSong = app.list[app.songToMove - 1]
      app.list.pop(app.songToMove - 1)
      app.list.insert(app.newSpot - 1, currSong)
    app.songToMove = 0
    app.newSpot = 0
    app.firstVal = True
    app.secondVal = False
    app.firstDig = 0
    app.secondDig = 0  

  elif(650 < app.cx < 900 and 560 < app.cy < 580): #right update button pressed
    app.toDel = False
    if (0 < app.delete <= len(app.list)):
      app.delList.append(app.list.pop(app.delete - 1))
      app.list = makeList(app.data[0], app.data[1], app.data[2], app.data[3], app.list, app.delList, [], [], [], [], 0, app.data[3] + 10, 1)
    app.delete = 0
    app.delTen = 0

  elif (950 < app.cx < 1100 and 500 < app.cy < 550): #next button pressed - "restart" app
    if (app.songToMove == 0 and app.newSpot == 0 and app.delete == 0):
      app.mode = 'newSplashMode'
  

def playlistMode_keyPressed(app, event):
    acceptedVals = "abcdefghijklmnopqrstuvwxyz1234567890"
    nums = "1234567890"

    #snapshot code cited from 112 course notes: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#getAndSaveSnapshot
    if (event.key == 's'):
        app.saveSnapshot()

    #checking "delete songs" part
    if (app.toDel and event.key in nums):
        app.delete = app.delete*(10**app.delTen) + int(event.key)
        app.delTen += 1

    #checking move songs condition
    if(event.key in acceptedVals and app.changeOrder):
      if (app.firstVal and event.key in nums):
        app.songToMove = app.songToMove*(10**app.firstDig) + int(event.key)
        if (app.songToMove > len(app.list)):
          app.leftValid = False
        else:
          app.leftValid = True
        app.firstDig += 1
      elif(app.secondVal and event.key in nums):
        app.newSpot = app.newSpot*(10**app.secondDig) + int(event.key)
        app.secondDig += 1

        if (app.newSpot > len(app.list)):
          app.leftValid = False
        else:
          app.leftValid = True

    elif(event.key == "Space" and app.changeOrder):
      app.firstVal = False
      app.secondVal = True

##########################################
# Main App
##########################################
# rgbString method from 112 course notes: https://www.cs.cmu.edu/~112/notes/notes-graphics.html
def rgbString(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def appStarted(app):
    app.mode = 'splashScreenMode'
    app.score = 0
    app.timerDelay = 50
    
    #image below found from Google Image search
    url = 'https://lockpaperscissors.co/wp-content/uploads/spotify-theme-music-bkg-dark.png'
    app.image = app.loadImage(url)
    app.image1 = None

    app.kPSelect = False
    app.latSelect = False
    app.indieSelect = False
    app.classSelect = False
    app.pSelect = False
    app.eSelect = False
    app.hSelect = False
    app.countrySelect = False

    app.hMood = False
    app.sadMood = False
    app.sMood = False
    app.aMood = False
    app.wMood = False
    app.pMood = False
    app.jollyMood = False

    app.sList = False
    app.mList = False
    app.lList = False
    
    app.artistPage = False
    app.genrePage = False
    app.moodPage = False
    app.sizePage = False
    app.playlistPage = False

    app.bold = 5
    app.narrow = 2 
    app.font = 'Arial 24 bold'
    app.mFont = 'Arial 18 bold'
    app.medFont = 'Arial 13 bold'
    app.sFont = 'Arial 12 bold'
    app.tFont = 'Arial 10 bold'

    app.artistList = []
    app.data = []
    app.i = 0
    app.list = []
    app.songToMove = 0
    app.newSpot = 0
    app.delete = 0
    app.firstVal = True
    app.secondVal = False

    app.firstDig = 0
    app.secondDig = 0

    app.leftValid = True

    app.changeOrder = False
    app.deleteSong = False

    app.leftVal = ""
    app.rightVal = ""
    app.toDel = False

    app.delTen = 0
    app.delList = []

    app.ranPage = False

    app.sGreen = rgbString(30,215,96)
    app.pGreen = rgbString(208,240, 192)
    app.dGreen = rgbString(54, 156, 27)

runApp(width=1200, height=600)