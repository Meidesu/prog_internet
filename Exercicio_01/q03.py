import requests

url = "https://memetemplates.in/uploads/1650185861.jpeg"



response =  requests.get(url)

if response.status_code == 200:
    data = response.content

    with open("q2_megamind.png", "wb") as file:
        file.write(data)