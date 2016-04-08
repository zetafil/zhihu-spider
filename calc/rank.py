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
limit = 100000
for x in following.find(limit=limit):
    G.add_edge(x['follower'], x['followee'])

# p = {i: 1 if i == 'sherrie' else 0 for i in G.nodes()}
# rank = nx.pagerank(G, personalization=p)
rank = nx.pagerank(G)

ranking = sorted(rank.items(), key=operator.itemgetter(1), reverse=True)

# print G.out_edges('mymiss')

for i,(id,wight) in enumerate(ranking, start=1):
    for follower,followee in G.out_edges(id):
        # print follower, followee
        if 'followers' not in G.node[followee]:
            G.node[followee]['followers'] = []
        if len(G.node[followee]['followers']) < 100:
            G.node[followee]['followers'].append({'id':id, 'rank':i, 'pagerank':wight})

# for x in G.nodes():
    # print G[x].get('followers', None)
res=[]
for i, (id, wight) in enumerate(ranking[:100], start=1):
    # print id
    res.append({'id':id, 'rank':i, 'pagerank':wight, 'followers': G.node[id]['followers'] if 'followers' in G.node[id] else []})

db['ranking'].insert_one({'type':'user', 'list':res}    )
# print res
# print ranking[:100]
# print len(ranking)
# for r in ranking:
    # print r
    # people.update_one({'id':r[0].encode('utf-8')}, {'$set': {'scores.pagerank':r[1]}})

