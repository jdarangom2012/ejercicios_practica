from django.urls import path
from e_commerce.api.hello_world_api import *


urlpatterns = [
    path('hello-world/',hello_world),

]
 