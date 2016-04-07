# encoding: utf-8
import pymongo
import networkx as nx
from pprint import pprint
import operator
mongo_uri='mongodb://127.0.0.1:8100'
mongo_db='zhihu'
client = pymongo.MongoClient(mongo_uri,connect=False )
# client = pymongo.MongoWrapper(mongo_uri )
db = client[mongo_db]
following = db['following']
people = db['people']

G = nx.DiGraph()
limit = 10000
for x in following.find(limit=limit):
    G.add_edge(x['follower'], x['followee'])

print G.out_edges('davidc')
# p = {i: 1 if i == 'sherrie' else 0 for i in G.nodes()}
# rank = nx.pagerank(G, personalization=p)
rank = nx.pagerank(G)

ranking = sorted(rank.items(), key=operator.itemgetter(1), reverse=True)

for id,wight in ranking:
    for follower, _ in G.in_edges(id):
        if 'followers' not in G[follower]:
            G[follower]['followers'] = []
        else if len(G[follower]['followers']) < 100:
            G[follower]['followers'].append(id)

for x in G.nodes():
    print G[x].get('followers', None)
# print ranking[:100]
# print len(ranking)
# for r in ranking:
    # print r
    # people.update_one({'id':r[0].encode('utf-8')}, {'$set': {'scores.pagerank':r[1]}})

