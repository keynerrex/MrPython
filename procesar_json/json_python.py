import urllib.request

respuesta = urllib.request.urlopen(
    "http://globalmentoring.com.mx/api/personas.json")
print(respuesta)