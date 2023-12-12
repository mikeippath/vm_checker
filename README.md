# vm_checker

## Project Overview

This repository contains scripts for interacting with Virtuozzo pods to retrieve information about servers and track changes over time. The main components of the project include:

1. **get_tokens.py:**
   - File containing functions to request an API token from Virtuozzo pods.

2. **vm_list.py:**
   - Contains a function, `list_vms()`, that utilizes the `get_tokens()` function.
   - Iterates over each pod to retrieve server names and stores them in a file called `all_servers_dump_new.json`.

3. **compare.py:**
   - Script for comparing two JSON files (`all_servers_dump_old.json` and `all_servers_dump_new.json`).
   - Outputs a file named `server_changes.json` containing added or removed servers from each pod.
   - Renames `all_servers_dump_new.json` to `all_servers_dump_old.json` after the comparison.
   - Generates a `.csv` file called `servers.csv` containing a list of web servers from each pod.
  
4. **Example Output Files:**
   - `all_servers_dump_old.json`: Master list of all servers and their pods in JSON format.
   - `server_changes.json`: Lists added or removed servers from each pod.
   - `servers.csv`: CSV file with a list of web servers from each pod.
   
5. **Integration with alert_feeder:**
   - The script's output is designed to be served by `alert_feeder`, a Flask app deployed for upstream use with services like Zabbix.

## Usage

1. Run `get_tokens.py` to obtain API tokens from Virtuozzo pods.
2. Execute `vm_list.py` to gather server names and update `all_servers_dump_new.json`.
3. Run `compare.py` to compare old and new server lists, update `server_changes.json`, and generate `servers.csv`.
4. Use the outputs with `alert_feeder` for integration with Zabbix or other services.

## Files

- `get_tokens.py`
- `vm_list.py`
- `compare.py`
- `all_servers_dump_old.json` (example)
- `all_servers_dump_new.json` (example)
- `server_changes.json` (example)
- `servers.csv` (example)

## Notes

- Improvements needed: Better error handling around API endpoints, credentials, and other configurations in the scripts.
- TPWM integration.
- Historical logs of servers added or removed with date/time.
- Example output files are provided for reference.
  
Feel free to contribute, report issues, or suggest improvements.