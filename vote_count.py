import os
import redis
import requests
from pprint import pprint

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

raw_votes: str = pprint.pformat(votes)
sorted_votes: str = pprint.pformat(
    dict(sorted(votes.items(), key=lambda item: item[1], reverse=True))
)

with open("votes.txt", "w") as f:
    f.write(raw_votes)
    f.write(sorted_votes)
