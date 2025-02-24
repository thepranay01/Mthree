# Understanding Processes in Linux

## What is a Process?
A **process** is an instance of a program that is being executed. It consists of system resources such as memory, CPU time, and file handles.

### Key Points:
- Every command executed in Linux starts a **new process**.
- Each process has a unique **Process ID (PID)**.
- Used PIDs can be reassigned after being released.
- At any time, no two processes have the same PID.

---

## Running a Process
### 1️⃣ Foreground Process (Default Mode)
- Runs in the foreground, receiving input from the keyboard and displaying output to the screen.
- Blocks the terminal until the process completes.

**Example:**
```bash
$ pwd
/home/user
```

### 2️⃣ Background Process
- Runs in the background, allowing other tasks to execute in parallel.
- Use `&` to start a process in the background.

**Example:**
```bash
$ pwd &
[1]   +   Done                 pwd
```

---

## Viewing Processes
### 🔍 List Running Processes
- Use the `ps` command to see running processes.

```bash
$ ps
PID       TTY      TIME        CMD
19        pts/1    00:00:00    sh
24        pts/1    00:00:00    ps
```

### 🔍 Detailed Process Information
- Use `ps -f` for more details.

```bash
$ ps -f
UID      PID  PPID C STIME    TTY        TIME CMD
52471     19     1 0 07:20    pts/1  00:00:00 sh
52471     25    19 0 08:04    pts/1  00:00:00 ps -f
```

- `UID`: User ID
- `PID`: Process ID
- `PPID`: Parent Process ID
- `C`: CPU usage
- `STIME`: Start time
- `TTY`: Terminal
- `TIME`: CPU time used
- `CMD`: Command that started the process

---

## Controlling Processes
### 🚀 Move a Process to the Background
```bash
$ bg %19
```
### 🎯 Bring a Background Process to the Foreground
```bash
$ fg %19
```

### 🛑 Stopping a Process
- **Foreground Process**: Press `Ctrl + C`
- **Background Process**: Use `kill` with PID

```bash
$ kill 19
Terminated
```
- **Force Kill**: If the process ignores `kill`, use `kill -9`.
```bash
$ kill -9 19
Terminated
```

---

## Monitoring System Processes
### 📊 View Active Processes
```bash
$ top
```

### ⏳ Set Process Priority
- **Start a Process with Priority:**
```bash
$ nice -10 my_program
```
- **Change Priority of Running Process:**
```bash
$ renice -5 1234  # 1234 is PID
```

---

## System Resource Monitoring
### 📁 Check Disk Space
```bash
$ df
```
### 🖥️ Check Memory Usage
```bash
$ free
```

---

## Types of Processes
1. **Parent and Child Processes**
   - Parent processes create child processes.
   - `PPID` (Parent PID) shows the parent of each process.

2. **Zombie and Orphan Processes**
   - **Zombie**: A terminated process that still appears in the process table.
   - **Orphan**: A child process whose parent has exited, adopted by `init`.

3. **Daemon Processes**
   - Background system processes running with root permissions.
   - Identified by `?` in the `TTY` column.

```bash
$ ps -ef
```

---

## 🏆 Best Practices
- Use `ps aux` to get a detailed process list.
- Prefer `kill -15` before using `kill -9` (force kill).
- Use `nohup command &` to run processes that persist after logout.
- Monitor system resources with `top`, `df`, and `free`.

---

## 📊 Summary Table
| Command | Description |
|---------|-------------|
| `ps` | List processes |
| `ps -f` | Show detailed process info |
| `kill PID` | Terminate a process |
| `kill -9 PID` | Force terminate a process |
| `bg %job_id` | Resume a job in the background |
| `fg %job_id` | Bring a background job to the foreground |
| `top` | Show running processes |
| `df` | Show disk space usage |
| `free` | Show memory usage |

---
