import moviepy.editor as mp 


def startpy():
    conversion()


def conversion():
    clip = mp.VideoFileClip("bb.mp4") 
    clip.audio.write_audiofile("a.mp3") 


if __name__ == '__main__':
    startpy()