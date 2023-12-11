import json
import os
import csv
from vm_list import list_vms

list_vms()

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def compare_servers(old_servers, new_servers):
    added_servers = {pod: list(set(new_servers[pod]) - set(old_servers.get(pod, []))) for pod in new_servers}
    removed_servers = {pod: list(set(old_servers.get(pod, [])) - set(new_servers[pod])) for pod in old_servers}
    return added_servers, removed_servers

def remove_and_rename(old_file_path, new_file_path):
    os.remove(old_file_path)
    os.rename(new_file_path, old_file_path)

# File paths
old_file_path = 'all_servers_dump_old.json'
new_file_path = 'all_servers_dump_new.json'

# Load old and new server data
old_servers = load_json(old_file_path)
new_servers = load_json(new_file_path)

# Extract server names
all_server_names = set()
for pod_servers in new_servers.values():
    all_server_names.update(pod_servers)

# Writing server names to CSV
csv_file_path = 'servers.csv'
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for server_name in all_server_names:
        if server_name.startswith('Websrv'):
            server_name = f'{server_name},zfs1,w'
            writer.writerow([server_name])

with open('servers.csv', 'r') as f:
    lines = f.readlines()

# Remove double quotes from each line
lines = [line.replace('"', '') for line in lines]

# Write the modified lines back to the file
with open('servers.csv', 'w') as f:
    f.writelines(lines)

# Compare servers
added_servers, removed_servers = compare_servers(old_servers, new_servers)

# Combine the data into a single dictionary
result_data = {
    "Added Servers": added_servers,
    "Removed Servers": removed_servers
}

# Writing the combined data to the JSON file
with open("server_changes.json", "w") as json_file:
    json.dump(result_data, json_file, indent=2)

# Remove old file and rename new file
remove_and_rename(old_file_path, new_file_path)

