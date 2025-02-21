![Linux Logo](https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png)

# Intermediate Linux Commands

## 1. How would you create a new user account in Linux?
To create a new user account, use the `useradd` command:
```bash
sudo useradd -m username
```
The `-m` flag creates a home directory for the user. You can set a password using:
```bash
sudo passwd username
```

## 2. Explain the difference between relative and absolute paths.
- **Absolute Path**: Starts from the root (`/`), e.g., `/home/user/file.txt`.
- **Relative Path**: Starts from the current directory, e.g., `./file.txt`.

## 3. What command would you use to change file ownership?
Use the `chown` command:
```bash
sudo chown new_owner:new_group filename
```

## 4. How can you schedule a task to run automatically at a specific time?
Using `cron`, edit the crontab:
```bash
crontab -e
```
Example: Run a script daily at 2 AM:
```bash
0 2 * * * /path/to/script.sh
```

## 5. Describe how you would compress and decompress files in Linux.
- Compress using `tar` and `gzip`:
  ```bash
  tar -czvf archive.tar.gz directory/
  ```
- Decompress:
  ```bash
  tar -xzvf archive.tar.gz
  ```

## 6. What's the purpose of the 'grep' command and how would you use it?
`grep` searches for patterns in text:
```bash
grep 'error' logfile.txt
```

## 7. How do you check and manage running processes in Linux?
- Use `ps` to list processes:
  ```bash
  ps aux
  ```
- Use `top` or `htop` for real-time monitoring:
  ```bash
  top
  ```
- Kill a process:
  ```bash
  kill PID
  ```

## 8. Explain how to set up a basic firewall using iptables.
Block all incoming traffic and allow outgoing:
```bash
sudo iptables -P INPUT DROP
sudo iptables -P OUTPUT ACCEPT
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
```

## 9. What command would you use to check system resource usage?
Use `free`, `vmstat`, or `top`:
```bash
free -m
vmstat 5
```

## 10. How do you create and manage symbolic links?
Create a symlink:
```bash
ln -s /path/to/file linkname
```
Remove it:
```bash
rm linkname
```

## 11. Describe the process of mounting and unmounting file systems.
- Mount a filesystem:
  ```bash
  sudo mount /dev/sdb1 /mnt
  ```
- Unmount:
  ```bash
  sudo umount /mnt
  ```

## 12. What's the difference between 'sudo' and 'su' commands?
- `sudo`: Runs a single command as root.
- `su`: Switches to root or another user session.

## 13. How would you search for files larger than a specific size?
```bash
find / -type f -size +100M
```

## 14. Explain how to redirect output to a file and append to an existing file.
- Redirect:
  ```bash
  ls > output.txt
  ```
- Append:
  ```bash
  ls >> output.txt
  ```

## 15. What command would you use to view real-time log entries?
```bash
tail -f /var/log/syslog
```

## 16. How do you check and modify file permissions recursively?
- Check:
  ```bash
  ls -lR
  ```
- Modify:
  ```bash
  chmod -R 755 directory/
  ```

## 17. Describe how to use the 'find' command to locate files.
Find files by name:
```bash
find /path -name "file.txt"
```

## 18. What's the purpose of the '/etc/fstab' file and how would you edit it?
- Stores filesystem mount information.
- Edit with:
  ```bash
  sudo nano /etc/fstab
  ```

## 19. How can you check and manage available swap space?
Check swap:
```bash
free -h
```
Add swap:
```bash
sudo fallocate -l 1G /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

## 20. Explain how to use 'tar' for backing up and restoring files.
- Backup:
  ```bash
  tar -cvf backup.tar /path/to/files
  ```
- Restore:
  ```bash
  tar -xvf backup.tar
  ```


