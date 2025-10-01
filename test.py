import requests

payload = {
    "file_path": "/mihaiciorobitca007@gmail.com/generated_images/"
}

print(requests.post("https://pcloud-get-code.vercel.app/", json=payload))