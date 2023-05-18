import base64
import hashlib
import hmac
import os
import sys
import time
import requests

access_key = "018707c3fb7c6e5c0d0896ebea400107"
access_secret = "paoHmtERn4lCY3my9Iw1TrvVSdrdoiTlamnRajMr"
requrl = "http://identify-eu-west-1.acrcloud.com/v1/identify"

http_method = "POST"
http_uri = "/v1/identify"
# default: "fingerprint" it's for recognizing fingerprint, 
# identify audio: data_type="audio"
data_type = "audio"
signature_version = "1"
timestamp = time.time()

string_to_sign = http_method + "\n" + http_uri + "\n" + access_key + "\n" + data_type + "\n" + signature_version + "\n" + str(
    timestamp)

sign = base64.b64encode(hmac.new(access_secret.encode('ascii'), string_to_sign.encode('ascii'),
                                 digestmod=hashlib.sha1).digest()).decode('ascii')

# suported file formats: mp3,wav,wma,amr,ogg, ape,acc,spx,m4a,mp4,FLAC
# File size: < 1M 
# Duration < 15 seconds

###OPCION 2
#files = []
#audio_folder = "c:\\repositorios\metricas\media"  # Ruta de la carpeta que contiene los archivos de audio
# Iterar sobre los archivos de audio en la carpeta
#for filename in os.listdir(audio_folder):
#    file_path = os.path.join(audio_folder, filename)
#    if os.path.isfile(file_path):
#        files.append(('sample', (filename, open(file_path, 'rb'), 'audio/mpeg')))


f = open(sys.argv[0], "rb")
sample_bytes = os.path.getsize(sys.argv[0])

file_path = 'c:\\repositorios\\metricas\\media\\'
#file_audio = 'lianne-la-havas-wonderful-live.mp3'
file_audio = 'do-i-wanna-know-official-video.mp3'

files = [
    ('sample', (file_audio, open(os.path.join(file_path, file_audio), 'rb'), 'audio/mpeg'))
]


data = {'access_key': access_key,
        'sample_bytes': sample_bytes, #'sample_bytes': '',
        'timestamp': str(timestamp), #'timestamp': timestamp
        'signature': sign,
        'data_type': data_type,
        "signature_version": signature_version}

response = requests.post(requrl, files=files, data=data)
response.encoding = "utf-8"
print(response.json())