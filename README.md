# CheckNetworkStorage
The script in this project is meant to auto-mount a windows network drive to a raspberry pi storage devices. It also handles disconnection to this network drive.
Using rasbian crontabs `crontab -e` the script is run every minute to check if the network drive is mounted. If it is not mounted, it will attempt to mount it. If it is mounted, it will check if it is still connected. If it is not connected, it will attempt to unmount it.

Nevertheless, you need to have added your network drive to the fstab file `/etc/fstab`. You can do this by adding the following line to the fstab file:
```
//192.168.xx.xxx/Shared_folder_in_the_server /mnt/<folder_to _mount_to> cifs username=<user_in_server>,password=<password_for_server_user>,rw,uid=1000,users,gid=1000,file_mode=0777,dir_mode=0777,vers=3.0 0 0
```