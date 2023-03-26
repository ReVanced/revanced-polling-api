import os
import redis
import requests
from pprint import pformat

paste_url: str = "https://api.paste.ee/v1/pastes"

db = redis.StrictRedis(
    host=os.environ["REDIS_URL"], port=os.environ["REDIS_PORT"], db=3
)

votes: dict = {}

for key in db.scan_iter("*"):
    ballot = db.json().get(key)["votes"]
    for entry in ballot:
        if entry["vote"]:
            if entry["cid"] in votes:
                votes[entry["cid"]] += 1
            else:
                votes[entry["cid"]] = 1

raw_votes: str = pformat(votes)
sorted_votes: str = pformat(sorted(votes))

text: list = [
        'Raw votes:\n\n',
        raw_votes,
        '\n\nSorted votes:\n\n',
        sorted_votes
]

with open("votes.txt", "w") as f:
    f.writelines(text)

payload: dict = {
    "description": "ReVanced Poll Results",
    "sections": [
        {
            "name": "Raw Votes",
            "syntax": "autodetect",
            "contents": raw_votes
        },
        {
            "name": "Sorted Votes",
            "syntax": "autodetect",
            "contents": sorted_votes
        }
    ]
}

headers = {
    "Content-Type": "application/json",
    "X-Auth-Token": os.environ["PASTE_EE_KEY"]
}

response: dict = requests.post(paste_url, json=payload, headers=headers).json()

print(f'Upload response: {response["link"]}')
