import requests

BASE = "http://127.0.0.1:5000"

print("\n--- GET all users ---")
print(requests.get(f"{BASE}/users").json())

print("\n--- GET user 1 ---")
print(requests.get(f"{BASE}/users/1").json())

print("\n--- POST new user ---")
new_user = {"name": "Karen", "age": 22}
print(requests.post(f"{BASE}/users", json=new_user).json())

print("\n--- PUT update user 2 ---")
updated = {"name": "Vache Updated", "age": 31, 'hey':'aaa'}
print(requests.put(f"{BASE}/users/2", json=updated).json())

print("\n--- DELETE user 1 ---")
print(requests.delete(f"{BASE}/users/1").json())
