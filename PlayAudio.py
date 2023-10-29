from pygame import mixer

with open("audio.txt", "r") as f:
    fileName = f.read()

mixer.init()
mixer.music.load(fileName)
mixer.music.play()
while True:
    if mixer.music.get_busy() == False:
        mixer.music.play()
    else:
        pass
