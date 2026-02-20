# Experiment 2: Docker Installation, Configuration, and Running Images

**Date:** 31st January 2026
---

## Table of Contents

1. [Objective](#objective)
2. [Procedure](#procedure)
3. [Result](#result)
4. [Conclusion](#conclusion)

---

## Objective

- Pull Docker images
- Run containers
- Manage container lifecycle

---

## Procedure

### Step 1: Pull Image

Pull the Nginx image from Docker Hub:

```bash
docker pull nginx
```

![Pull Docker Image](../Asset/Lab_2/2-1.png)

---

### Step 2: Run Container with Port Mapping

Run a container with port mapping (host port 8080 to container port 80):

```bash
docker run -d -p 8080:80 nginx
```

![Run Container with Port Mapping](../Asset/Lab_2/2-2.png)

---

### Step 3: Verify Running Containers

List all running containers:

```bash
docker ps
```

![Verify Running Containers](../Asset/Lab_2/2-4.png)

---

### Step 4: Stop and Remove Container

Stop the running container and remove it:

```bash
docker stop <container_id>
docker rm <container_id>
```

![Stop Container](../Asset/Lab_2/2-6.png)

![Remove Container](../Asset/Lab_2/2-7.png)

---

### Step 5: Remove Image

Remove the Docker image:

```bash
docker rmi nginx
```

![Remove Image](../Asset/Lab_2/2-5.png)

---

## Result

Docker images were successfully pulled, containers executed, and lifecycle commands performed.

![Result Summary](../Asset/Lab_2/2-6.png)

---

## Conclusion

This lab demonstrated containerization using Docker, highlighting container management basics. Containers are better suited for rapid deployment and microservices, while VMs provide stronger isolation.

---

## Additional Resources

- [Docker Official Documentation](https://docs.docker.com/)
- [Docker Images Documentation](https://docs.docker.com/get-started/docker-concepts/building-images/)
- [Docker CLI Reference](https://docs.docker.com/engine/reference/commandline/docker/)
- [Docker Hub Registry](https://hub.docker.com/)
- [Docker Getting Started Guide](https://docs.docker.com/get-started/)
