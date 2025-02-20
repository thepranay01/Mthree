# **Linux Commands and Concepts - Quick Reference Guide**

## **1. What is Linux?**
Linux is a free and open-source operating system based on the Linux kernel. It is widely used in fields like **web and cloud computing, DevOps, system administration, and software development** due to its **stability, security, and flexibility**.

### **Accessing Linux**
- **Command-Line Interface (CLI):** Text-based interface for entering commands.
- **Graphical User Interface (GUI):** Mouse and keyboard-based interface.

## **2. Linux File System**
The Linux file system follows a hierarchical, tree-like structure starting from `/` (root directory).

### **Standard Directories**
- `/home/` → Contains user home directories.
- `/etc/` → System configuration files.
- `/var/` → Variable data (logs, cache, etc.).
- `/usr/` → User-related programs and data.
- `/bin/` → Essential executable programs.
- `/lib/` → Library files required for system execution.

### **Path Types**
- **Absolute Path:** Starts from `/`, e.g., `/home/user1/filename.txt`.
- **Relative Path:** Starts from current directory, e.g., `./filename.txt`.

## **3. Basic Navigation Commands**
- `pwd` → Display current directory.
- `ls -lah` → List directory contents in a detailed format.
- `cd /path/to/directory` → Change directory.
- `cd ..` → Move up one directory.
- `cd ~` → Move to home directory.
- `man <command>` → Show manual for a command.
- `history` → Display command history.

## **4. Managing Files and Directories**
### **Creating Files and Directories**
- `touch myfile.txt` → Create an empty file.
- `mkdir myfiles` → Create a directory.

### **Moving and Renaming Files**
- `mv file1.txt folder/` → Move a file.
- `mv file1.txt file2.txt` → Rename a file.

### **Copying Files and Directories**
- `cp file1.txt file2.txt` → Copy a file.
- `scp user@host:/path/file.txt .` → Securely copy a file.

### **Deleting Files and Directories**
- `rm file.txt` → Remove a file.
- `rmdir emptydir` → Remove an empty directory.
- `rm -r mydir/` → Remove a directory and its contents.

## **5. Viewing and Searching Files**
- `cat file.txt` → View entire file contents.
- `head -n 10 file.txt` → Show first 10 lines.
- `tail -n 10 file.txt` → Show last 10 lines.
- `less file.txt` → Scroll through file contents.
- `grep "pattern" file.txt` → Search for a pattern.
- `find /path -name "*.log"` → Search for files by name.
- `locate filename` → Quickly find files (requires `updatedb`).

## **6. File Permissions and Ownership**
- **Access Levels:**
  - **Owner:** User who created the file.
  - **Group:** Users in the same group.
  - **Others:** Everyone else.
- **Permission Levels:**
  - **Read (`r`=4), Write (`w`=2), Execute (`x`=1).**
- `chmod 755 script.sh` → Owner: `rwx` (7), Group: `rx` (5), Others: `rx` (5).
- `chown user:group file.txt` → Change file ownership.
- `umask 022` → Set default permissions.

## **7. Process Management**
- `ps aux` → List all running processes.
- `top` or `htop` → Monitor system resource usage.
- `kill -9 <PID>` → Force kill a process.
- `jobs` → Show background jobs.
- `fg` → Bring a background job to foreground.
- `bg` → Resume a background job in the background.

## **8. Disk and File System Management**
- `df -h` → Display disk usage.
- `du -sh /path` → Show directory size.
- `mount /dev/sdb1 /mnt` → Mount a partition.
- `fsck /dev/sda1` → Check and repair filesystem.

## **9. Editing Files in Linux**
### **Vim Editor Basics**
- `vim filename` → Open file in Vim.
- `i` → Insert mode.
- `Esc` → Return to command mode.
- `:wq` → Save and exit.
- `:q!` → Quit without saving.
- `dd` → Delete a line.
- `yy` → Copy a line.
- `p` → Paste a line.
- `:%s/old/new/g` → Replace all occurrences of "old" with "new".

## **10. Special Operators in Linux**
- `|` → Pipe output of one command to another (`ls | head -3`).
- `>` → Redirect output to a file (`echo "Hello" > file.txt`).
- `>>` → Append output to a file (`echo "Append" >> file.txt`).
- `<` → Redirect input (`sort < file.txt`).

## **11. Sed & Awk for Text Processing**
### **Sed - Stream Editor**
- `sed 's/old/new/g' file.txt` → Replace text.
- `sed -n '1,5p' file.txt` → Print lines 1 to 5.
- `sed '/^$/d' file.txt` → Remove empty lines.

### **Awk - Pattern Scanning**
- `awk '{print $1, $2}' file.txt` → Print first two columns.
- `awk -F, '{print $1}' file.csv` → Use custom field separator.
- `awk '/pattern/ {print}' file.txt` → Print lines matching a pattern.

## **12. Scheduling Tasks**
### **Using Cron Jobs**
- `crontab -e` → Edit scheduled tasks.
- **Example:** `0 2 * * * /path/to/script.sh` → Run script daily at 2 AM.
- `crontab -l` → List current cron jobs.
- **Syntax:** `minute hour day month day-of-week command`
  - `*/5 * * * * script.sh` → Runs script every 5 minutes.
  - `0 0 * * 0 script.sh` → Runs script every Sunday at midnight.

### **Using the at Command**
- `at 3:00 PM` → Schedule a one-time task.
- `at -l` → List scheduled jobs.
- `atrm <job_number>` → Remove a scheduled job.

## **13. Searching and Finding Files**
- `locate filename` → Fast search (requires `updatedb`).
- `find /path -name "file.txt"` → Search for a specific file.
- `find / -size +1G` → Find files larger than 1GB.
- `find / -perm 644` → Find files with specific permissions.

## **14. User Management**
- `whoami` → Show current user.
- `id` → Display user and group ID.
- `adduser username` → Create a new user.
- `passwd username` → Change user password.
- `groups username` → List user's groups.
- `sudo command` → Run a command as root.

---

This **Linux Quick Reference Guide** covers essential commands for **system administration, DevOps, and production support**. Mastering these commands will help troubleshoot, manage, and optimize Linux environments efficiently. 🚀

