# IP Ping & Duplicate Checker

This project provides two Python scripts for managing and analyzing lists of IP addresses:

- **ping.py**: Pings a list of IPs and separates them into active and inactive lists.
- **dupl_test.py**: Checks for duplicate IPs within and between the active and inactive lists.

## Usage

### 1. Prepare Your IP List

Before running the scripts, input the IP addresses you want to check into the [`ip_list.txt`](ip_list.txt) file. Enter one IP address per line.

### 2. Run the Ping Script

Execute [`ping.py`](ping.py) to ping all IPs in [`ip_list.txt`](ip_list.txt). The script will:

- Print the number of active and inactive IPs.
- Save active IPs to [`active_ip_list.txt`](active_ip_list.txt).
- Save inactive IPs to [`inactive_ip_list.txt`](inactive_ip_list.txt).

```sh
python ping.py
```
