# Package Management in Linux

## Table of Contents
1. [Overview](#overview)
2. [Package Managers](#package-managers)
3. [Package Installation and Removal](#package-installation-and-removal)
4. [Repository Management](#repository-management) 
5. [LAMP Server Setup](#lamp-server-setup)
6. [Troubleshooting](#troubleshooting)

## Overview
Package management is a fundamental concept in Linux systems that handles the installation, removal, configuration and updating of software. It provides a streamlined way to manage software packages and their dependencies.

## Package Managers

### Common Package Managers
1. **APT (Advanced Package Tool)**
   - Used in Debian-based distributions (Ubuntu, Linux Mint)
   - Package format: .deb
   - Main commands:
   ```bash
   sudo apt update              # Update package list
   sudo apt upgrade            # Upgrade installed packages
   sudo apt install package    # Install a package
   sudo apt remove package     # Remove a package
   ```

2. **YUM (Yellowdog Updater, Modified)**
   - Used in Red Hat-based distributions (CentOS, RHEL)
   - Package format: .rpm
   - Main commands:
   ```bash
   sudo yum update              # Update package list
   sudo yum upgrade            # Upgrade installed packages
   sudo yum install package    # Install a package
   sudo yum remove package     # Remove a package
   ```

3. **DNF (Dandified YUM)**
   - The next-generation version of YUM, used in Fedora
   - Package format: .rpm
   - Main commands:
   ```bash
   sudo dnf update              # Update package list
   sudo dnf upgrade            # Upgrade installed packages
   sudo dnf install package    # Install a package
   sudo dnf remove package     # Remove a package
   ```

## Package Installation and Removal

### Installing Packages
To install a package using APT:
```bash
sudo apt update
sudo apt install <package_name>
```

### Basic Package Operations
1. **Searching for Packages**
   ```bash
   # APT
   apt search package_name

   # YUM
   yum search package_name

   # DNF
   dnf search package_name
   ```

2. **Installing Packages**
   ```bash
   # APT
   sudo apt install package_name

   # YUM
   sudo yum install package_name

   # DNF
   sudo dnf install package_name
   ```

3. **Removing Packages**
   ```bash
   # APT
   sudo apt remove package_name
   sudo apt purge package_name  # Remove package and configuration

   # YUM
   sudo yum remove package_name

   # DNF
   sudo dnf remove package_name
   ```

## Repository Management

### Adding Repositories
```bash
# APT
sudo add-apt-repository ppa:repository_name

# YUM
sudo yum-config-manager --add-repo repository_url

# DNF
sudo dnf config-manager --add-repo repository_url
```

### Updating Repository Information
```bash
# APT
sudo apt update

# YUM
sudo yum check-update

# DNF
sudo dnf check-update
```

## LAMP Server Setup

### Installing LAMP Stack Components
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install apache2
sudo apt install mysql-server
sudo apt install php libapache2-mod-php php-mysql

# RHEL/CentOS
sudo yum install httpd
sudo yum install mysql-server
sudo yum install php php-mysql
```

### Starting Services
```bash
# Ubuntu/Debian
sudo systemctl start apache2
sudo systemctl start mysql

# RHEL/CentOS
sudo systemctl start httpd
sudo systemctl start mysqld
```

## Troubleshooting

### Common Issues and Solutions

1. **Package Dependencies**
   ```bash
   # APT
   sudo apt --fix-broken install

   # YUM
   sudo yum clean all
   sudo yum update

   # DNF
   sudo dnf clean all
   sudo dnf update
   ```

2. **Repository Issues**
   ```bash
   # APT
   sudo apt clean
   sudo apt update

   # YUM
   sudo yum clean metadata
   sudo yum clean all

   # DNF
   sudo dnf clean metadata
   sudo dnf clean all
   ```

### Checking Service Status
```bash
sudo systemctl status service_name
sudo journalctl -u service_name
```

### Network Troubleshooting
```bash
ping -c 4 google.com        # Test connectivity
nslookup domain_name       # DNS lookup
traceroute domain_name    # Trace network path
```