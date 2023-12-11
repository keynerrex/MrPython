from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

# Subir un archivo
file1 = drive.CreateFile({'title': 'Hello.txt'})
file1.Upload()

# Lista de archivos en Drive
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file in file_list:
    print('Título: %s, ID: %s' % (file['title'], file['id']))
