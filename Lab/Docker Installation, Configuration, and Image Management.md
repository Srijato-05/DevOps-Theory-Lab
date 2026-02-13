# Lab Report: Docker Installation, Configuration, and Image Management

**Date:** February 10, 2026

## Objective

The primary objective of this experiment is to gain proficiency in the core Docker workflow. This includes pulling official images from a registry, executing containers with specific port configurations, and managing the full lifecycle of containerized applications.

---

## Procedure

### Step 1: Pulling a Docker Image

The initial phase involves downloading the official Nginx image from Docker Hub to the local repository.

**Command:**

```bash
docker pull nginx
```

### Step 2: Executing a Container with Port Mapping

The container is launched in detached mode. Host port 8080 is mapped to the container's internal port 80 to enable external traffic access.

**Command:**

```bash
docker run -d -p 8080:80 nginx
```

### Step 3: Verification of Active Containers

To ensure the container is running correctly and to identify its unique ID, the process status command is executed.

**Command:**

```bash
docker ps
```

### Step 4: Managing Container Lifecycle

This phase involves stopping the active process and subsequently removing the container instance from the host system.

**Command:**

```bash
docker stop <container_id>
docker rm <container_id>
```

### Step 5: Image Removal

Finally, the Nginx image is deleted from local storage to release system resources.

**Command:**

```bash
docker rmi nginx
```

---

## Result

The experiment was completed successfully. Docker images were retrieved from the registry, containers were executed with port mapping, and all lifecycle commands were verified.

## Overall Conclusion

This lab demonstrated the practical differences between virtualization via Vagrant and VirtualBox versus containerization with Docker. The observations highlight that containers are more resource-efficient and better suited for rapid deployment and microservices. Conversely, virtual machines provide stronger isolation at the cost of higher resource overhead.
