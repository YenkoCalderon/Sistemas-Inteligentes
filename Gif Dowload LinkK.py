import requests #Enviar una solicitud
import shutil

def gif(enlace, archivo):
    try:
        # Hacer una solicitud GET al enlace
        respuesta = requests.get(enlace, stream="True")
        # Verificar si la solicitud fue exitosa
        if respuesta.status_code == 200:
            # Abrir un archivo en modo binario y escribir el contenido de la respuesta en él
            with open(archivo, 'wb') as archivo:
                respuesta.raw.decode_content = True
                shutil.copyfileobj(respuesta.raw, archivo)
            print("GIF guardado Correctamente:", archivo)
        else:
            print("Error al descargar el GIF:", respuesta.status_code)
    except Exception as e:
        print("Ocurrió un error:", str(e))

# Ejemplo de uso
enlace = "https://media3.giphy.com/media/jIMfuPWTrYgEw/giphy.gif"
archivo = "cr7.gif"  # Nombre que deseas darle al archivo GIF descargado

gif(enlace, archivo)

