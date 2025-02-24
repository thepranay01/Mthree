# Linux Commands and Concepts FAQ

## 1. `lsof` Command
- `lsof` (List Open Files) displays all open files by processes.
- Example: `lsof -i :80` lists processes using port 80.

## 2. SMTP Port Number & Hardlink vs Softlink
- **SMTP Port**: Default is `25`, with `587` for encrypted SMTP.
- **Hardlink**: Direct pointer to the same inode.
- **Softlink**: Points to another file (like a shortcut).

## 3. DNS Port
- **Port 53** for both TCP and UDP.

## 4. SSH Port
- **Port 22** (default, but can be changed in `/etc/ssh/sshd_config`).

## 5. Difference Between `scp` and `sftp`
- `scp`: Copies files securely over SSH.
- `sftp`: Interactive file transfer over SSH.

## 6. Inode and Process ID
- **Inode**: Metadata of a file (not the filename).
- **Process ID (PID)**: Unique identifier for running processes.

## 7. `top` Command
- Displays real-time system performance.
- Usage: `top`, `htop` (enhanced version).

## 8. `chmod` and `chown`
- `chmod`: Changes file permissions.
- `chown`: Changes file ownership.

## 9. `tail` Command
- Displays the last `n` lines of a file.
- Example: `tail -n 10 /var/log/syslog`

## 10. `find` Command
- Searches for files.
- Example: `find /home -name "*.txt"`

## 11. `grep` Command
- Searches for patterns in files.
- Example: `grep "error" /var/log/syslog`

## 12. What is RAM?
- Random Access Memory, volatile memory used for fast processing.

## 13. What is a File System?
- Organizes and stores data (ext4, NTFS, XFS, etc.).

## 14. `ps` Command
- Shows running processes.
- Example: `ps aux | grep nginx`

## 15. Passwordless Authentication
- Uses SSH keys instead of passwords (`ssh-keygen`, `ssh-copy-id`).

## 16. `scp` and `sftp`
- **`scp`**: Secure file copy.
- **`sftp`**: Secure FTP over SSH.

## 17. `scp` Command Example
- `scp file.txt user@host:/path/`

## 18. Add/Delete/Block User
- Add: `useradd username`
- Delete: `userdel username`
- Block: `passwd -l username`

## 19. Difference: `diff`, `cp`, `scp`
- `diff`: Compares files.
- `cp`: Copies locally.
- `scp`: Copies remotely.

## 20. `inode`
- Identifies file metadata uniquely.

## 21. Hardlink vs Softlink
- **Hardlink**: Same inode.
- **Softlink**: Different inode (symbolic link).

## 22. `mount` and `unmount`
- `mount /dev/sda1 /mnt`
- `umount /mnt`

## 23. `watch 'docker diff a2311'`
- Monitors changes in Docker container `a2311`.

## 24. Difference Between `su` and `sudo`
- `su`: Switch user.
- `sudo`: Run a command as another user (root).

## 25. `free -h`, `free -m`, `free`
- Displays memory usage.

## 26. `grub` Command
- Bootloader management (`update-grub`).

## 27. `netstat -nltp`
- Lists open network ports.

## 28. `free -m`
- Shows free and used memory in MB.

## 29. Ways to Create Files
- `touch file`
- `echo "data" > file`
- `cat > file`
- `vi file`
- `nano file`

## 30. `split`
- Splits large files into smaller ones.
- Example: `split -b 1M file.txt`

## 31. `shuf`
- Randomly shuffles file lines.
- Example: `shuf file.txt`

## 32. `alias`
- Shortcuts for commands.
- Example: `alias ll='ls -la'`

## 33. `df -h`
- Disk usage in human-readable format.

## 34. `lscpu`
- Displays CPU details.

## 35. `/proc/meminfo`
- Kernel memory usage information.

## 36. `$$`
- PID of the current shell.

## 37. `less` Command
- View large files efficiently.

## 38. `more` Command
- Similar to `less`, but less interactive.

## 39. `find` Command
- Searches for files.

## 40. `locate` Command
- Faster alternative to `find` (requires `updatedb`).

## 41. `dbupdate`
- Updates locate database (`updatedb`).

## 42. `sed` Command
- Stream editor for modifying text.

## 43. `traceroute` and `tracepath`
- Tracks network packet path.

## 44. `port`
- Endpoint for network communication.

## 45. `ping`
- Checks network connectivity.

## 46. `nested`
- Nested loops or directories.

## 47. `ssh`
- Secure Shell for remote access.

## 48. `telnet` (Port 23)
- Legacy remote login protocol.

## 49. FTP (Port 21)
- File Transfer Protocol.

## 50. HTTP & HTTPS
- **HTTP**: Port 80
- **HTTPS**: Port 443
- **DNS**: Port 53

## 51. Change SSH Port
- Modify `/etc/ssh/sshd_config`, change `Port`.

## 52. Email
- Uses SMTP (port 25/587).

## 53. Zombie Process
- A process that has completed but still occupies a PID.

## 54. Linux Partition
- Disk division (`/, /home, /var, /swap`).

## 55. `w` Command
- Shows logged-in users.

## 56. `ls -lart`
- Lists files sorted by time.

## 57. `nested` & `ss`
- **Nested**: Layered structure.
- **`ss`**: Socket statistics.

## 58. Log Management
- Use `logrotate`, `journalctl`.

## 59. Install Software on Multiple Servers
- Use Ansible, Puppet, or shell scripting.

## 60. `sed` Command
- Stream text editing.

## 61. `grep` Command
- Pattern matching in files.

## 62. Worked with Web Services?
- Yes, experience with REST APIs and web servers.

## Summary Table
| Topic | Command |
|--------|---------|
| File Search | `find`, `locate` |
| Network | `ping`, `traceroute`, `netstat` |
| Process Management | `ps`, `top`, `kill` |
| File Permissions | `chmod`, `chown` |
| User Management | `useradd`, `passwd -l` |
| System Monitoring | `w`, `df -h`, `free -m` |
| Security | `ssh`, `scp`, `sudo` |

## Best Practices
- Always check logs (`/var/log`).
- Use `sudo` cautiously.
- Automate tasks with scripts.

## Conclusion
This guide provides key Linux commands and concepts essential for system administration and DevOps tasks.

