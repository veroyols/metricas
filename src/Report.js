//import data from '../responses/doIWannaKnow.json'
/*
{
    "archive" : item, 
    "response": response.json()
}
*/

const data = [
    {
        "archive": "do-i-wanna-know-official-video (online-audio-converter.16000).flac",
        "response": 
        {
            "metadata": 
            {
                "timestamp_utc": "2023-05-18 19: 07: 24", 
                "music": [
                    {
                        "db_begin_time_offset_ms": 3000, 
                        "db_end_time_offset_ms": 14340, 
                        "sample_begin_time_offset_ms": 0, 
                        "sample_end_time_offset_ms": 11340, 
                        "play_offset_ms": 14920, 
                        "genres": [
                            {
                                "name": "Alternative"
                            }
                        ], 
                        "title": "Do I Wanna Know?", 
                        "album": {
                            "name": "AM"
                        }, 
                        "acrid": "7ba416e859845247a65db99a7fb77211", 
                        "external_ids": {}, 
                        "external_metadata": {
                            "spotify": {
                                "track": {
                                    "name": "Do I Wanna Know?", 
                                    "id": "2UzMpPKPhbcC8RbsmuURAZ"
                                }, 
                                "album": {
                                    "name": "AM", 
                                    "id": "41vPD50kQ7JeamkxQW7Vuy"
                                }, 
                                "artists": [
                                    {
                                        "name": "Arctic Monkeys", "id": "7Ln80lUS6He07XvHI8qqHH"
                                    }
                                ]
                            }
                        }, 
                        "result_from": 3, 
                        "score": 100, 
                        "release_date": "2013-01-01", 
                        "label": "Universal Music", 
                        "duration_ms": 271716, 
                        "artists": [
                            {
                                "name": "Arctic Monkeys"
                            }
                        ]
                    },
                    {
                        "album": {
                            "name": "Zbc"
                        }, "label": "Tate Music Group", "acrid": "6b77b95ac5af1addf03458bd8adcfcef",
                        "external_ids": {}, "external_metadata": {
                            "spotify": {
                                "track": {
                                    "name": "Simple & Plain", "id": "3JkPJe3Jvm72ygWlOCFIyy"
                                }, "album": {
                                    "name": "Zbc", "id": "1RD9aRjw13KwgDoSYAcEWR"
                                }, "artists": [
                                    {
                                        "name": "Dinamite & Young Pharaoh", "id": "6thJTGN6VDSqRsXl6DaknZ"
                                    }
                                ]
                            }
                        }, "result_from": 3, "sample_begin_time_offset_ms": 0, "sample_end_time_offset_ms": 11100, "play_offset_ms": 14720, "artists": [
                            {
                                "name": "Dinamite & Young Pharaoh"
                            }
                        ], "score": 100, "release_date": "2014-12-16", "db_begin_time_offset_ms": 2800, "db_end_time_offset_ms": 13900, "duration_ms": 73328, "title": "Simple & Plain", "genres": [
                            {
                                "name": "Hip Hop"
                            }
                        ]
                    },
                    {
                        "album": {
                            "name": "Crawl Back"
                        }, "acrid": "2570caebabba6f8519e7e732679dd70d", "external_ids": {}, "db_end_time_offset_ms": 14180, "sample_begin_time_offset_ms": 0, "sample_end_time_offset_ms": 11320, "play_offset_ms": 14780, "artists": [
                            {
                                "name": "Down Low Tha B365t"
                            },
                            {
                                "name": "Kristastrophe"
                            }
                        ], "score": 100, "release_date": "2018-03-03", "result_from": 3, "label": "Fire Breather Recordz", "db_begin_time_offset_ms": 2860, "duration_ms": 308783, "title": "Crawl Back", "external_metadata": {
                            "spotify": {
                                "track": {
                                    "name": "Crawl Back", "id": "2jCTjyZ3oqfUWihOYiVEE7"
                                }, "album": {
                                    "name": "Crawl Back", "id": "0rXZGF5uZHMf5fU5qoIRRI"
                                }, "artists": [
                                    {
                                        "name": "Down Low Tha B365t", "id": "0WZAMjC46oxm4lEB5p7NhJ"
                                    },
                                    {
                                        "name": "Kristastrophe", "id": "5XiBcOXSdat8gC5jpAllAD"
                                    }
                                ]
                            }
                        }
                    }
                ]
            }, 
            "cost_time": 1.8770000934601, 
            "status": {
                "code": 0, 
                "msg": "Success", 
                "version": "1.0"
            }, 
            "result_type": 0
        }
    }        
    ,
    {        
        "archive": "lianne-la-havas-wonderful-live.mp3",
        "response": {
            "status": {
                "code": 1001, 
                "msg": "Success", 
                "version": "1.0"
            }
        }
    }
]

const Report = (data) => { //data = [{"archive" : archive, "response": response}, {...}]
    
    let notRecognize = [];
    let success = [];
    let others = 0;
    
    for (let i = 0; i < data.length; i++) {
        const element = data[i];
        
        if (element.response.status.code === 0) {
            let info = 
            {
                "nameFile" : element.archive, 
                "cost_time": element.response.cost_time,
                "title": element.response.metadata.music[0].title,
                "album": element.response.metadata.music[0].album.name,
                "artist": element.response.metadata.music[0].artists[0].name,
                "data": element.data
            }
            success.push(info)
        }
        else if (element.response.status.code === 1001) {
            notRecognize.push({ 
                "nameFile" : element.archive, 
                "data": element.data
            })
        } 
    }
    let report = {
        "notRecognize" : { 
            "count": notRecognize.length,
            "items": notRecognize
        },
        "sucess" : {
            "count": success.length,
            "items": success
        },
    }
    console.log(JSON.stringify(report, null, 2))
    return report;
}

Report(data);
//export default {Report}