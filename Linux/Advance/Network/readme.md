# 🌐 Detailed Notes on Linux Networking Commands

## 📢 Introduction
Linux networking commands are essential for managing and troubleshooting network configurations, performance, and security. These commands help system administrators configure interfaces, diagnose connectivity issues, and monitor network traffic efficiently. This document provides a comprehensive guide to essential Linux networking commands, explaining their purpose and usage in detail.

---

## 1️⃣ IP Command

### 📌 Overview
The `ip` command is part of the **iproute2** package and is used for network and routing configuration. It replaces older commands like `ifconfig` and `route`. It allows administrators to configure IP addresses, interfaces, routes, and rules efficiently.

### 📌 Key Subcommands
- **`ip link`**: Used to configure, add, and delete network interfaces.
- **`ip address`**: Used to display, add, or delete IP addresses.
- **`ip route`**: Used to display or manipulate the routing table.

### 📌 Why Use It?
The `ip` command provides a powerful and flexible way to manage network interfaces and routing compared to legacy commands. It supports IPv4 and IPv6 and offers better debugging capabilities.

---

## 2️⃣ nslookup

### 📌 Overview
The `nslookup` command is used to query **Domain Name System (DNS)** servers to resolve domain names to IP addresses and vice versa. It helps diagnose DNS issues and check domain configurations.

### 📌 Why Use It?
- Ensures correct DNS resolution of domain names.
- Helps troubleshoot DNS server issues.
- Checks multiple DNS record types such as **A, MX, CNAME, and TXT**.

---

## 3️⃣ Ping

### 📌 Overview
The `ping` command tests network connectivity between two hosts by sending **ICMP Echo Request** packets. It is one of the most commonly used commands for network troubleshooting.

### 📌 Why Use It?
- Checks if a host is reachable over the network.
- Measures packet loss and network latency.
- Helps detect network congestion or misconfigurations.

### 📌 Key Options
- `-c [number]`: Sends a specified number of ping requests.
- `-s [size]`: Specifies packet size for each request.
- `-t [ttl]`: Sets the maximum time-to-live (TTL) value for packets.

---

## 4️⃣ iperf

### 📌 Overview
The `iperf` command is used to measure **network bandwidth and performance** between two hosts. It is widely used for testing network speed and throughput.

### 📌 Why Use It?
- Determines available network bandwidth.
- Diagnoses network performance bottlenecks.
- Tests TCP and UDP transmission quality.

### 📌 Key Usage
- Runs in **server mode** (`iperf -s`) on one host.
- Runs in **client mode** (`iperf -c [server_ip]`) to measure network performance.

---

## 5️⃣ Traceroute

### 📌 Overview
The `traceroute` command traces the **path packets take** to reach a destination. It helps identify routing issues and detect delays at different network hops.

### 📌 Why Use It?
- Diagnoses network path and latency issues.
- Identifies where network packets are being dropped or delayed.
- Helps troubleshoot **ISP and firewall** routing problems.

### 📌 Key Options
- `-m [hops]`: Sets the maximum number of hops.
- `-n`: Disables hostname resolution for faster results.

---

## 6️⃣ tcpdump

### 📌 Overview
The `tcpdump` command is a **packet analyzer** used to capture and analyze network traffic in real time. It is a powerful tool for debugging network security and performance issues.

### 📌 Why Use It?
- Captures network packets for detailed inspection.
- Analyzes network activity and potential threats.
- Helps debug **firewall rules and network protocols**.

### 📌 Key Options
- `-i [interface]`: Specifies the network interface to capture packets from.
- `-c [count]`: Captures a specified number of packets.
- `-w [file]`: Saves the captured packets to a file for later analysis.

---

## 7️⃣ netstat

### 📌 Overview
The `netstat` command displays **network connections, routing tables, and interface statistics**. It is useful for monitoring active connections and troubleshooting network issues.

### 📌 Why Use It?
- Shows open ports and established connections.
- Lists network interfaces and their traffic statistics.
- Displays **TCP, UDP, and ICMP traffic details**.

### 📌 Key Options
- `-t`: Displays only TCP connections.
- `-u`: Displays only UDP connections.
- `-r`: Shows the routing table.
- `-p`: Displays the process using each network connection.

