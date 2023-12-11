import requests
import json
from get_tokens import get_tokens

def list_vms():

    # Get tokens for each pod
    pod_tokens = get_tokens()

    # Define the URLs for retrieving server names
    pod_urls = {
        "pod1": "https://172.19.100.10:8774/v2.1/9931d7631149484b96c5d6ae9266c86e/servers?all_tenants",
        "pod2": "https://172.19.111.100:8774/v2.1/d0236e37ec654bb9bcfca85645d5cb6d/servers?all_tenants",
        "pod3": "https://172.19.113.100:8774/v2.1/09dc4b54fbd94bb6b5d60d486df62811/servers?all_tenants",
        "pod4": "https://172.19.108.10:8774/v2.1/5dcda23cb9bd4718b32610bbe18a1382/servers?all_tenants"
    }

    # Dictionary to store all server names
    all_server_names = {}

    # Iterate over pods and get server names
    for pod_name, token in pod_tokens.items():
        print(pod_tokens.items())
        headers = {
            'Content-Type': 'application/json',
            'X-Auth-Token': f'{token}'
        }

        url = pod_urls[pod_name]
        response = requests.get(url, headers=headers, verify=False)

        if response.status_code == 200:
            response_json = response.json()
            # Extracting names from the 'servers' list
            names = [server['name'] for server in response_json['servers']]
            # Store names in the dictionary with pod_name as the key
            all_server_names[pod_name] = names
        else:
            print(f"Error: {response.status_code}\n{response.text}")

    # Save the dictionary to a file
    with open('all_servers_dump_new.json', 'w') as file:
        json.dump(all_server_names, file, indent=2)

    # Load the JSON file
    with open('all_servers_dump_new.json', 'r') as file:
        all_server_names = json.load(file)

    # Calculate the total number of servers
    total_servers = sum(len(names) for names in all_server_names.values())

    print(f"Total number of servers: {total_servers}")
