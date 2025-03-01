# 📦 Package Management with DNF

## 🔹 Introduction

Package management in Linux is essential for installing, updating, and removing software. 

In **Red Hat Enterprise Linux (RHEL)** and its derivatives, including **Amazon Linux 2023**, the **dnf** package manager is used. **Debian-based** distributions use **apt**, while **Alpine Linux** uses **apk**.

Not all software is installed via a package manager; some software is manually installed using a **gzip tarball**.

---

## ⚙️ DNF - The Red Hat Package Manager

### 📖 Read the Manual
To understand **dnf**, read its manual page:
```bash
man dnf
```
Or use the `--help` flag and filter results with **grep**:
```bash
dnf --help | grep list
```

### 📌 Checking Available Repositories & Installed Packages
```bash
dnf repolist    # Show repositories in use
dnf list installed  # List all installed packages
dnf list installed | grep curl  # Check if curl is installed
```

### 🔍 Searching & Querying Packages
```bash
dnf search mariadb  # Search for MariaDB package
dnf repoquery mariadb105 --deplist  # Query dependencies of mariadb105
```

### 🏗 Installing & Removing Packages
```bash
sudo dnf install mariadb105  # Install MariaDB (use -y to skip prompt)
dnf list installed | grep mariadb  # Verify installation
sudo dnf remove mariadb105  # Uninstall MariaDB
dnf list installed | grep mariadb  # Verify removal
```

---

## 🔄 Updating & Upgrading Packages

### ⬆️ Updating Installed Packages
Updating ensures you have the latest versions with security patches.
```bash
dnf check-update  # Check for available updates
sudo dnf update  # Install updates for all installed packages
```
**🔹 Best Practice:** Update before installing new software to ensure compatibility.

### 🚀 Upgrading to a New Release
Upgrades involve major changes, such as moving to a new OS version.
```bash
dnf upgrade --releasever=<version>  # Upgrade to a new release version
sudo dnf system-upgrade reboot  # Reboot system after upgrade
```

---

## 🔗 Adding a Repository
Sometimes, the required packages exist in external repositories. 
To install **Terraform**, add the HashiCorp repo:
```bash
sudo dnf config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
```

### 📌 Installing a Specific Package Version
To list all available versions:
```bash
dnf list --showduplicates terraform
```
To install a specific version:
```bash
sudo dnf install terraform-1.6.0-1
```
To **downgrade**, allow replacing dependencies:
```bash
sudo dnf install terraform-1.5.0-1 --allowerasing
```
To upgrade to the latest version:
```bash
sudo dnf update terraform
```

---

## ✅ Best Practices
- Always update package lists before installation.
- Use `--dry-run` to simulate installations.
- Avoid using `--force` unless necessary.
- Remove unused dependencies using `dnf autoremove`.

---

## 📊 Summary Table
| Command | Description |
|---------|------------|
| `dnf repolist` | Show available repositories |
| `dnf list installed` | List installed packages |
| `dnf search <package>` | Search for a package |
| `dnf install <package>` | Install a package |
| `dnf remove <package>` | Remove a package |
| `dnf check-update` | Check for available updates |
| `dnf update` | Update installed packages |
| `dnf upgrade --releasever=<version>` | Upgrade to a new OS version |

---

## 🎯 Conclusion
Mastering **dnf** on RHEL-based systems like **Amazon Linux 2023** enables efficient package management. By following best practices, you can keep your system secure and up-to-date.

💡 **Practice these commands to enhance your Linux administration skills!** 🚀
