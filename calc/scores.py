# encoding: utf-8
import pymongo
from pprint import pprint
mongo_uri='mongodb://127.0.0.1:8100'
mongo_db='zhihu'
client = pymongo.MongoClient(mongo_uri)
db = client[mongo_db]
people = db['people']
scores={}
max_relationship = 0
max_contribution = 0
for p in people.find(limit=0):
    if 'followers' not in p:
        continue
    id=p['id'].encode('utf-8')
    scores[id] = {}
    answers = p['answers'] + 1
    asks = p['asks'] + 1
    agree = p['agree'] + 1
    thanks = p['thanks'] + 1
    followers = p['followers'] + 1
    followees = p['followees'] + 1
    scores[id]['relationship'] = relationship = float(followers)*80/100 + float(followees)*20/100
    scores[id]['contribution'] = contribution = (agree + thanks) / float(asks + answers)
    if relationship > max_relationship: max_relationship = relationship
    if contribution > max_contribution: max_contribution = contribution
for p in scores:
    scores[p]['relationship'] /= (max_relationship)
    scores[p]['contribution'] /= (max_contribution)
    scores[p]['total'] = scores[p]['relationship'] * 20 / 100 + scores[p]['contribution'] * 20 / 100
# pprint(sorted(scores.items()))

sorted_items = sorted(scores.items(), key=lambda y: int(y[1]['total'] * 1e10), reverse=True)

for p in sorted_items:
    id=p[0]
    scores=p[1]
    people.update_one({'id':id},{'$set':{'scores':scores}})
