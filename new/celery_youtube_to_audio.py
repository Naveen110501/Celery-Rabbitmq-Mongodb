from celery import Celery
import pafy


app = Celery('celery_youtube_to_audio', broker = 'amqp://localhost' )


@app.task
def conversion():
    url = "https://youtu.be/fRRxW0ECBUg"
    url.encode('utf-8')
    final = pafy.new(url)
    audio = final.getbestaudio()
    return audio.download()

   


