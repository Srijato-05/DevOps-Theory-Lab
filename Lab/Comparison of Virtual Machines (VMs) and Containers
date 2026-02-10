# Lab Report: Comparison of Virtual Machines (VMs) and Containers

**Date:** February 10, 2026

## Objective

The primary goal of this experiment is to evaluate the conceptual and practical differences between Virtual Machines (VMs) and Containers by deploying an Ubuntu-based Nginx web server in both environments. Key objectives include:

* Installing and configuring a Virtual Machine using VirtualBox and Vagrant on Windows.
* Configuring containers using Docker inside the Windows Subsystem for Linux (WSL).
* Deploying an Ubuntu-based Nginx web server in both environments.
* Comparing resource utilization, performance, and operational characteristics such as boot time and RAM usage.

---

## Implementation: Part A – Virtual Machine (Windows)

This phase involves the deployment of a full operating system emulation using a hypervisor.

### Environment Initialization

Install Oracle VirtualBox and Vagrant using default settings. Verify the Vagrant installation via the terminal.

**Command:**

```powershell
vagrant --version
```

### Ubuntu VM Deployment

Create a dedicated project directory and initialize the environment using an Ubuntu box.

**Command:**

```powershell
mkdir vm-lab
cd vm-lab
vagrant init ubuntu/jammy64
vagrant up
```

### Nginx Configuration

Access the virtual machine via SSH to install and start the Nginx service.

**Command:**

```bash
vagrant ssh
sudo apt update
sudo apt install -y nginx
sudo systemctl start nginx
```

### Verification and Cleanup

Confirm the web server is operational and then terminate the instance.

**Command:**

```bash
curl localhost
vagrant halt
vagrant destroy
```

---

## Implementation: Part B – Containers using WSL (Windows)

This phase focuses on virtualization at the operating system level, where the host OS kernel is shared.

### WSL and Ubuntu Setup

Install the WSL 2 feature and the Ubuntu distribution.

**Command:**

```powershell
wsl --install
wsl --install --distribution Ubuntu
```

_Note: A system restart is mandatory after the initial WSL installation to finalize the kernel integration._

### Docker Engine Installation

Within the WSL Ubuntu terminal, install the Docker engine and configure the user group for non-root access.

**Command:**

```bash
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo usermod -aG docker $USER
```

### Container Deployment

Pull the official Ubuntu image and launch an Nginx container, mapping host port 8080 to container port 80.

**Command:**

```bash
docker pull ubuntu
docker run -d -p 8080:80 --name nginx-container nginx
curl localhost:8080
```

---

## Resource Utilization Analysis

System metrics were monitored using commands such as `free -h` for memory and `docker stats` for container-specific performance.

| Parameter        | Virtual Machine | Container |
| ---------------- | --------------- | --------- |
| **Boot Time**    | High            | Very Low  |
| **RAM Usage**    | High            | Low       |
| **CPU Overhead** | Higher          | Minimal   |
| **Isolation**    | Strong          | Moderate  |

---

## Conclusion

The experiment confirms that Containers are significantly more lightweight and resource-efficient compared to virtual machines. Containers are ideal for microservices and rapid deployment, while Virtual Machines remain suitable for workloads requiring full OS isolation.
