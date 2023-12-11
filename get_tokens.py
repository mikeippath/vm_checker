import requests
import json

def authenticate(pod_url, pod_key, headers):
    auth_url = f"{pod_url}/v3/auth/tokens"

    auth_data = {
        "auth": {
            "identity": {
                "methods": ["password"],
                "password": {
                    "user": {
                        "name": "admin",
                        "domain": {
                            "id": "default"
                        },
                        "password": pod_key
                    }
                }
            },
            "scope": {
                "project": {
                    "name": "admin",
                    "domain": {
                        "id": "default"
                    }
                }
            }
        }
    }

    response = requests.post(auth_url, headers=headers, data=json.dumps(auth_data), verify=False)

    if response.status_code == 201:
        token = response.headers.get("X-Subject-Token")
        return token
    else:
        print(f"Failed to authenticate to {pod_url}. Status code: {response.status_code}")
        return None

def get_tokens():
    pod_urls = {
        "pod1": "https://172.19.100.10:5000",
        "pod2": "https://172.19.111.100:5000",
        "pod3": "https://172.19.113.100:5000",
        "pod4": "https://172.19.108.10:5000"
    }

    pod_keys = {
        "pod1": "l5%Sc8?6$t9#1!",
        "pod2": "Badlands123.",
        "pod3": "RedRocks123..",
        "pod4": "MtHelen123.."
    }

    headers = {'Content-Type': 'application/json'}

    pod_tokens = {}

    for pod_name, pod_url in pod_urls.items():
        pod_key = pod_keys.get(pod_name, "")
        token = authenticate(pod_url, pod_key, headers)

        if token:
            pod_tokens[pod_name] = token

    return pod_tokens
