# **Essential Linux Commands for Production Support Roles in Investment Banking**

## **1. File and Directory Management**
- `ls -lah` → List directory contents in a human-readable format.
- `cd /var/log` → Navigate to the log directory.
- `pwd` → Display the current working directory.
- `cp file1.txt /backup/` → Copy file to a backup folder.
- `mv file1.txt file2.txt` → Rename or move a file.
- `rm -rf /tmp/test/` → Force delete a directory and its contents.
- `find / -name '*.log'` → Locate all `.log` files.

## **2. File Permissions and Ownership**
- **Access Levels:**
  - **Owner:** The user who owns the file.
  - **Group:** Users who are part of the file's group.
  - **Others:** All other users.
- **Permission Levels:**
  - **Read (`r`)** = 4
  - **Write (`w`)** = 2
  - **Execute (`x`)** = 1
- **Examples:**
  - `chmod 755 script.sh` → Owner: read/write/execute (7), Group: read/execute (5), Others: read/execute (5).
  - `chmod 640 file.txt` → Owner: read/write (6), Group: read (4), Others: no permission (0).
  - `chown user:group file.txt` → Change file ownership.
  - `umask 022` → Set default permissions for new files.

## **3. Process Management**
- `ps aux` → List all processes with details.
- `top` → Real-time process monitoring.
- `kill -9 12345` → Force kill a process by PID.
- `htop` → Interactive process viewer.
- `jobs -l` → List background jobs.
- `fg` → Bring a background job to the foreground.
- `bg` → Resume a background job.

## **4. Disk and File System Management**
- `df -h` → Check disk space usage.
- `du -sh /var/log` → Summarize disk usage.
- `mount /dev/sdb1 /mnt` → Mount a partition.
- `fsck` → Check and repair file system issues.
- `lsof -i :8080` → List processes using port 8080.

## **5. Networking**
- `ping google.com` → Test network connectivity.
- `netstat -tuln` → Show listening TCP/UDP ports.
- `ss -tulw` → Modern alternative to `netstat`.
- `curl -I http://example.com` → Fetch HTTP headers.
- `wget http://example.com/file.zip` → Download a file.
- `traceroute example.com` → Trace packet route to a destination.

## **6. Log Analysis**
- `cat /var/log/syslog` → View syslog content.
- `less /var/log/syslog` → Paginate through a log file.
- `tail -f /var/log/app.log` → Follow a live log file.
- `grep "error" /var/log/syslog` → Search logs for "error".
- `awk '{print $1, $2}' /var/log/syslog` → Extract columns from logs.
- `sed -i 's/error/warning/g' app.log` → Replace "error" with "warning" in logs.

## **7. System Monitoring**
- `uptime` → Check system uptime.
- `who` → List logged-in users.
- `vmstat` → Monitor CPU, memory, I/O performance.
- `free -m` → Show memory usage in MB.
- `iostat` → Monitor CPU and disk I/O performance.

## **8. Scheduling and Automation**
- `crontab -e` → Edit cron jobs.
  - Example: `0 2 * * * /path/to/backup.sh` (Run at 2 AM daily)
- `at 3:00 PM` → Schedule a one-time task.

## **9. User Management**
- `whoami` → Display the current user.
- `id` → Show user and group IDs.
- `adduser username` → Add a new user.
- `passwd username` → Change user password.
- `groups username` → List user groups.
- `sudo command` → Execute a command as another user.

## **10. Troubleshooting and Debugging**
- `dmesg` → View kernel messages.
- `strace -p <PID>` → Trace system calls of a process.
- `journalctl -u nginx` → View logs for a service.

## **11. Backup and Restore**
- `tar -cvf backup.tar /var/log` → Create a tar archive.
- `gzip backup.tar` → Compress a backup file.
- `rsync -av /source /destination` → Synchronize files between directories or servers.

## **12. Vim Text Editor**
- `vim filename` → Open a file in Vim.
- **Modes:**
  - **Insert Mode:** Press `i` to enter insert mode.
  - **Normal Mode:** Press `Esc` to return to normal mode.
  - **Command Mode:** Press `:` to enter command mode.
- **Basic Commands:**
  - `:w` → Save file.
  - `:q` → Quit.
  - `:wq` → Save and quit.
  - `:q!` → Quit without saving.
- **Editing:**
  - `dd` → Delete a line.
  - `yy` → Copy a line.
  - `p` → Paste.
  - `u` → Undo last change.
  - `/pattern` → Search for a pattern.
  - `:%s/old/new/g` → Replace all occurrences of "old" with "new".

---

This guide provides a **quick reference** to essential Linux commands for production support in investment banking. Mastering these will help you troubleshoot, manage, and optimize Linux systems efficiently.

