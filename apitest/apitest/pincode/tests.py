from rest_framework.reverse import reverse
from django.test import Client

client = Client()

######################### INTERVIEW STAGE1 ###########################################################
request = client.post(reverse('post_locations'), {"pincode": "201005","address": "Sahibabad","city": "Ghaziabad","lng": "111.11","lat": "111.12"})
request2 = client.post(reverse('post_locations'), {"pincode": "201005","address": "Sahibabad","city": "Ghaziabad","lng": "111.50","lat": "111.62"})
print(request.content)
print(request2.content)


######################## INTERVIEW STAGE 2 ##########################################################


request3 = client.get(reverse('get_using_postgres')+'?latitude=28.6488&&longitude=77.1726')
request4 = client.get(reverse('get_using_self')+'?latitude=28.6488&&longitude=77.1726')
print(request3.content)
print(request4.content)

####################### INTERVIEW STAGE 3 ###########################################################

request5 = client.post(reverse('get_area_details'), {"lng": "77.09106445","lat": "28.62310355"})
request6 = client.post(reverse('get_area_details'), {"lng": "77.03887939","lat": "28.47352011"})
print(request5.content)
print(request6.content)