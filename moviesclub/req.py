import requests
import json

URL = "http://127.0.0.1:8000/"

data={"name":"Avengers: Endgame","img":"https://bit.ly/2Pzczlb","summary":"Adrift in space with no food or water, Tony Stark sends a message to Pepper Potts as his oxygen supply starts to dwindle. Meanwhile, the remaining Avengers -- Thor, Black Widow, Captain America, and Bruce Banner -- must figure out a way to bring back their vanquished allies for an epic showdown with Thanos -- the evil demigod who decimated the planet and the universe."}
# data={"name":"Harry Potter and the Order of the Phoenix","img":"https://bit.ly/2IcnSwz","summary":"Harry Potter and Dumbledore's warning about the return of Lord Voldemort is not heeded by the wizard authorities who, in turn, look to undermine Dumbledore's authority at Hogwarts and discredit Harry."}
json_data = json.dumps(data)

r = requests.post(url=URL,data=json_data)
# r = requests.get(url=URL)
data = r.json()
print(data)