import graphene
from graphene_django.types import DjangoObjectType
from .models import Order
import graphql_jwt
from orders.schema import Query as OrdersQuery, Mutation as OrdersMutation
from orders.schema import AuthMutations

class AuthMutations(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = "__all__"

class Query(graphene.ObjectType):
    all_orders = graphene.List(OrderType)
    order_by_id = graphene.Field(OrderType, id=graphene.ID(required=True))

    def resolve_all_orders(root, info):
        return Order.objects.all()

    def resolve_order_by_id(root, info, id):
        return Order.objects.get(pk=id)

class CreateOrder(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=False)

    order = graphene.Field(OrderType)

    def mutate(root, info, title, description=None):
        order = Order.objects.create(title=title, description=description)
        return CreateOrder(order=order)

class UpdateOrderStatus(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        status = graphene.String(required=True)

    order = graphene.Field(OrderType)

    def mutate(root, info, id, status):
        order = Order.objects.get(pk=id)
        order.status = status
        order.save()
        return UpdateOrderStatus(order=order)

class Mutation(graphene.ObjectType):
    create_order = CreateOrder.Field()
    update_order_status = UpdateOrderStatus.Field()

class Query(OrdersQuery, graphene.ObjectType):
    pass

class Mutation(OrdersMutation, AuthMutations, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
