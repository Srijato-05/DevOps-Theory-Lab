**Objective**

The goal of this lab is to establish a functional Linux environment on a
Windows host using the Windows Subsystem for Linux (WSL). This setup
provides the necessary kernel interface required for running DevOps
tools and containerization engines.

**Implementation**

**Installation of WSL and Ubuntu**

To begin the setup, open PowerShell as an Administrator and execute the
installation command. This process enables the Virtual Machine Platform
and installs the Ubuntu distribution.

**Command:**

PowerShell

wsl \--install \--distribution Ubuntu

*Note: A system restart is required after this command completes to
finalize the installation.*

**Verifying the Installation**

Once the system has rebooted, verify that the distribution is installed
and identify which version of WSL is currently active.

**Command:**

PowerShell

wsl \--list \--verbose

This output confirms the distribution name, the current state
(Running/Stopped), and the WSL version (Version 1 or 2).

**Setting the Default Distribution**

In cases where multiple Linux environments are installed, Ubuntu should
be set as the default instance for the terminal.

**Command:**

PowerShell

wsl \--set-default Ubuntu

**Configuring WSL 2 as the Global Default**

To ensure that all future distributions and current instances utilize
the improved performance of the WSL 2 architecture, the default version
must be set globally.

**Command:**

PowerShell

wsl \--set-default-version 2

**Converting Existing Instances**

If an instance is currently running on Version 1, it can be manually
upgraded to Version 2 by specifying the distribution name and the
desired version.

**Command:**

PowerShell

wsl \--set-version Ubuntu 2
