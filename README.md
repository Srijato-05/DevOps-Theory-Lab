# Containerization & DevOps Portfolio

UPES | School of Computer Science | Academic Year 2025-26

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![WSL2](https://img.shields.io/badge/WSL2-0078D4?style=for-the-badge&logo=windows&logoColor=white) ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![Bash](https://img.shields.io/badge/bash-%234EAA25.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)

---

## Index

Quick links:

- [Student Information](#student-information)
- [About This Portfolio](#about-this-portfolio)
- Laboratory Experiments
  - [Experiment 0 — WSL Configuration](#experiment-0-windows-subsystem-for-linux-configuration)
  - [Experiment 1 — VMs vs Containers](#experiment-1-comparison-of-virtual-machines-vms-and-containers)
  - [Experiment 2 — Docker Basics](#experiment-2-docker-installation-configuration-and-running-images)
  - [Experiment 3 — Deploying NGINX](#experiment-3-deploying-nginx-using-different-base-images)
  - [Experiment 4 — Docker Essentials](#experiment-4-docker-essentials)
- [Technology Stack & Tools](#technology-stack--tools)
- [Classroom Theory Integration](#classroom-theory-integration)
- [Documentation Standards](#documentation-standards)
- [Repository Structure](#repository-structure)
- [Contact & Support](#contact--support)

---

## Student Information

| Detail | Information |
| :--- | :--- |
| **Name** | Srijato Das |
| **SAP ID** | 500119148 |
| **Enrollment No.** | R2142230488 |
| **Batch** | B1 CCVT |
| **Course** | Containerization and DevOps |
| **Institution** | UPES, School of Computer Science |

---

## About This Portfolio

This portfolio documents comprehensive hands-on experience with containerization technologies and DevOps practices. Through carefully designed laboratory experiments, students progress from foundational Linux concepts to advanced Docker optimization techniques.

The curriculum emphasizes practical implementation over theory, with each experiment building upon previous knowledge to create a cohesive learning experience. All work maintains professional documentation standards with detailed analysis, visual evidence, and real-world applications.

**What Makes This Portfolio Unique:**
- Hands-on experimentation with real DevOps tools
- Performance-based analysis and comparisons
- Professional documentation with visual evidence
- Progressive complexity from setup to optimization
- Focus on WSL2 development environments

---

## Laboratory Experiments

### Experiment 0: Windows Subsystem for Linux Configuration

January 24, 2026 

Establish a Linux development environment within Windows using WSL2. This foundational experiment prepares the system for all subsequent containerization work and introduces essential command-line tools.

**Learning Focus:**
- WSL2 installation and resource configuration
- Ubuntu distribution management
- Git version control setup
- Windows-Linux file system interaction
- Development workflow optimization

**Key Outcomes:**
WSL2 properly configured with adequate resources, Ubuntu fully functional, and Git ready for repository management. Foundation established for all future experiments.

[View Experiment 0](./Lab/Experiment_0-Windows_Subsystem_for_Linux(WSL)_Configuration)

---

### Experiment 1: Comparison of Virtual Machines and Containers

January 24, 2026 

Compare traditional virtualization (VirtualBox/Vagrant) with containerization (Docker) through hands-on deployment and performance measurement. This experiment demonstrates why containers have become the industry standard for microservices.

**Core Comparison Metrics:**

| Metric | Virtual Machines | Containers |
|--------|-----------------|-----------|
| Boot Time | 30-60 seconds | <1 second |
| Memory (Idle) | 512MB - 1GB | 5-15MB |
| Memory (Running) | 800MB - 1.2GB | 25-50MB |
| Disk Space | 2-3GB per VM | 100-300MB per image |
| Deployment Speed | Minutes | Seconds |

**Key Findings:**
Containers demonstrate 50-100x memory efficiency advantage compared to full virtual machines. This dramatic difference explains container adoption in cloud-native architectures, microservices, and CI/CD pipelines.

**Technical Understanding:**
- Hypervisor-based vs. container-based virtualization
- Resource isolation at different layers
- Trade-offs between isolation levels and efficiency
- Real-world use case suitability

[View Experiment 1](./Lab/Experiment_1-Comparison_of_Virtual_Machines(VMs)_and_Containers)

---

### Experiment 2: Docker Installation, Configuration, and Running Images

January 31, 2026 

Master fundamental Docker operations through practical image management and container lifecycle procedures. This experiment establishes core Docker competency required for advanced techniques.

**Practical Skills Developed:**

- Image pulling from Docker Hub registries
- Container deployment with port mapping
- Container status verification and networking
- Container lifecycle management (create, start, stop, remove)
- Cleanup and resource management
- Basic troubleshooting

**Experiment Structure:**
The hands-on approach focuses on understanding Docker CLI commands and their practical application. Students execute real-world scenarios and verify expected outputs, building muscle memory for container operations.

**Progression Path:**
This experiment provides essential foundation for Experiment 3's image optimization work and prepares students for multi-container orchestration in advanced experiments.

[View Experiment 2](./Lab/Experiment_2-Docker_Basic_Operations)

---

### Experiment 3: Deploying NGINX Using Different Base Images

February 7, 2026

Analyze Docker image optimization through comparison of different base operating systems. This advanced experiment examines the trade-offs between functionality, size, and performance.

**Image Size Comparison:**

| Base Image | Size | Startup | Memory | Best For |
|-----------|------|---------|--------|----------|
| Official (Debian) | 187 MB | ~1s | 12 MB | Production |
| Ubuntu | 320 MB | ~2s | 18 MB | Development |
| Alpine | 28 MB | ~0.5s | 4 MB | Edge/Lightweight |

**Critical Insights:**

Alpine Linux achieves 85-90% size reduction compared to Ubuntu while maintaining full NGINX functionality. This dramatic difference directly impacts:
- Deployment speed (faster pulls and transfers)
- Container registry storage costs
- Resource-constrained environments
- Security surface area

**Technical Depth:**
Students learn to create Dockerfiles from scratch, analyze multi-layer image structure, understand package manager differences (apt vs apk), and evaluate security implications of base image selection.

**Real-World Application:**
Image optimization is critical in production environments where thousands of container instances deploy across distributed systems. Size reduction translates directly to infrastructure cost savings and improved deployment velocity.

[View Experiment 3](./Lab/Experiment_3-Deploying_NGINX_Using_Different_Base_Images_and_Comparing_Image_Layers)

---

### Experiment 4: Docker Essentials

February 14, 2026 

Advanced Docker concepts including multi-stage builds, Docker Compose orchestration, security scanning, and production-ready configurations.

**Topics to Explore:**
- Multi-stage builds for image optimization
- Docker Compose for application stacks
- Container networking architectures
- Volume and data persistence patterns
- Security best practices and scanning
- Performance optimization techniques
- Logging and monitoring strategies

[View Experiment 4](./Lab/Experiment_4-Docker_Essentials)

---

## Technology Stack & Tools

| Category | Technologies | Purpose |
| :--- | :--- | :--- |
| **Containerization** | Docker, Docker Compose | Application packaging and orchestration |
| **Operating Systems** | Windows 11, WSL2, Ubuntu 22.04, Alpine | Development and container base images |
| **Cloud Infrastructure** | Docker Hub, AWS (planned) | Image registry and cloud deployment |
| **Virtualization** | VirtualBox, Vagrant | VM comparison and testing |
| **Version Control** | Git, GitHub | Code and documentation management |
| **Scripting & CLI** | Bash, PowerShell | Automation and command execution |
| **Web Services** | NGINX, Apache | Web server containerization examples |
| **Configuration** | Dockerfile, YAML | Infrastructure as code |

---

## Classroom Theory Integration

Theory sessions complement practical experiments by providing conceptual foundation:

**Session Topics:**
- Virtualization history and evolution
- Docker architecture and component interaction
- Container runtime and orchestration concepts
- Networking models and communication patterns
- Storage and data persistence strategies
- Security in containerized environments
- DevOps workflows and CI/CD integration
- Production deployment patterns

Theory provides context that makes practical experiments more meaningful and helps students understand "why" behind "what" they're doing in labs.

**Note:** Complete theory session documentation will be added as the course progresses.

---

## Documentation Standards

All experimental reports maintain consistent quality:

**Structure:**
- Clear experiment title and objectives
- Prerequisites and setup requirements
- Step-by-step procedures with expected outputs
- Command examples with explanations
- Screenshot evidence at key points
- Data analysis and interpretation
- Conclusions with real-world implications

**Quality Characteristics:**
- Professional technical writing
- Reproducible procedures
- Comparative analysis where applicable
- Visual documentation
- Reference to official documentation
- Performance metrics and data

---

## Repository Structure

```
DevOps-Theory-Lab/
│
├── Lab/                                    # Laboratory Experiments
│   ├── Experiment_0-Windows_Subsystem_for_Linux(WSL)_Configuration.md
│   ├── Experiment_1-Comparison_of_Virtual_Machines(VMs)_and_Containers.md
│   ├── Experiment_2-Docker_Basic_Operations.md
│   ├── Experiment_3-Deploying_NGINX_Using_Different_Base_Images...md
│   └── Experiment_4-Docker_Essentials.md
│
├── Asset/                                  # Visual Documentation & Screenshots
│   ├── Lab_0/
│   │   ├── 0-1.png through 0-6.png       (WSL Configuration)
│   │
│   ├── Lab_1/
│   │   ├── 1-1.png through 1-10.png      (VMs vs Containers Comparison)
│   │
│   ├── Lab_2/
│   │   ├── 2-1.png through 2-7.png       (Docker Basic Operations)
│   │
│   └── Lab_3/
│       ├── 3-1.png through 3-8.png       (NGINX Base Images Analysis)
│
├── Theory/                                 # Classroom Theory Sessions (Planned)
│   ├── Virtualization_Fundamentals/
│   ├── Docker_Architecture/
│   ├── Container_Networking/
│   └── DevOps_Practices/
│
├── README.md                               # Main Documentation (This File)
├── _config.yml                             # GitHub Pages Jekyll Configuration
└── .gitignore                              # Git Ignore Rules
```

**Directory Organization:**

- **Lab/** - Complete experiment documentation with markdown files
- **Asset/** - Screenshot evidence organized by experiment number
- **Theory/** - Classroom materials and theoretical concepts
- **Root Files** - Configuration and documentation index

---

## Key Features & Highlights

**Comprehensive Documentation**
Each experiment includes detailed procedures, expected outputs, command examples, and visual evidence through screenshots. Documentation follows academic standards while maintaining practical focus.

**Performance Analysis**
Experiments include comparative metrics and analysis, demonstrating concrete differences between technologies and approaches through measurable data.

**Progressive Complexity**
Experiments build systematically from foundational setup through advanced optimization, with each building on previous knowledge and creating practical skills progression.

**Real-World Application**
Theory connects to practice, and each experiment includes discussion of real-world implications and industry applications of learned concepts.

**Professional Standards**
All work maintains consistency in formatting, structure, and quality, suitable for academic submission and professional portfolio representation.

---

## Technology & Tools Overview

**Development Environment**
- Windows 11 as host operating system
- WSL2 providing Linux compatibility layer
- Ubuntu 22.04 for Linux development work
- Git for version control and collaboration

**Containerization Platform**
- Docker Engine for container runtime
- Docker Hub for image registry and distribution
- Docker Compose for multi-container orchestration
- Alpine, Ubuntu, Debian as container base images

**Infrastructure & Virtualization**
- VirtualBox for virtual machine hosting
- Vagrant for VM provisioning and management
- NGINX as containerization example application
- Apache for web server comparisons

**DevOps Technologies**
- YAML configuration files
- Dockerfiles for image building
- Command-line interfaces (Bash, PowerShell)
- GitHub for code hosting and collaboration

---

## Experiment Summary

| Experiment | Focus | Key Takeaway |
|-----------|-------|--------------|
| 0 | WSL Setup | Environment ready |
| 1 | VMs vs Containers | Containers 50-100x more efficient |
| 2 | Docker Basics | Docker CLI mastery |
| 3 | Image Optimization | Alpine 85-90% smaller than Ubuntu |
| 4 | Advanced DevOps | Production-ready techniques |

---

## Contact & Support

**Student:** Srijato Das  
**Email:** srijato.119148@stu.upes.ac.in  
**GitHub:** [@Srijato-05](https://github.com/Srijato-05)  
**University:** UPES, School of Computer Science

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
