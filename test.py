import requests

payload = {
    "file_path": "/mihaiciorobitca007@gmail.com/generated_images/fc07acbb-1bd3-4a2a-afbc-6d8c7650277d.jpeg"
}

print(requests.post("https://pcloud-get-code.vercel.app/get_code", json=payload).content)