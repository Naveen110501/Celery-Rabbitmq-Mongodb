import pafy


def startpy():
    conversion()


def conversion():
    url = "https://youtu.be/fRRxW0ECBUg"
    final = pafy.new(url)
    audio = final.getbestaudio()
    audio.download()


    #audio = final.getbest(preftype = "mp3") 



if __name__ == '__main__':
    startpy()