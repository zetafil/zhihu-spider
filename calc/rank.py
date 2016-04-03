# encoding: utf-8
import pymongo
import networkx as nx
from pprint import pprint
import operator
mongo_uri='mongodb://127.0.0.1:8100'
mongo_db='zhihu'
client = pymongo.MongoClient(mongo_uri)
db = client[mongo_db]
following = db['following']
people = db['people']

G = nx.DiGraph()
for x in following.find(limit=0):
    G.add_edge(x['follower'], x['followee'])

rank = nx.pagerank(G)
print len(G.nodes())
# 
ranking = sorted(rank.items(), key=operator.itemgetter(1))

print ranking
# print len(ranking)
# for r in ranking:
    # print r
    # people.update_one({'id':r[0].encode('utf-8')}, {'$set': {'scores.pagerank':r[1]}})