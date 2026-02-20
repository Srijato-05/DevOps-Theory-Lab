# Containerization & DevOps Portfolio

UPES | School of Computer Science | Academic Year 2025-26

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![WSL2](https://img.shields.io/badge/WSL2-0078D4?style=for-the-badge&logo=windows&logoColor=white) ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![Bash](https://img.shields.io/badge/bash-%234EAA25.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)

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

This portfolio documents comprehensive hands-on experience with containerization technologies and DevOps practices. Through carefully designed laboratory experiments, this course provides deep understanding of Docker, container orchestration, image optimization, and modern cloud-native development workflows.

The curriculum progresses from foundational concepts to advanced optimization techniques, with each experiment building upon previous knowledge. All work has been completed to professional standards with detailed documentation, performance analysis, and real-world application insights.

---

## Laboratory Experiments

### Experiment 0: Windows Subsystem for Linux Configuration

**January 24, 2026**

Establish a functional Linux development environment on Windows using WSL2 and install Git for version control. This foundational experiment sets up the development environment required for all subsequent experiments.

**What You'll Learn:**
- Installing and configuring WSL2 on Windows
- Setting up Ubuntu distribution within WSL
- Installing and configuring Git for version control
- Understanding Windows-Linux interoperability

[View Experiment 0](./Lab/Experiment%200_%20Windows%20Subsystem%20for%20Linux%20(WSL)%20Configuration.md)

---

### Experiment 1: Comparison of Virtual Machines and Containers

**January 24, 2026** 

Practical comparison of traditional virtual machines using VirtualBox/Vagrant with modern containerization using Docker. This experiment demonstrates performance differences and helps determine appropriate use cases for each technology.

**Key Topics:**
- Deploying virtual machines with Vagrant and VirtualBox
- Deploying containers with Docker
- Analyzing performance metrics: boot time, memory usage, CPU overhead
- Comparing resource efficiency and deployment speed
- Understanding isolation levels and security trade-offs

**Results Summary:**

| Metric | Virtual Machines | Containers |
|--------|-----------------|-----------|
| Boot Time | 30-60 seconds | <1 second |
| Memory (Idle) | 512MB - 1GB | 5-15MB |
| Memory (Running) | 800MB - 1.2GB | 25-50MB |
| Disk Space | 2-3GB per VM | 100-300MB per image |

Containers demonstrated significant advantages in startup time and resource consumption, making them ideal for microservices and rapid deployment scenarios.

[View Experiment 1](./Lab/Experiment%201_%20Comparison%20of%20Virtual%20Machines%20(VMs)%20and%20Containers.md)

---

### Experiment 2: Docker Installation, Configuration, and Running Images

**January 31, 2026**

Master fundamental Docker operations through hands-on image management and container lifecycle procedures. This experiment covers essential skills for working with Docker in development and production environments.

**Practical Activities:**
- Pulling images from Docker Hub
- Running containers with port mapping
- Verifying container status and connectivity
- Managing container lifecycle (start, stop, remove)
- Cleaning up unused images and containers

This experiment provides the foundation for understanding Docker operations and prepares students for more advanced container management techniques.

[View Experiment 2](./Lab/Experiment%202_Docker%20Basic%20Operations.md)

---

### Experiment 3: Deploying NGINX Using Different Base Images

**February 7, 2026**

Advanced analysis of Docker images using different base operating systems. This experiment compares the Official NGINX image, Ubuntu-based custom images, and Alpine Linux-based optimized images, examining performance, security, and size trade-offs.

**Image Comparison Analysis:**

| Base Image | Size | Startup Time | Memory | Use Case |
|-----------|------|--------------|--------|----------|
| Official (Debian) | 187 MB | ~1 second | 12 MB | Production deployments |
| Ubuntu | 320 MB | ~2 seconds | 18 MB | Development environments |
| Alpine | 28 MB | ~0.5 seconds | 4 MB | Edge and lightweight applications |

**Key Insights:**

Alpine Linux provides a 85-90% reduction in image size compared to Ubuntu-based images while maintaining full functionality. Official NGINX images offer the best balance of optimization and maintainability for production use. The experiment demonstrates that image selection significantly impacts deployment efficiency, particularly in resource-constrained environments.

**Technical Deep Dive:**
- Creating Dockerfiles with different base images
- Analyzing image layers and their impact on size
- Understanding package management differences (apt vs apk)
- Evaluating security surface and vulnerability considerations

[View Experiment 3](./Lab/Experiment%203_%20Deploying%20NGINX%20Using%20Different%20Base%20Images%20and%20Comparing%20Image%20Layers.md)

---

### Experiment 4: Docker Essentials

**Status: Planned**

This experiment will cover advanced Docker concepts including multi-stage builds, Docker Compose for orchestration, container security practices, and production-ready configurations.

[View Experiment 4](./Lab/Experiment%204_Docker%20Essentials.md)

---

## Classroom Theory Sessions

Foundational concepts and theoretical knowledge covered during classroom sessions provide context for practical experiments. Theory sessions cover:

- Virtualization architecture and evolution
- Docker ecosystem and core concepts
- Container networking and communication patterns
- Data persistence and volume management
- Dockerfile optimization techniques
- Docker API and programmatic access
- Security best practices and image scanning
- Advanced container management strategies

---

## Technology Stack

| Category | Technologies |
| :--- | :--- |
| Containerization | Docker, Docker Compose |
| Operating Systems | Windows 11, WSL2, Ubuntu 22.04, Alpine Linux |
| Cloud-Native Tools | Docker Hub, Kubernetes (planned) |
| Infrastructure | VirtualBox, Vagrant |
| Development Tools | Git, GitHub, VS Code |
| Scripting | Bash, PowerShell |
| Web Servers | NGINX, Apache |
| Configuration | Dockerfile, Docker Compose YAML, Linux Commands |

---

## Course Structure

The curriculum is organized as a progressive learning path, with each experiment building upon previous knowledge and introducing new concepts and tools.

**Foundation Phase** focuses on environment setup and understanding core concepts. Students establish their development environment, learn basic Docker operations, and understand the fundamental differences between virtualization approaches.

**Core Phase** covers practical Docker implementation through image management, container deployment, and lifecycle operations. Students gain hands-on experience with real-world workflows and best practices.

**Advanced Phase** explores optimization techniques, performance analysis, and production-ready configurations. Students learn to make informed decisions about image selection, resource allocation, and deployment strategies.

---

## Learning Outcomes

Upon completing this coursework, students will have demonstrated proficiency in:

- Understanding virtualization concepts and containerization advantages
- Installing, configuring, and managing Docker in development environments
- Pulling, running, and managing Docker containers
- Creating optimized Docker images with appropriate base systems
- Analyzing image layers and understanding size-performance trade-offs
- Comparing different deployment approaches and selecting appropriate solutions
- Implementing best practices for containerized application development
- Troubleshooting common container issues and optimizing performance

---

## Repository Contents

The repository is organized to support both laboratory work and theoretical study:

- **Lab directory** contains detailed experiment documentation and procedures
- **Asset directory** stores screenshots and visual documentation organized by experiment
- **Theory directory** houses classroom materials and supplementary resources
- **README file** serves as the main entry point and course overview

Experiments progress sequentially, with earlier content providing foundation for later, more advanced topics. Each experiment is self-contained with clear objectives and expected outcomes.

---

## Documentation Quality

All laboratory reports maintain consistent professional standards:

- Clear experiment titles and metadata
- Explicitly stated learning objectives
- Complete prerequisites and setup instructions
- Step-by-step procedures with command examples
- Expected output examples for verification
- Detailed visual documentation through screenshots
- Comparative analysis and performance data
- Real-world application context
- Comprehensive resource references

This standardized approach ensures clarity, reproducibility, and professional presentation across all experiments.

---

## Assessment and Progress

| Experiment | Completion | Difficulty | Technologies |
|-----------|-----------|-----------|----------------|
| 0 - WSL Setup | 100% | Beginner | WSL2, Ubuntu, Git |
| 1 - VMs vs Containers | 100% | Intermediate | Vagrant, VirtualBox, Docker |
| 2 - Docker Basics | 100% | Beginner | Docker CLI, Images |
| 3 - Image Optimization | 100% | Intermediate | Dockerfile, Base Images |
| 4 - Docker Essentials | 0% | Advanced | Docker Compose, Security |


---

## Repository Structure

```
DevOps-Theory-Lab/
├── Lab/
│   ├── Experiment 0_ Windows Subsystem for Linux (WSL) Configuration.md
│   ├── Experiment 1_ Comparison of Virtual Machines (VMs) and Containers.md
│   ├── Experiment 2_Docker Basic Operations.md
│   ├── Experiment 3_ Deploying NGINX Using Different Base Images...md
│   └── Experiment 4_Docker Essentials.md
├── Asset/
│   ├── Lab_0/          (Screenshots: 0-1.png through 0-6.png)
│   ├── Lab_1/          (Screenshots: 1-1.png through 1-10.png)
│   ├── Lab_2/          (Screenshots: 2-1.png through 2-7.png)
│   └── Lab_3/          (Screenshots: 3-1.png through 3-8.png)
├── Theory/             (Classroom practicals and supplementary materials)
├── README.md           (This file)
└── .gitignore
```

---

## Learning Objectives

Upon completion of this course, students will be able to:

- Understand virtualization concepts and containerization advantages  
- Deploy and manage Docker containers in production environments  
- Optimize Docker images for size, performance, and security  
- Implement container networking and data persistence strategies  
- Deploy multi-container applications using Docker Compose  
- Compare different base images and choose appropriate solutions  
- Apply DevOps best practices in containerized environments  
- Troubleshoot container issues and optimize performance

---

## Documentation Standards

All lab reports follow a standardized format:

1. **Experiment Title** - Clear, descriptive name
2. **Metadata** - Date, technology stack
3. **Objectives** - Clear learning outcomes
4. **Prerequisites** - Required knowledge and tools
5. **Procedure** - Step-by-step instructions with code blocks
6. **Expected Output** - Verification examples
7. **Screenshots** - Visual documentation of results
8. **Analysis** - Performance metrics and comparisons
9. **Conclusion** - Key takeaways and real-world applications
10. **Resources** - Links to official documentation

---

## Useful Resources

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
