# dupl_test.py

"""
This script checks for duplicate IPs within 'active_ip_list.txt', within 'inactive_ip_list.txt', and between the two files.
"""

def read_ips(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def find_duplicates(ip_list):
    seen = set()
    duplicates = set()
    for ip in ip_list:
        if ip in seen:
            duplicates.add(ip)
        else:
            seen.add(ip)
    return duplicates

def main():
    active_ips = read_ips('active_ip_list.txt')
    inactive_ips = read_ips('inactive_ip_list.txt')

    # Duplicates within each file
    active_dups = find_duplicates(active_ips)
    inactive_dups = find_duplicates(inactive_ips)

    # Duplicates between files
    between_dups = set(active_ips) & set(inactive_ips)

    if active_dups:
        print(f"Duplicate IPs in active_ip_list.txt: {sorted(active_dups)}")
    else:
        print("No duplicates in active_ip_list.txt.")

    if inactive_dups:
        print(f"Duplicate IPs in inactive_ip_list.txt: {sorted(inactive_dups)}")
    else:
        print("No duplicates in inactive_ip_list.txt.")

    if between_dups:
        print(f"Duplicate IPs between both files: {sorted(between_dups)}")
    else:
        print("No duplicates between the two files.")

if __name__ == "__main__":
    main()
