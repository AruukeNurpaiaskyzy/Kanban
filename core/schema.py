import graphene
import graphql_jwt

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello, world!")
class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()  # Для получения токенов
    refresh_token = graphql_jwt.Refresh.Field()  # Для обновления токенов
    verify_token = graphql_jwt.Verify.Field() 

schema = graphene.Schema(query=Query, mutation=Mutation)
