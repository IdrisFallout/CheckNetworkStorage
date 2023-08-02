import subprocess

ip_address = "192.168.43.138"

def ping():
    try:
        # Run 'ping' command to check if the IP address is reachable
        subprocess.run(['ping', '-c', '1', '-W', '1', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except subprocess.CalledProcessError:
        # Handle the case where the 'ping' command fails (Network share disconnected)
        return False

    return True

def check_mounted(mount_point):
    try:
        # Run 'mount' command and capture its output
        output = subprocess.check_output(['mount'])
        # Check if the mount_point is present in the output
        is_mounted = mount_point in output.decode('utf-8')
        if not is_mounted:
            return False  # Folder is not mounted
    except subprocess.CalledProcessError:
        # Handle the case where the 'mount' command fails
        return False

    return True  # Folder is mounted and IP address is reachable

def mount_network_drive(mount_point):
    try:
        # Run the 'mount' command with the specified mount point
        subprocess.check_call(['/bin/mount', mount_point])
    except subprocess.CalledProcessError as e:
        # Handle the case where the 'mount' command fails
        print(f"Error: Failed to mount {mount_point}. Error: {e}")

def main():
    network_drive = "/home/idrisfallout/Documents/network_storage"
    if not ping():
        print(f"Network share not reachable: {ip_address}")
        return
    if not check_mounted(network_drive):
        print(f"Network drive not mounted. Mounting {network_drive}...")
        mount_network_drive(network_drive)
    else:
        print(f"Network drive already mounted: {network_drive}")

if __name__ == "__main__":
    main()