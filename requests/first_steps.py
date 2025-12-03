import requests

print("\n--- GET Example ---")
get_url = "https://jsonplaceholder.typicode.com/posts"
get_response = requests.get(get_url)
print("Status:", get_response.status_code)
print("First 2 posts:", get_response.json()[:2])


print("\n--- GET with Query Params ---")
cat_url = "https://catfact.ninja/facts"
params = {"limit": 3}
cat_response = requests.get(cat_url, params=params)
print(cat_response.json())


print("\n--- POST Example ---")
post_url = "https://jsonplaceholder.typicode.com/posts"
payload_post = {
    "title": "My test post",
    "body": "Teaching Python requests!",
    "userId": 1
}
post_response = requests.post(post_url, json=payload_post)
print("Status:", post_response.status_code)
print(post_response.json())


print("\n--- PUT Example ---")
put_url = "https://jsonplaceholder.typicode.com/posts/1"
payload_put = {
    "id": 1,
    "title": "Updated title",
    "body": "Updated body",
    "userId": 1
}
put_response = requests.put(put_url, json=payload_put)
print("Status:", put_response.status_code)
print(put_response.json())


print("\n--- DELETE Example ---")
delete_url = "https://jsonplaceholder.typicode.com/posts/1"
delete_response = requests.delete(delete_url)
print("Status:", delete_response.status_code)


print("\n--- Error Handling Example ---")
try:
    resp = requests.get(get_url, timeout=5)
    resp.raise_for_status()
    print("Success example response:", resp.json()[:1])
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print("Error:", e)
