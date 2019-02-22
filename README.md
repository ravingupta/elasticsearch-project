Download and extract elastic search
go to elasticsearch-folder/
run ./bin/elasticsearch

Download and extract mongo
go to mongo-folder/
run ./bin/mongod (if requires permission run with sudo)

run mongo-cli

use searchbar

db.createUser(
   {
    user: "searchbaruser",
    pwd: "searchbaruser",
    roles: [ "readWrite", "dbAdmin" ]
   }
)

TF-IDF [https://en.wikipedia.org/wiki/Tf%E2%80%93idf]