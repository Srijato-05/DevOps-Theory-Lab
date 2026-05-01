# Advanced DevOps and Containerized Infrastructure Laboratory
**University of Petroleum and Energy Studies | School of Computer Science**

## 1. Laboratory Overview
This technical portfolio documents a comprehensive series of laboratory experiments focused on the architecture, deployment, and management of cloud-native infrastructure. The curriculum provides an end-to-end perspective on the DevOps lifecycle, moving from local POSIX-compliant environment virtualization to advanced cluster orchestration and automated security analysis.

## 2. Core Technical Domains
The laboratory curriculum is structured across the following specialized technical domains:

### 2.1 Containerization and Runtime Isolation
Implementation of OS-level virtualization utilizing the Docker engine to ensure environment parity and resource isolation across heterogeneous systems.

### 2.2 Infrastructure as Code (IaC) and Automation
Utilization of declarative configuration languages and agentless automation tools to enforce system state and eliminate configuration drift.

### 2.3 Continuous Integration and Delivery (CI/CD)
Construction of automated software delivery pipelines that integrate version control, automated building, and artifact management.

### 2.4 Software Quality Assurance and Static Analysis
Integration of Static Application Security Testing (SAST) into the development lifecycle to identify vulnerabilities and maintainability issues prior to runtime.

### 2.5 Distributed System Orchestration
Management of containerized workloads across clusters, implementing automated scaling, load balancing, and self-healing mechanisms.

---

## 3. Quick Reference Index

| ID | Module Title | Primary Focus |
|:---:|:---|:---|
| 0 | [WSL Configuration](./Lab/Experiment_0-Windows_Subsystem_for_Linux(WSL)_Configuration.md) | Environment Virtualization |
| 1 | [Virtualization Analysis](./Lab/Experiment_1-Comparison_of_Virtual_Machines(VMs)_and_Containers.md) | Virtualization Theory |
| 2 | [Docker Primaries](./Lab/Experiment_2-Docker_Basic_Operations.md) | Container Management |
| 3 | [Layered Architecture](./Lab/Experiment_3-Deploying_NGINX_Using_Different_Base_Images_and_Comparing_Image_Layers.md) | Storage Optimization |
| 4 | [Runtime Essentials](./Lab/Experiment_4-Docker_Essentials.md) | Runtime Configuration |
| 5 | [Data Persistence](./Lab/Experiment_5_Docker-Volumes_Monitoring_Networks.md) | Volume Management |
| 6 | [Declarative Orchestration](./Lab/Experiment_6_Docker_Run_Comparison_Docker_Compose.md) | Service Orchestration |
| 7 | [Pipeline Automation](./Lab/Experiment_7_Jenkins_Github_Docker-Hub.md) | CI/CD Integration |
| 9 | [Configuration Management](./Lab/Experiment_9_Infrastructure_Automation_using_Ansible.md) | Infrastructure as Code |
| 10 | [Static Analysis](./Lab/Experiment_10_SonarQube_Static_Code_Analysis.md) | Security Auditing |
| 11 | [Cluster Management](./Lab/Experiment_11_Orchestration_using_Docker_Swarm.md) | Basic Orchestration |
| 12 | [Advanced Orchestration](./Lab/Experiment_12_Container_Orchestration_using_Kubernetes.md) | Kubernetes API |

---

## 4. Experimental Procedures and Technical Summaries

### 4.1 Experiment 0: Windows Subsystem for Linux (WSL2) Configuration
*   **Documentation**: [Experiment 0 Manual](./Lab/Experiment_0-Windows_Subsystem_for_Linux(WSL)_Configuration.md)
*   **Summary**: Establishment of a high-performance, POSIX-compliant virtualization layer on the Windows host. This procedure focuses on kernel optimization, distribution management (Ubuntu 22.04 LTS), and the integration of the Linux kernel with the Windows file system to support native development tools.

### 4.2 Experiment 1: Comparative Analysis of Virtualization Methodologies
*   **Documentation**: [Experiment 1 Manual](./Lab/Experiment_1-Comparison_of_Virtual_Machines(VMs)_and_Containers.md)
*   **Summary**: A theoretical and empirical study comparing Hypervisor-based virtualization (Type 1 and Type 2) with OS-level containerization. The analysis focuses on resource overhead, boot latency, and isolation boundaries.

### 4.3 Experiment 2: Docker Fundamental Operations
*   **Documentation**: [Experiment 2 Manual](./Lab/Experiment_2-Docker_Basic_Operations.md)
*   **Summary**: Initial implementation of the Docker CLI for container lifecycle management. Key operations include image acquisition, container execution, state inspection, and ephemeral resource cleanup.

