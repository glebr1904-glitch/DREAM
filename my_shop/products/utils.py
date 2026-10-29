from .models import Product
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline
    
)


  
def q_search(query):
    if query.isdigit() and len(query)<=7:
        return Product.objects.filter(id=int(query))


    vector=SearchVector('name')
    query_objects=SearchQuery(query)

    query_res=(Product.objects.annotate(
        rank=SearchRank(vector, query_objects)
    )).filter(rank__gt=0).order_by('-rank')

    query_res=query_res.annotate(
        headline=SearchHeadline(
            'name',
            query_objects,
            start_sel="<span style='background-color:yellow'>",
            stop_sel="</span>",
        ))

    return query_res