import requests
from os import environ
from datetime import datetime

USERNAME = environ.get("PIXELA_USR")
TOKEN = environ.get("PIXELA_TOKEN")
GRAPH_ID = environ.get("PIXELA_GRAPH_ID")

today = datetime.now()

headers = {
    "X-USER-TOKEN": TOKEN,
}


# # Create User with POST.
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)


# # Create Graph with POST.
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Lecture Graph",
    "unit": "Min",
    "type": "int",
    "color": "sora"
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)


# # Create pixel with POST.
add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
add_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": str(int(float(input("How many minutes did you read today? ")))),
}
response = requests.post(url=add_pixel_endpoint, json=add_pixel_params, headers=headers)
print(response.text)


# # Update Pixel with PUT.
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20210412"
update_pixel_params = {
    "quantity": "100",
}
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)


# # Delete Pixel with DELETE.
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20210413"
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
