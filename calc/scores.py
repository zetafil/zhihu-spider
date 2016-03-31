# encoding: utf-8
import pymongo
from pprint import pprint
mongo_uri='mongodb://127.0.0.1:27017'
mongo_db='zhihu'
client = pymongo.MongoClient(mongo_uri)
db = client[mongo_db]

scores={}
max_relationship = 0
max_contribution = 0
for p in db['people'].find(limit=1000):
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
    scores[id]['relationship'] = relationship = followers / float(followees)
    scores[id]['contribution'] = contribution = (agree + thanks) / float(asks + answers)
    if relationship > max_relationship: max_relationship = relationship
    if contribution > max_contribution: max_contribution = contribution
for p in scores:
    scores[p]['relationship'] /= (max_relationship)
    scores[p]['contribution'] /= (max_contribution)
    scores[p]['total'] = scores[p]['relationship'] * 20 / 100 + scores[p]['contribution'] * 20 / 100
pprint(scores)