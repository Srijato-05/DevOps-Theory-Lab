# Experiment 0: Windows Subsystem for Linux

### Step 1: Install WSL and Ubuntu Distribution

Open **PowerShell as Administrator** and execute the installation command. This process automatically enables the Virtual Machine Platform and installs the latest Ubuntu distribution.

**Command:**
```powershell
wsl --install --distribution Ubuntu
```

![Installation Command](../Asset/0/0-1.png)

**Expected Output:**
```
Installing, this may take a few minutes...
WslRegisterDistribution failed with error: 0x80370102
Please enable the Virtual Machine Platform Windows feature and ensure virtualization platform is enabled in the BIOS.
```
*(If you see this error, enable Hyper-V in Windows Features)*

**Important Note:** A system restart is required after this command completes. Save all work before proceeding.n

**Date:** February 9, 2026  
**Lab Type:** Infrastructure Setup  
**Difficulty Level:** Beginner

---

## Table of Contents

1. [Objective](#objective)
2. [Prerequisites](#prerequisites)
3. [Implementation Steps](#implementation-steps)
4. [Verification](#verification)
5. [Troubleshooting](#troubleshooting)
6. [Conclusion](#conclusion)

---

## Objective

Establish a functional Linux environment on a Windows host using Windows Subsystem for Linux (WSL2). This setup provides the necessary foundation for running DevOps tools, containerization engines (Docker), and Linux-based development environments natively on Windows.

**Expected Outcomes:**
- Successfully install WSL2 with Ubuntu distribution
- Verify WSL2 installation and status
- Configure Ubuntu as the default Linux environment
- Enable seamless Windows-Linux interoperability

---

## Prerequisites

- **OS:** Windows 10 (Build 19041+) or Windows 11
- **Hardware:** Virtualization capability enabled in BIOS
- **Permissions:** Administrator access to PowerShell
- **Disk Space:** Minimum 5GB free storage

---

## Implementation Steps

### Step 1: Install WSL and Ubuntu Distribution

Open **PowerShell as Administrator** and execute the installation command. This process automatically enables the Virtual Machine Platform and installs the latest Ubuntu distribution.

**Command:**
```powershell
wsl --install --distribution Ubuntu
```

**Expected Output:**
```
Installing, this may take a few minutes...
WslRegisterDistribution failed with error: 0x80370102
Please enable the Virtual Machine Platform Windows feature and ensure virtualization platform is enabled in the BIOS.
```
*(If you see this error, enable Hyper-V in Windows Features)*

**Important Note:** A system restart is required after this command completes. Save all work before proceeding.

![WSL Installation](../Asset/Lab 0/0-1.png)

---

### Step 2: Restart the System

After running the installation command, restart your computer to allow Windows to initialize the WSL2 kernel and virtual machine platform.

```powershell
Restart-Computer
```

### Step 3: Verify WSL Installation and Version

Once the system has rebooted, verify that the distribution is properly installed and confirm which version of WSL is active.

**Command:**
```powershell
wsl --list --verbose
```

**Expected Output:**
```
  NAME      STATE           VERSION
* Ubuntu    Running         2
```

This confirms:
- **Distribution Name:** Ubuntu
- **Current State:** Running or Stopped
- **WSL Version:** Version 2 (preferred) or Version 1

![WSL List Verbose](../Asset/Lab 0/0-2.png)

---

### Step 4: Set Ubuntu as Default Distribution

In cases where multiple Linux distributions are installed, designate Ubuntu as the default instance.

**Command:**
```powershell
wsl --set-default Ubuntu
```

![Set Default Distribution](../Asset/Lab 0/0-3.png)

**Verification:**
```powershell
wsl --list --verbose
```
The asterisk (*) should appear next to Ubuntu in the output.

---

### Step 5: Configure WSL 2 as Global Default

Ensure all future distributions use the improved WSL2 architecture, which provides better performance, full Linux kernel compatibility, and Docker support.

**Command:**
```powershell
wsl --set-default-version 2
```

![WSL2 Default Version](../Asset/Lab 0/0-5.png)

**Verification:**
```powershell
wsl --list --verbose
```

---

### Step 6: Convert Existing WSL1 Instances (if applicable)

If an instance is currently running on WSL Version 1, upgrade it to WSL2 by specifying the distribution name.

**Command:**
```powershell
wsl --set-version Ubuntu 2
```

![Convert WSL Version](../Asset/0/Lab 0-6.png)

**Conversion Duration:** This may take 3-5 minutes depending on your system.

**Status Check:**
```powershell
wsl --list --verbose
```

---

## Verification

### Verify WSL2 Installation

Run the following command to confirm successful setup:

```powershell
wsl --list --verbose
```

Expected output should show Ubuntu with VERSION 2.

### Launch Ubuntu Environment

Open a new PowerShell window and start Ubuntu:

```powershell
wsl
```

Or directly from Windows Terminal by selecting "Ubuntu" from the dropdown.

### Check Ubuntu Version

Once in the Ubuntu environment, verify the Linux distribution:

```bash
lsb_release -a
```

Expected output:
```
Distributor ID: Ubuntu
Release: 22.04 (or latest LTS version)
Codename: jammy
```

### Update Package Manager

Update the Ubuntu package index:

```bash
sudo apt update && sudo apt upgrade -y
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **"Virtual Machine Platform not enabled"** | Enable it in Windows Features: `Settings > Apps > Apps & features > Optional features > Virtual Machine Platform` |
| **"Virtualization not enabled in BIOS"** | Restart computer, enter BIOS (Del/F2), enable VT-x (Intel) or AMD-V (AMD) |
| **WSL1 instead of WSL2** | Run `wsl --set-default-version 2` and convert existing instances |
| **Slow WSL2 performance on network drives** | Store projects in WSL's native file system (`/home/username/`) instead of `/mnt/c/` |
| **"Distribution not found"** | Run `wsl --install --distribution Ubuntu` again or download from Microsoft Store |

---

## Performance Comparison

| Feature | WSL1 | WSL2 |
|---------|------|------|
| **File System Performance** | Native Windows | Virtual Machine |
| **Linux Compatibility** | ~80% | 100% |
| **Docker Support** | Limited | Full |
| **Memory Usage** | Low | Medium |
| **Boot Time** | Instant | ~3-5 seconds |

**Recommendation:** WSL2 is strongly preferred for DevOps and containerization work.

---

## Conclusion

You have successfully:
- Installed Windows Subsystem for Linux 2
- Configured Ubuntu as the default distribution
- Verified installation and system compatibility
- Established a Linux development environment on Windows

Your Windows-Linux development environment is now ready for containerization (Docker), Kubernetes, and advanced DevOps tooling in subsequent experiments.

**Next Steps:** Proceed to Experiment 1 to install Docker and containerization tools.

---

## Additional Resources

- [WSL Official Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- [WSL2 Kernel Updates](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
- [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701)
- [Ubuntu on WSL Guide](https://ubuntu.com/wsl)
