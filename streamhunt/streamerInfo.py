import requests

headers = {
    'client-id': 'kcr0klbq15200bi1tfn5clbuhwzimb',
    'Authorization': 'Bearer aewkd3yjjwvqcuzpafsomafbv5oy7i',
 }
response = requests.get("https://api.twitch.tv/helix/streams", headers=headers)
streamer = response.json()



print(streamer)
   


