import youtube_dl
import subprocess


def descargar_video(url):
  ydl_opts = {}
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])


def partir_intervalo(fuente, inicio, fin, salida):
  partirComando = 'ffmpeg -i '+ fuente +' -ss '+ inicio +' -to '+ fin +' -q:a 0 -map a ' + salida
  subprocess.call(partirComando, shell=True)