# Lab Report: Docker Installation, Configuration, and Image Management

**Date:** February 10, 2026

## Objective

The primary goal of this experiment is to gain proficiency in the core Docker workflow. Key objectives include:

* Pulling official Docker images from remote registries.
* Executing containers with specific port mapping configurations.
* Managing the complete container lifecycle, from execution to removal.

---

## Procedure

### Step 1: Pulling a Docker Image

The initial phase involves retrieving the official Nginx image from the repository.

**Command:**

```bash
docker pull nginx
```

### Step 2: Executing Container with Port Mapping

The container is launched in detached mode, mapping host port 8080 to the container's internal port 80.

**Command:**

```bash
docker run -d -p 8080:80 nginx
```

### Step 3: Verification of Active Containers

The current state of running containers is verified to confirm successful execution.

**Command:**

```bash
docker ps
```

### Step 4: Stop and Remove Container

The active container instance is stopped and subsequently removed from the system.

**Command:**

```bash
docker stop <container_id>
docker rm <container_id>
```

### Step 5: Image Removal

The Nginx image is deleted from local storage to clean up system resources.

**Command:**

```bash
docker rmi nginx
```

---

## Result and Conclusion

The experiment was successful, with all lifecycle commands performed as expected. This lab demonstrated that containers are better suited for rapid deployment and microservices, while virtual machines provide stronger isolation.