### 4.4 Experiment 3: NGINX Deployment and Image Layer Optimization
*   **Documentation**: [Experiment 3 Manual](./Lab/Experiment_3-Deploying_NGINX_Using_Different_Base_Images_and_Comparing_Image_Layers.md)
*   **Summary**: Examination of the Union File System (UnionFS) and the impact of image layering on storage efficiency. The lab involves deploying NGINX using various base images (Alpine vs. Ubuntu) and auditing the resulting layer metadata.

### 4.5 Experiment 4: Docker Essential Runtimes
*   **Documentation**: [Experiment 4 Manual](./Lab/Experiment_4-Docker_Essentials.md)
*   **Summary**: Configuration of advanced container runtime parameters, including environment variable injection, manual port mapping, and the execution of interactive shell sessions within isolated environments.

### 4.6 Experiment 5: Persistent Storage and Network Isolation
*   **Documentation**: [Experiment 5 Manual](./Lab/Experiment_5_Docker-Volumes_Monitoring_Networks.md)
*   **Summary**: Implementation of Docker Volumes for data persistence across container restarts and the creation of isolated bridge networks to facilitate secure inter-container communication without host-level exposure.

### 4.7 Experiment 6: Declarative Deployment with Docker Compose
*   **Documentation**: [Experiment 6 Manual](./Lab/Experiment_6_Docker_Run_Comparison_Docker_Compose.md)
*   **Summary**: A comparative study transitioning from imperative `docker run` commands to declarative multi-service orchestration using YAML. The lab features the deployment of a WordPress/MySQL stack with automated service discovery.

### 4.8 Experiment 7: Automated CI/CD Pipeline Orchestration
*   **Documentation**: [Experiment 7 Manual](./Lab/Experiment_7_Jenkins_Github_Docker-Hub.md)
*   **Summary**: Construction of an end-to-end CI/CD pipeline using Jenkins. This includes automated source code acquisition via GitHub webhooks, containerized builds, and the secure pushing of artifacts to Docker Hub using credential injection.

### 4.9 Experiment 9: Infrastructure Automation via Ansible
*   **Documentation**: [Experiment 9 Manual](./Lab/Experiment_9_Infrastructure_Automation_using_Ansible.md)
*   **Summary**: Implementation of agentless configuration management. The procedure covers SSH key distribution, inventory management, and the execution of idempotent YAML playbooks to standardize the state of remote managed nodes.

### 4.10 Experiment 10: Static Application Security Testing (SAST)
*   **Documentation**: [Experiment 10 Manual](./Lab/Experiment_10_SonarQube_Static_Code_Analysis.md)
*   **Summary**: Integration of SonarQube into the development lifecycle. The experiment focuses on automated scanning for security vulnerabilities, code smells, and technical debt, enforcing quality gates within the deployment pipeline.

### 4.11 Experiment 11: Basic Cluster Orchestration with Docker Swarm
*   **Documentation**: [Experiment 11 Manual](./Lab/Experiment_11_Orchestration_using_Docker_Swarm.md)
*   **Summary**: Transitioning from single-host Compose to multi-node cluster management. Features include service scaling, internal load balancing via the Swarm Ingress Mesh, and automated self-healing for failed container instances.

### 4.12 Experiment 12: Advanced Orchestration via Kubernetes
*   **Documentation**: [Experiment 12 Manual](./Lab/Experiment_12_Container_Orchestration_using_Kubernetes.md)
*   **Summary**: Implementation of the Kubernetes API for advanced workload management. This includes the configuration of Pods, Deployments, and NodePort Services to manage scalable and resilient containerized applications.

---

## 4. Technical Specifications and Environment
The experimental environment is standardized to ensure reproducibility and performance:
*   **Operating System**: Windows 11 Enterprise (Host) / Ubuntu 22.04 LTS (WSL2)
*   **Container Runtime**: Docker Engine v24.0.7
*   **Automation Engine**: Ansible v2.10.8
*   **CI Orchestrator**: Jenkins LTS (Containerized)
*   **Analysis Engine**: SonarQube Community Edition
*   **Orchestration API**: Kubernetes v1.29.0 (via k3d)

## 5. Infrastructure Design Principles
*   **Idempotency**: All automation procedures are designed to ensure that multiple executions yield the same system state without redundant modifications.
*   **Declarative Configuration**: Preference for Infrastructure as Code (IaC) over manual imperative execution to ensure version control and auditability.
*   **Security by Design**: Implementation of least-privilege networking and secure secret handling via environment variables and dedicated credential managers.
*   **Scalability**: Architecture designed to handle horizontal scaling through cluster orchestration.

---

## 6. Repository Organization
*   **[/Lab](./Lab)**: Detailed technical documentation and experimental procedures for all modules.
*   **[/Asset](./Asset)**: Empirical evidence, including terminal logs, architecture diagrams, and system snapshots.
*   **[/Project_Assignment](./Project_Assignment)**: Advanced implementations focused on specialized network architectures and automated security protocols.
