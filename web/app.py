from flask import Flask, jsonify, request, url_for
from flask_graphql import GraphQLView
import pymongo
import graphene

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://db:27017")

# connects to the database or create a new one if not exists
db = client.aNewDB

# creates a new collection
UserNum = db["UserNum"]

# insert a document in the collection
UserNum.insert({
    "num_of_visits":0
})

# GraphQL Schema
######################################################################

# define a new schema to execute queries
class User(graphene.ObjectType):
    number = graphene.Int()

# this is the object where the query fields and resolvers are defined
class Query(graphene.ObjectType):
    # this is a query field named user.... the query {user} returns what is inside the resolve
    user = graphene.Field(User)

    # here is what should be returned for the {user} query
    def resolve_user(self, info):
        # database consult goes here...
        prev_num = UserNum.find({})[0]['num_of_visits']
        new_num = prev_num + 1
        UserNum.update({}, {"$set": {"num_of_visits": new_num}})

        # just returning an object with a static number
        return User(number=new_num)


schema = graphene.Schema(query=Query)

######################################################################


# Endpoint to make queries
#####################################################
# app.add_url_rule("/graphql", view_func=GraphQLView.as_view(
#     "graphql",
#     schema = schema,
#     graphiql=True 
# ))
####################################################


@app.route("/")
def main():
    query = '{user{number}}'
    result = schema.execute(query)
    num = result.data['user']['number']
    return "Hello user: " + str(num)

if __name__ == "__main__":
    app.run(host="0.0.0.0")