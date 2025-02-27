# 🧪 Activity: Linux Networking and Sys Admin

## Completion Requirements

Welcome to our hands-on activity for mastering Linux Networking and System Administration! 🎓 In this activity, you'll dive into essential commands and techniques that every Linux sysadmin should know. Let's get started!

### Memory Management

Memory is the lifeblood of your applications. Understanding how to monitor and manage it effectively is crucial.

**Step 1:** Check your machine's memory summary.

```bash
cat /proc/meminfo
```

**Key Values to Observe:**
- **MemTotal**: Total RAM installed.
- **MemFree**: Currently unused RAM.
- **MemAvailable**: Estimated RAM available for new applications.

Alternatively, use:

```bash
free --mega -h # --mega for megabytes, -h for human readable.
# man free # for options
```

**Want to watch it live?** Use:

```bash
watch "free --bytes"
```

or

```bash
vmstat 1
```

**Pro Tip:** Use `ps` to see which processes are hogging your memory.

```bash
ps aux --sort -rss # Sort by memory usage.
ps aux --sort -%mem # Sort by percentage memory usage.
ps -eo user,pid,%mem,stat,cmd --sort=-%mem # Custom output.
ps aux --sort -%cpu # Sort by CPU usage.
ps aux --forest # View process tree.
watch 'ps aux --sort -%mem | head' # Refresh every 2 seconds.
top # Interactive process viewer.
```

### Understanding Inodes

Inodes are like the DNA of your files, storing crucial metadata and pointers to data blocks.

**Example:** Create an 8 KB file.

```bash
dd if=/dev/urandom of=8kb_file bs=1K count=8
```

**Inspect the file:**

```bash
stat 8kb_file
```

**Check inode usage:**

```bash
df -i
```

### Network Diagnostic Tools

Networking issues? Fear not! These tools will help you diagnose and troubleshoot.

**Ping:** Test connectivity.

```bash
ping 8.8.8.8
ping -c 4 8.8.8.8 # Send 4 packets.
```

**nslookup:** Query DNS.

```bash
nslookup example.com
nslookup 8.8.8.8 # Reverse lookup.
```

**traceroute:** Trace packet path.

```bash
traceroute example.com
```

**dig:** Detailed DNS information.

```bash
dig example.com
dig example.com A # Query specific record type.
dig example.com MX
dig -x 8.8.8.8 # Reverse DNS lookup.
```

**curl:** Transfer data.

```bash
curl https://example.com
```

**Advanced Usage:**

```bash
# Save output to file
curl -o index.html https://example.com

# Follow redirects
curl -L -o redirected.html https://example.com

# Send POST data
curl -X POST -d 'username=user&password=pass' https://example.com/login -f

# Include headers or cookies
curl -H "Authorization: Bearer token" https://api.example.com/data
curl -b "cookie1=value1; cookie2=value2" https://example.com
```

### Monitoring Open Ports and Network Traffic

Knowing what's listening on your machine is crucial for security.

**Open Ports:**

```bash
sudo lsof -i -P # List open ports.
```

**Monitor Network Traffic:**

```bash
netstat -c # Live view.
ss # Similar to netstat.
```

### Private IP and Subnet

Every network interface tells a story. Let's read it.

**View network interfaces:**

```bash
ifconfig
```

**Key Terms:**
- **inet**: Assigned IP address.
- **netmask**: Determines the network and host parts of the IP address.
- **broadcast**: Address to send data to all devices on the network.

### Summary

In this activity, we've explored essential Linux commands and techniques for effective system administration and network diagnostics. Let’s recap what we’ve learned:

- **Memory Management**:
  - Monitoring Memory Usage: Commands like `cat /proc/meminfo` and `free –mega -h` provide insights into total, free, and available memory.
  - Process Management: Using `ps` to sort processes by memory (`%mem`) and CPU (`%cpu`) usage helps identify resource-intensive applications.

- **Inodes**:
  - Understanding Inodes: Files and directories on Linux are managed through inodes, which store metadata and data block pointers. The `stat` command reveals inode details.
  - Checking Inode Usage: `df -i` displays inode usage statistics, crucial for managing filesystem limits.

- **Network Diagnostics**:
  - Ping: Uses ICMP to test network connectivity (`ping`).
  - nslookup: Queries DNS for IP address mapping (`nslookup`).
  - traceroute: Traces the path packets take to a destination (`traceroute`).
  - dig: Provides detailed DNS information (`dig`).
  - Curl: HTTP/FTP Data Transfer: `curl` is versatile for retrieving and sending data over various protocols (`curl https://example.com`).
  - Advanced Usage: Includes saving output to files (`curl -o index.html`), following redirects (`curl -L`), and sending POST data (`curl -X POST -d ‘data’`).

- **Monitoring and Administration**:
  - Open Ports: `lsof -i -P` lists open ports and associated processes, crucial for network security.
  - Monitoring Network Traffic: Commands like `netstat -c` and `ss` provide real-time network connection details.
  - Private IP and Subnet: `ifconfig` displays network interface details including IP addresses, netmasks, and broadcast addresses.

### Exercise

#### Install stress:

First, search for the stress package using `dnf search` and then install it.

```bash
dnf search stress
sudo dnf install stress
```

#### Capture free memory before starting the stress test:

Use the free command to retrieve the amount of free memory in megabytes and save it to a file named `free_mega_before_stress`:

```bash
free --mega # make sure output aligns with awk
free --mega | awk 'NR==2 {print $4}' > free_mega_before_stress
# NR==2 is for row 2 and $4 is col 4
```

#### Perform the stress test:

Execute the stress command to stress the system with virtual memory for 300 seconds:

```bash
stress --vm 1 --vm-bytes 512M --vm-keep -t 300s &
# press enter
```

#### Capture free memory during the stress test:

While the stress test is running, again use the free command to get the amount of free memory in megabytes and save it to a file named `free_mega_during_stress`:

```bash
free --mega
free --mega | awk 'NR==2 {print $4}' > free_mega_during_stress
```

#### Capture the top 5 memory-consuming processes during the stress test:

Use the ps command to retrieve the PID, %mem, %cpu, and CMD of the 5 processes consuming the most memory:

```bash
ps -eo pid,%mem,%cpu,cmd --sort=-%mem | head -n 6 
```

#### Use BC to calculate the difference between how much memory the stress test used:

```bash
bc <<< "$(cat free_mega_before_stress) - $(cat free_mega_during_stress)"
```

