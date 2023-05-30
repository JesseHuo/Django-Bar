from . import views
from django.urls import path

app_name = 'drinks'
urlpatterns = [
    # /drinks/
    path('', views.IndexClassView.as_view(), name='index'),
    # needs "as_view()" when pass in a class

    # /drinks/item_id
    # ----------------the function based view below is superseded, replaced by class view
    # path('<int:item_id>/',views.detail,name='detail'),
    # a path can be quoted by its name
    # index page gives options to link to urls "drinks/item.id"->  click to visit the url and pass the "item.id" into "item_id" (new definition to be passed into views ) -> url pulls detail view and passes over the item_id -> detail view render detail template
    # means the path will be "drinks/item_id inputted"

    path('<int:item_id>/', views.detail, name='detail'),

    # path('item/', views.item, name='item'),

    path('add/', views.CreateItem.as_view(), name='create_item'),
    # add items

    path('update/<int:item_id>/', views.update_item, name='update_item'),
    # item_id here is passed into views.update_item as item_id

    path('delete/<int:pk>/', views.DeleteClassView.as_view(), name='delete_item')
]