import subprocess
import platform

def ping_ip(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip]
    
    try:
        output = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return output.returncode == 0
    except Exception as e:
        print(f"Error pinging {ip}: {e}")
        return False

def check_ips(ip_list):
    active_ips = []
    inactive_ips = []

    for ip in ip_list:
        if ping_ip(ip):
            active_ips.append(ip)
        else:
            inactive_ips.append(ip)

    return active_ips, inactive_ips

with open("ip_list.txt") as f:
    ips_to_check = [line.strip() for line in f.readlines()]

active, inactive = check_ips(ips_to_check)

print(f"Total IPs pinged: {len(ips_to_check)}")

print(f"\nActive IPs: {len(active)}")
print("✅ Active IPs:")
print(active)


print(f"\nInactive IPs: {len(inactive)}")
print("❌ Inactive IPs:")
print(inactive)


with open("active_ip_list.txt", "a") as f:
    for ip in active:
        f.write(ip + "\n")

with open("inactive_ip_list.txt", "a") as f:
    for ip in inactive:
        f.write(ip + "\n")

print("\nResults saved to active_ip_list.txt and inactive_ip_list.txt")