import os
import json

responses = []
track_name = "wonderful" # ==nombre de la carpeta
media_path = "c:\\repositorios\\metricas\\media\\" + track_name
responses_path = "c:\\repositorios\\metricas\\responses\\"
responses_file = os.path.join(responses_path, track_name +".json")
responses_fileReport = os.path.join(responses_path, "report "+track_name +".json")

with open(responses_file, "r") as file:
    #content = file.read()
    content =json.load(file)
    contentJson = json.dumps(content, ensure_ascii=False) #"comillas"
    print(contentJson)

responsesSuccess = []
responsesError = []

for item in content:
    data = {
          "sample_bytes": item["data"]["sample_bytes"],
          "timestamp": item["data"]["timestamp"]
    }
    if (item["response"]["status"]["code"] == 0) :
        info = {
            "cost_time": item["response"]["cost_time"],
            "title": item["response"]["metadata"]["music"][0]["title"],
            "album": item["response"]["metadata"]["music"][0]["album"]["name"],
            "artist": item["response"]["metadata"]["music"][0]["artists"][0]["name"],
        }
        responsesSuccess.append({"nameFile" : item["item"], "info" : info, "data" : data})

    if (item["response"]["status"]["code"] == 1001) :
        responsesError.append({"nameFile" : item["item"], "data" : data})

with open(responses_fileReport, "w") as file:
    json.dump({
        "success": responsesSuccess,
        "error" : responsesError
    }, file, ensure_ascii=False)

#with open(responses_fileReport, "w") as file:
#    file.write(str({
#        "success": responsesSuccess,
#        "error" : responsesError
#    }))

print(responsesSuccess)
print(responsesError)