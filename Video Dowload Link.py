
#Permite descargar videos de YouTube
from pytube import YouTube

# Ingresamos el enlace del video
yt = YouTube('https://youtu.be/sidPTvbTv9o?si=aR_tQ7LULpSwuMrd')

# Filtros para el video 
streams = yt.streams.filter(progressive=True, file_extension='mp4')

# Ordenar el video por resolución màs alta 
streams = streams.order_by('resolution').desc()

# Selecciona el video en mayor resolución
stream = streams.first()

# Descargar el video
stream.download()