---

## 8️⃣ ss

### 📌 Overview
The `ss` command is a **modern replacement for netstat**, providing faster and more detailed socket statistics.

### 📌 Why Use It?
- Offers real-time connection monitoring.
- Provides faster performance compared to `netstat`.
- Displays active and listening sockets efficiently.

### 📌 Key Options
- `-t`: Shows TCP sockets.
- `-u`: Shows UDP sockets.
- `-a`: Displays all sockets (listening and established).

---

## 9️⃣ telnet

### 📌 Overview
The `telnet` command is used to establish remote connections and test connectivity to specific network ports.

### 📌 Why Use It?
- Tests if a remote service is **reachable on a specific port**.
- Helps diagnose **firewall rules and blocked ports**.
- Useful for **manual testing of mail and web servers**.

---

## 🔟 dig

### 📌 Overview
The `dig` command queries **DNS records** and is used to retrieve domain name information.

### 📌 Why Use It?
- Retrieves **A, MX, CNAME, and TXT records**.
- Helps diagnose **DNS misconfigurations**.
- Tests domain resolution with multiple DNS servers.

---



## 1️⃣1️⃣ ifconfig

### 📌 Overview
The `ifconfig` command is used to configure, manage, and display network interface information in Linux. Although largely replaced by the `ip` command, it is still found in many older systems.

### 📌 Why Use It?
- Displays network interface details such as IP addresses, MAC addresses, and netmasks.
- Enables or disables network interfaces.
- Configures IP addresses and netmasks manually.

### 📌 Key Options
- `ifconfig eth0`: Shows details of a specific interface.
- `ifconfig eth0 up/down`: Activates or deactivates an interface.
- `ifconfig eth0 192.168.1.100 netmask 255.255.255.0`: Assigns an IP and netmask.

---

## 1️⃣2️⃣ ssh

### 📌 Overview
The `ssh` command is used for securely accessing remote machines over an encrypted connection. It replaces insecure protocols like `telnet` for remote administration.

### 📌 Why Use It?
- Provides encrypted communication between local and remote systems.
- Allows remote execution of commands.
- Supports secure file transfer using SCP and SFTP.

### 📌 Key Options
- `ssh user@remote_host`: Connects to a remote host.
- `ssh -p 2222 user@remote_host`: Specifies a custom port.
- `ssh -X user@remote_host`: Enables X11 forwarding for GUI applications.

---

## 1️⃣3️⃣ Additional Networking Commands

### 📌 tracepath
The `tracepath` command is similar to `traceroute`, but it does not require root privileges. It is used to track the path packets take to reach a destination.

### 📌 route
The `route` command allows administrators to display and manipulate the IP routing table. It has been replaced by `ip route` in modern distributions.

### 📌 host
The `host` command resolves domain names into IP addresses and vice versa.

### 📌 curl & wget
Both `curl` and `wget` are used to fetch data from web servers. `curl` supports a wide range of protocols, while `wget` is mainly used for downloading files.

### 📌 iwconfig
The `iwconfig` command is used to configure wireless network interfaces.

### 📌 arp
The `arp` command displays and modifies the ARP table, which maps IP addresses to MAC addresses.

### 📌 whois
The `whois` command retrieves domain registration details, including ownership and expiration dates.

### 📌 mtr
The `mtr` command combines the functionality of `ping` and `traceroute` to diagnose network issues in real time.

### 📌 ifplugstatus
The `ifplugstatus` command checks whether a network cable is physically connected to an interface.

---

## 📌 Key Points to Remember
- **Use `ping` and `traceroute`** to diagnose connectivity issues.
- **`netstat` and `ss`** help analyze active network connections.
- **Secure remote access** with `ssh` instead of `telnet`.
- **Analyze network traffic** using `tcpdump` and `wireshark`.
- **Verify DNS records** using `nslookup` and `dig`.
- **Measure network performance** using `iperf`.
- **Manage wireless networks** with `iwconfig`.
- **Check routing configurations** using `route` and `ip route`.
- **Monitor network connectivity** with `mtr`.



