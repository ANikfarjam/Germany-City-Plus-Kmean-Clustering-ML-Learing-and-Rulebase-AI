#author ANikfarjam
#extracting data from job board API
#source: https://rapidapi.com/arbeitnow/api/arbeitnow-free-job-board/
import requests
import json
url = "https://arbeitnow-free-job-board.p.rapidapi.com/api/job-board-api"

headers = {
	"Content-Type": "application/json",
	"X-RapidAPI-Key": "5847527b5bmshe2f2f4e69370c30p1a3ec9jsn659fda58c155",
	"X-RapidAPI-Host": "arbeitnow-free-job-board.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
with open('extractedjobs.json', 'w') as fp:
    json.dump(response.json(),fp)
