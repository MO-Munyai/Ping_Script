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


### 3. Check for Duplicates

Run [`dupl_test.py`](dupl_test.py) to check for duplicate IPs:

- Within [`active_ip_list.txt`](active_ip_list.txt)
- Within [`inactive_ip_list.txt`](inactive_ip_list.txt)
- Between both files

```sh
python dupl_test.py
```

## Files

- [`ip_list.txt`](ip_list.txt): Input your IP addresses here.
- [`ping.py`](ping.py): Script to ping IPs and separate them into active/inactive.
- [`active_ip_list.txt`](active_ip_list.txt): Automatically generated list of active IPs.
- [`inactive_ip_list.txt`](inactive_ip_list.txt): Automatically generated list of inactive IPs.
- [`dupl_test.py`](dupl_test.py): Script to check for duplicate IPs.

## Requirements

- Python 3+

## Notes

- Make sure to input your IPs in [`ip_list.txt`](ip_list.txt) before running the scripts.
- The scripts are designed for cross-platform use (Windows, Linux, macOS).
