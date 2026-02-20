# Containerization & DevOps Portfolio

**UPES | School of Computer Science | Academic Year 2025-26**

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![GitHub Pages](https://img.shields.io/badge/github%20pages-121013?style=for-the-badge&logo=github&logoColor=white) ![Bash](https://img.shields.io/badge/bash-%234EAA25.svg?style=for-the-badge&logo=gnu-bash&logoColor=white) ![WSL2](https://img.shields.io/badge/WSL2-0078D4?style=for-the-badge&logo=windows&logoColor=white) ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

---

## 👤 Student Information

| Detail | Information |
| :--- | :--- |
| **Name** | Srijato Das |
| **SAP ID** | 500119148 |
| **Enrollment No.** | R2142230488 |
| **Batch** | B1 CCVT |
| **Course** | Containerization and DevOps |
| **Institution** | UPES, School of Computer Science |

---

## 📚 Course Overview

This portfolio documents comprehensive hands-on experience with containerization technologies and DevOps practices. The curriculum covers Docker fundamentals, container orchestration, image optimization, and practical DevOps workflows using modern cloud-native tools.

**Key Learning Outcomes:**
- Master containerization concepts and Docker ecosystem
- Build and optimize production-ready container images
- Implement container networking and data persistence
- Deploy and manage multi-container applications
- Compare virtualization vs. containerization approaches

---

## 🔬 Lab: Laboratory Experiments

*Official documentation of hands-on experiments performed in the laboratory.*

### Experiment 0: Windows Subsystem for Linux (WSL) Configuration
**Date:** February 9, 2026 | **Status:** ✅ Complete

Establish a functional Linux development environment on Windows using WSL2 and install Git for version control.

**Topics Covered:**
- WSL2 installation and configuration
- Ubuntu distribution setup
- Git installation and configuration
- Windows-Linux interoperability

**Documentation:** [📖 Experiment 0](./Lab/Experiment%200_%20Windows%20Subsystem%20for%20Linux%20(WSL)%20Configuration.md)

---

### Experiment 1: Comparison of Virtual Machines (VMs) and Containers
**Date:** February 10, 2026 | **Status:** ✅ Complete

Practical comparison of VirtualBox/Vagrant VMs and Docker containers through hands-on deployment and resource monitoring.

**Topics Covered:**
- Virtual Machine deployment with Vagrant
- Container deployment with Docker
- Performance metrics comparison (boot time, memory, CPU)
- Use case analysis and recommendations

**Key Findings:**
- Containers start in milliseconds vs. minutes for VMs
- Container memory overhead: 25-50MB vs. 800MB-1.2GB for VMs
- Containers ideal for microservices; VMs for complete OS isolation

**Documentation:** [📖 Experiment 1](./Lab/Experiment%201_%20Comparison%20of%20Virtual%20Machines%20(VMs)%20and%20Containers.md)

---

### Experiment 2: Docker Installation, Configuration, and Running Images
**Date:** February 11, 2026 | **Status:** ✅ Complete

Master Docker fundamentals through image management and container lifecycle operations.

**Topics Covered:**
- Docker installation and verification
- Pulling images from Docker Hub
- Running containers with port mapping
- Container lifecycle management (stop, remove)
- Image removal and cleanup

**Practical Tasks:**
- Pull and run official Nginx image
- Map container ports to host system
- Verify running containers with `docker ps`
- Manage container lifecycle operations

**Documentation:** [📖 Experiment 2](./Lab/Experiment%202_Docker%20Basic%20Operations.md)

---

### Experiment 3: Deploying NGINX Using Different Base Images and Comparing Image Layers
**Date:** February 20, 2026 | **Status:** ✅ Complete

Advanced container image analysis comparing different base images (Official, Ubuntu, Alpine) and their performance characteristics.

**Topics Covered:**
- Official NGINX image deployment
- Custom Ubuntu-based NGINX image creation
- Alpine Linux-based optimization
- Docker image layer analysis
- Performance and security trade-offs

**Size Comparison Results:**
| Base Image | Size | Startup Time | Memory |
|-----------|------|--------------|--------|
| Official (Debian) | 187 MB | ~1 sec | 12 MB |
| Ubuntu | 320 MB | ~2 sec | 18 MB |
| Alpine | 28 MB | ~0.5 sec | 4 MB |

**Documentation:** [📖 Experiment 3](./Lab/Experiment%203_%20Deploying%20NGINX%20Using%20Different%20Base%20Images%20and%20Comparing%20Image%20Layers.md)

---

### Experiment 4: Docker Essentials
**Date:** TBD | **Status:** 🔄 In Progress

Deep dive into Docker best practices, optimization techniques, and production-ready configurations.

**Topics to Cover:**
- Multi-stage Dockerfile optimization
- Docker Compose for multi-container orchestration
- Container security and image scanning
- Resource limits and performance tuning
- CI/CD integration with Docker

**Documentation:** [📖 Experiment 4](./Lab/Experiment%204_Docker%20Essentials.md) *(Coming Soon)*

---

## 📖 Theory: Classroom Practicals

*Supplementary theoretical concepts and implementation guides covered during classroom sessions.*

| No. | Topic | Description |
| :-- | :---- | :---------- |
| P1 | VM vs. Containers | Historical timeline and architectural comparison of virtualization technologies |
| P2 | Docker Basics | Essential CLI commands and container lifecycle management |
| P3 | Container Persistence | Data volume management and state preservation strategies |
| P4 | Dockerfile Tutorial | Building custom images with best practices |
| P5 | Docker API | REST API exploration and engine interaction |
| P6 | Exposing Docker API | Secure API exposure patterns and security considerations |
| P7 | Multistage Builds | Image optimization for reduced size and improved security |
| P8 | Re-attaching Containers | Technical procedures for reconnecting to stopped instances |

---

## 🛠️ Technology Stack

| Category | Tools & Technologies |
| :--- | :--- |
| **Containerization** | Docker, Docker Compose |
| **Operating Systems** | Windows 11, WSL2, Ubuntu 22.04, Alpine Linux |
| **Cloud-Native** | Kubernetes (planned), Container Registry (Docker Hub) |
| **Infrastructure** | VirtualBox, Vagrant |
| **Version Control** | Git, GitHub |
| **Shell Scripting** | Bash, PowerShell |
| **Web Services** | NGINX, Apache |
| **Development** | Dockerfile, YAML, Linux Commands |

---

## 📁 Repository Structure

```
DevOps-Theory-Lab/
├── Lab/
│   ├── Experiment 0_ Windows Subsystem for Linux (WSL) Configuration.md
│   ├── Experiment 1_ Comparison of Virtual Machines (VMs) and Containers.md
│   ├── Experiment 2_Docker Basic Operations.md
│   ├── Experiment 3_ Deploying NGINX Using Different Base Images...md
│   └── Experiment 4_Docker Essentials.md
├── Asset/
│   ├── Lab_0/          (Screenshots: 0-1.png through 0-5.png)
│   ├── Lab_1/          (Screenshots: 1-1.png through 1-9.png)
│   ├── Lab_2/          (Screenshots: 2-1.png through 2-7.png)
│   └── Lab_3/          (Screenshots: 3-1.png through 3-8.png)
├── Theory/             (Classroom practicals and supplementary materials)
├── README.md           (This file)
└── .gitignore
```

---

## 🎯 Learning Objectives

Upon completion of this course, students will be able to:

✅ Understand virtualization concepts and containerization advantages  
✅ Deploy and manage Docker containers in production environments  
✅ Optimize Docker images for size, performance, and security  
✅ Implement container networking and data persistence strategies  
✅ Deploy multi-container applications using Docker Compose  
✅ Compare different base images and choose appropriate solutions  
✅ Apply DevOps best practices in containerized environments  
✅ Troubleshoot container issues and optimize performance  

---

## 📊 Course Progress

| Experiment | Status | Completion |
| :--- | :--- | :--- |
| Experiment 0 - WSL Setup | ✅ Complete | 100% |
| Experiment 1 - VMs vs Containers | ✅ Complete | 100% |
| Experiment 2 - Docker Basics | ✅ Complete | 100% |
| Experiment 3 - Image Comparison | ✅ Complete | 100% |
| Experiment 4 - Docker Essentials | 🔄 In Progress | 0% |

**Overall Progress:** 4 of 5 experiments complete (80%)

---

## 🚀 Quick Start

### Prerequisites
- Windows 10/11 with WSL2 enabled
- Docker installed in WSL
- Git configured
- GitHub account

### Running Experiments Locally

```bash
# Clone the repository
git clone https://github.com/Srijato-05/DevOps-Theory-Lab.git
cd DevOps-Theory-Lab

# Navigate to Lab directory
cd Lab

# Read Experiment documentation
cat "Experiment 0_ Windows Subsystem for Linux (WSL) Configuration.md"

# Start the experiment
cd ~/docker-projects
docker run -d -p 8080:80 nginx:latest
```

---

## 📝 Documentation Standards

All lab reports follow a standardized format:

1. **Experiment Title** - Clear, descriptive name
2. **Metadata** - Date, difficulty level, technology stack
3. **Objectives** - Clear learning outcomes
4. **Prerequisites** - Required knowledge and tools
5. **Procedure** - Step-by-step instructions with code blocks
6. **Expected Output** - Verification examples
7. **Screenshots** - Visual documentation of results
8. **Analysis** - Performance metrics and comparisons
9. **Conclusion** - Key takeaways and real-world applications
10. **Resources** - Links to official documentation

---

## 🔗 Useful Resources

### Official Documentation
- [Docker Official Docs](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [WSL2 Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- [Linux Documentation](https://linux.org/)

### Learning Platforms
- [Docker Learning Center](https://www.docker.com/resources/what-is-docker/)
- [Kubernetes.io](https://kubernetes.io/)
- [CNCF - Cloud Native Computing Foundation](https://www.cncf.io/)

### Related Technologies
- [Vagrant Documentation](https://www.vagrantup.com/docs)
- [VirtualBox Manual](https://www.virtualbox.org/manual/)
- [Git Documentation](https://git-scm.com/doc)

---

## 📧 Contact & Support

**Student:** Srijato Das  
**Email:** srijato.das@upes.ac.in  
**GitHub:** [@Srijato-05](https://github.com/Srijato-05)  
**University:** UPES, School of Computer Science

---

## 📋 Academic Integrity

This portfolio documents original work completed as part of the Containerization and DevOps course curriculum at UPES. All experiments were conducted following institutional guidelines and academic integrity standards.

---

## 📄 License

This documentation and code samples are provided for educational purposes as part of the UPES Containerization and DevOps course (Academic Year 2025-26). All rights reserved.

---

<p align="center">
  <b>System Documentation & Portfolio</b><br>
  <i>Maintained by Srijato Das | UPES School of Computer Science</i><br>
  <i>Last Updated: February 2026 | Hosted on GitHub Pages</i><br>
  <i>Content updated in real-time upon commit</i>
</p>

<p align="center">
  <a href="#containerization--devops-portfolio">↑ Back to Top</a>
</p>
