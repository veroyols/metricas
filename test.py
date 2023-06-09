import base64
import hashlib
import hmac
import os
import time
import requests
import json


access_key = "018707c3fb7c6e5c0d0896ebea400107"
access_secret = "paoHmtERn4lCY3my9Iw1TrvVSdrdoiTlamnRajMr"
requrl = "http://identify-eu-west-1.acrcloud.com/v1/identify"

http_method = "POST"
http_uri = "/v1/identify"
data_type = "audio" # default: "fingerprint" it"s for recognizing fingerprint, 
signature_version = "1"
timestamp = time.time()

string_to_sign = http_method + "\n" + http_uri + "\n" + access_key + "\n" + data_type + "\n" + signature_version + "\n" + str(timestamp)

sign = base64.b64encode(hmac.new(access_secret.encode("ascii"), string_to_sign.encode("ascii"), digestmod=hashlib.sha1).digest()).decode("ascii")

# suported file formats: mp3,wav,wma,amr,ogg, ape,acc,spx,m4a,mp4,FLAC
# File size: < 1M 
# Duration < 15 seconds

track_name = "wonderful" # ==nombre de la carpeta
media_path = "c:\\repositorios\\metricas\\media\\" + track_name
responses_path = "c:\\repositorios\\metricas\\responses\\"
responses_file = os.path.join(responses_path, track_name +".json")

#file_audio = "lianne-la-havas-wonderful-live.mp3"
#file_audio = "do-i-wanna-know-official-video.mp3"

###OPCION 1
#files.append(("sample", (file_audio, open(os.path.join(media_path, file_audio), "rb"), "audio/mpeg")))

###OPCION 2
responses = []

for item in os.listdir(media_path):
    file_path = os.path.join(media_path, item)
    if os.path.isfile(file_path): #si no es directorio
        file =[("sample", (item, open(file_path, "rb"), "audio/mpeg"))]
        sample_bytes = os.path.getsize(file_path)
        data = {
            "access_key": access_key,
            "sample_bytes": sample_bytes, #"sample_bytes": "",
            "timestamp": str(timestamp), #"timestamp": timestamp
            "signature": sign,
            "data_type": data_type,
            "signature_version": signature_version
            }
        response = requests.post(requrl, files=file, data=data)
        response.encoding = "utf-8"
        responses.append({
            "item": item,
            "data": data,
            "response" : response.json()
            })
#Aca iria el Report del response asi se guarda

print(responses)

with open(responses_file, "w") as file:
    json.dump(responses, file, ensure_ascii=False)
    #file.write(str(responses))
