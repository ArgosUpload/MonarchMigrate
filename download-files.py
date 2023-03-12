import requests
import os

token = ""
cdn_domain = "" # The main domain you use on monarch, example "selfbot.gay"

response = requests.get(
    "https://api.monarchupload.cc/api/v2/getfiles/0",
    params={"query": None},
    headers={"authorization": token, "Sec-GPC": "1"}
)

if response.status_code == 200:
    for file_data in response.json()["data"]:
        url = f"https://{cdn_domain}/content/cdn/{file_data['Id']}/{file_data['Realid']}"
        file_response = requests.get(url)

        if file_response.status_code == 200:
            if not os.path.exists("results"):
                os.makedirs("results")

            with open(f"results/{file_data['Realid']}", "wb") as f:
                f.write(file_response.content)

            print(f"File saved: {file_data['Realid']}")
        else:
            print(f"Failed to download file: {file_data['Realid']}")
else:
    print("Failed to retrieve file data from API")
