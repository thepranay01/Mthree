# 🧪 Linux Service Management with systemd

## 🔹 Introduction
Managing services is an essential skill for Linux administrators. **systemd** is the primary system and service manager in many modern Linux distributions. It is responsible for initializing the system, managing services, and maintaining the overall system state.

In this activity, you will learn how to:
- Use `systemctl` to manage services.
- Create a custom service.
- Use `journalctl` to view and filter service logs.
- Analyze open files related to a running service.

---

## ⚙️ systemctl - Managing System Services

### 📖 Checking Systemd Status
To confirm if `systemd` is running, use:
```bash
systemctl is-system-running
```

### 📌 Listing Services
To see all active services:
```bash
systemctl list-units
```
To filter specific services:
```bash
systemctl list-units | grep httpd
```
If `httpd` (Apache) is not installed, install it:
```bash
sudo dnf install httpd
```

### 🔄 Managing Service Startup Behavior
Check if a service starts on boot:
```bash
systemctl is-enabled httpd
```
Enable a service to start on boot:
```bash
sudo systemctl enable httpd
```

### ▶️ Controlling Services
| Command | Description |
|---------|------------|
| `sudo systemctl start httpd` | Start the service |
| `sudo systemctl restart httpd` | Restart the service |
| `sudo systemctl stop httpd` | Stop the service |
| `systemctl status httpd` | Check service status |

---

## 🛠 Creating a Custom Service

### 📌 Creating a Script
First, create a simple script that writes logs:
```bash
sudo vi /usr/local/bin/hello-world.sh
```
Paste the following content:
```bash
#!/bin/bash
LOGFILE="/tmp/hello-world.log"
exec 3>>$LOGFILE
while true
do
  echo "$(date): Hello World" >&3
  sleep 5
done
```
Make it executable:
```bash
sudo chmod +x /usr/local/bin/hello-world.sh
```

### 🔹 Creating a Systemd Service Unit
Create a service definition:
```bash
sudo vi /etc/systemd/system/hello-world.service
```
Add the following content:
```ini
[Unit]
Description=Hello World Service

[Service]
ExecStart=/usr/local/bin/hello-world.sh
Type=simple
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```
Reload `systemd`, start the service, and check its status:
```bash
sudo systemctl daemon-reload
sudo systemctl start hello-world
sudo systemctl status hello-world
```

---

## 📜 Viewing Logs with journalctl

To see logs for the `hello-world` service:
```bash
sudo journalctl -u hello-world
```
View logs from the last 10 minutes:
```bash
sudo journalctl -u hello-world --since "10 minutes ago"
```
Follow logs in real-time:
```bash
sudo journalctl -u hello-world -f
```

---

## 🔎 Finding Open Files & Process Details

### 📌 Finding the Process ID (PID)
```bash
sudo systemctl show -p MainPID hello-world
pgrep hello-world
```

### 🔍 Listing Open Files
```bash
sudo lsof -p $(pgrep hello-world)
sudo ls -ls /proc/$(pgrep hello-world)/fd
```
Follow the log file:
```bash
tail -f /tmp/hello-world.log
```

---

## 🔥 Enhancing Security & Restart Limits
Modify the service to run as **nobody** user:
```ini
[Service]
ExecStart=/usr/local/bin/hello-world.sh
Type=simple
Restart=always
RestartSec=5
User=nobody
Group=nobody
```

Limit restarts within a time frame:
```ini
[Service]
ExecStart=/usr/local/bin/hello-world.sh
Type=simple
Restart=always
RestartSec=5
User=nobody
Group=nobody
StartLimitBurst=3
StartLimitIntervalSec=30
```
Reload the service to apply changes:
```bash
sudo systemctl daemon-reload
sudo systemctl restart hello-world
```

---

## 🧹 Cleanup
Stop and disable the service:
```bash
sudo systemctl stop hello-world
sudo systemctl disable hello-world
```

---

## ✅ Summary Table
| Command | Description |
|---------|------------|
| `systemctl is-system-running` | Check if systemd is running |
| `systemctl list-units` | List running services |
| `sudo systemctl start <service>` | Start a service |
| `sudo systemctl stop <service>` | Stop a service |
| `sudo systemctl restart <service>` | Restart a service |
| `systemctl status <service>` | View service status |
| `sudo systemctl enable <service>` | Enable service at boot |
| `sudo systemctl disable <service>` | Disable service at boot |
| `sudo journalctl -u <service>` | View service logs |
| `sudo journalctl -u <service> --since "10 minutes ago"` | View last 10 minutes of logs |
| `sudo journalctl -u <service> -f` | Follow logs in real-time |
| `sudo systemctl show -p MainPID <service>` | Get process ID |
| `sudo lsof -p <PID>` | List open files by process |

---

## 🎯 Conclusion
We have successfully learned how to manage services using **systemctl**, create a **custom service**, view logs with **journalctl**, and inspect open files related to a process.