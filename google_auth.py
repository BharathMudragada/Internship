#1006549871150-3vk1sho56rq8d8joblm17geju5uf7vio.apps.googleusercontent.com - clientId
#JCUAM4wKHcfrqW4M5pssUJVR - clientSecret
#https://drive.google.com/open?id=1HWMNL8nnF5uhe9jVFCwvbQva8BSa4TdRPsuQ9tb86ug - file id
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
file_obj = drive.CreateFile({'id': '1HWMNL8nnF5uhe9jVFCwvbQva8BSa4TdRPsuQ9tb86ug'})
file_obj.GetContentFile('result.csv', mimetype='text/csv')