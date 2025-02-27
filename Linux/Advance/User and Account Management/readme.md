# 🤧 Linux User and Group Management Commands

Managing users and groups is crucial for Linux system administration. Here’s a list of essential commands along with their syntax and usage.

---
## 👤 User Management Commands

### 🆕 1. `useradd` (Add New User)
📌 **Definition**: Creates a new user account.

🔹 **Syntax**:
```bash
useradd [options] username
```
🔹 **Example**:
```bash
useradd pranay
```
🫠 Creates a new user named `pranay`.

### 🔑 2. `passwd` (Set/Change User Password)
📌 **Definition**: Sets or changes the password for a user.

🔹 **Syntax**:
```bash
passwd [username]
```
🔹 **Example**:
```bash
passwd pranay
```
🫠 Prompts to set a new password for the user `pranay`.

### 🛠️ 3. `usermod` (Modify User Account)
📌 **Definition**: Modifies an existing user account.

🔹 **Syntax**:
```bash
usermod [options] username
```
🔹 **Example**:
```bash
usermod -aG sudo pranay
```
🫠 Adds `pranay` to the `sudo` group.

### ❌ 4. `userdel` (Delete User Account)
📌 **Definition**: Deletes a user account.

🔹 **Syntax**:
```bash
userdel [options] username
```
🔹 **Example**:
```bash
userdel -r pranay
```
🫠 Deletes the user `pranay` and their home directory.

### ⏬ 5. `su` (Switch User)
📌 **Definition**: Allows switching to another user.

🔹 **Syntax**:
```bash
su [username]
```
🔹 **Example**:
```bash
su pranay
```
🫠 Switches to the user `pranay`.

### ⚡ 6. `sudo` (Run Commands as Another User, Typically Root)
📌 **Definition**: Executes commands with elevated privileges.

🔹 **Syntax**:
```bash
sudo [command]
```
🔹 **Example**:
```bash
sudo useradd testuser
```
🫠 Creates a new user with admin privileges.

---
## 👥 Group Management Commands

### 🆕 7. `groupadd` (Create New Group)
📌 **Definition**: Creates a new user group.

🔹 **Syntax**:
```bash
groupadd groupname
```
🔹 **Example**:
```bash
groupadd developers
```
🫠 Creates a new group named `developers`.

### ❌ 8. `groupdel` (Delete Group)
📌 **Definition**: Deletes a user group.

🔹 **Syntax**:
```bash
groupdel groupname
```
🔹 **Example**:
```bash
groupdel developers
```
🫠 Deletes the `developers` group.

### 🔄 9. `gpasswd` (Manage Group Membership)
📌 **Definition**: Adds or removes users from a group.

🔹 **Syntax**:
```bash
gpasswd -a username groupname
```
🔹 **Example**:
```bash
gpasswd -a pranay developers
```
🫠 Adds `pranay` to the `developers` group.

### ⏬ 10. `newgrp` (Change Active Group)
📌 **Definition**: Changes the current group of a logged-in user.

🔹 **Syntax**:
```bash
newgrp [groupname]
```
🔹 **Example**:
```bash
newgrp developers
```
🫠 Switches the current group to `developers`.

### 🔒 11. `finger` (Display User Information)
📌 **Definition**: Shows detailed user information.

🔹 **Syntax**:
```bash
finger [username]
```
🔹 **Example**:
```bash
finger pranay
```
🫠 Displays login details, home directory, and shell of `pranay`.

### 👨‍💻 12. `last` (Show Login History)
📌 **Definition**: Displays the login history of users.

🔹 **Syntax**:
```bash
last
```
🫠 Shows a list of users who logged in recently.

### ⛔️ 13. `faillog` (Show Failed Login Attempts)
📌 **Definition**: Displays failed login attempts of users.

🔹 **Syntax**:
```bash
faillog -u [username]
```
🔹 **Example**:
```bash
faillog -u pranay
```
🫠 Shows failed login attempts for `pranay`.

---

## 🏢 Best Practices
✔️ Use `sudo` before commands when modifying users/groups.
✔️ Assign strong passwords using `passwd`.
✔️ Remove unused users with `userdel -r` to free resources.
✔️ Regularly check system users with `who`, `id`, and `groups`.
✔️ Use `chmod`, `chown`, and `chgrp` carefully to avoid permission issues.

---
## 📊 Summary Table

| Command  | Purpose |
|----------|---------|
| `su`  | Switch user |
| `sudo`  | Run commands as root |
| `newgrp`  | Change active group |
| `finger`  | Show user info |
| `last`  | Show login history |
| `faillog`  | Show failed login attempts |

---
✅ **For detailed information, use:**
```bash
man [command]
```
➡️ Example:
```bash
man useradd
```
🎯 Learn more about each command in-depth!

---
