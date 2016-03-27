## update field type
```
db.people.find({}).forEach(function (v) {
    v.agree = new NumberInt(v.agree);
    v.thanks = new NumberInt(v.thanks);
    v.asks = new NumberInt(v.asks);
    v.answers = new NumberInt(v.answers);
    v.posts = new NumberInt(v.posts);
    v.collections = new NumberInt(v.collections);
    v.logs = new NumberInt(v.logs);
    db.people.save(v)
})
```
