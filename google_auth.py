#https://drive.google.com/open?id=15U3O8h0AbP23XjdTpqSPRgA8gmJfIpmk
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
file_obj = drive.CreateFile({'id': '15U3O8h0AbP23XjdTpqSPRgA8gmJfIpmk'})
file_obj.GetContentFile('result.csv', mimetype='text/csv')
