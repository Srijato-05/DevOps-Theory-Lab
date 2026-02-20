  Lab Report: NGINX Base Image Comparison and Layer Analysis

# Lab Report: Deploying NGINX Using Different Base Images

**Date:** February 20, 2026

## Lab Objectives

After completing this lab, the following competencies are achieved:

*   Deployment of NGINX using Official, Ubuntu-based, and Alpine-based images.
*   Understanding of Docker image layers and the resulting size differences.
*   Comparison of performance, security, and use-cases for each deployment strategy.
*   Explanation of real-world NGINX applications in containerized ecosystems.

## Prerequisites

*   Docker installed and operational.
*   Basic proficiency with `docker run`, `Dockerfile`, port mapping, and Linux command basics.

- - -

## Part 1: Deploy NGINX Using Official Image

The recommended approach for production involves using the pre-optimized official image.

### Implementation Steps

1.  **Pull the Image:**
    
    ```bash
    docker pull nginx:latest
    ```
    
2.  **Run the Container:**
    
    ```bash
    docker run -d --name nginx-official -p 8080:80 nginx
    ```
    
3.  **Verify:** Execute `curl http://localhost:8080` to view the NGINX welcome page.

### Key Observations

*   The image is pre-optimized and requires minimal configuration.
*   Internally, it utilizes a Debian-based operating system.

- - -

## Part 2: Custom NGINX Using Ubuntu Base Image

This approach uses a full Ubuntu distribution as the foundation for the NGINX service.

### Step 1: Create Dockerfile

```dockerfile
FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

### Step 2: Build and Run

```bash
docker build -t nginx-ubuntu .
docker run -d --name nginx-ubuntu -p 8081:80 nginx-ubuntu
```

### Observations

*   The resulting image size is significantly larger.
*   It contains more layers but provides access to full OS utilities.

- - -

## Part 3: Custom NGINX Using Alpine Base Image

Alpine Linux is a security-oriented, lightweight Linux distribution.

### Step 1: Create Dockerfile

```dockerfile
FROM alpine:latest

RUN apk add --no-cache nginx

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

### Step 2: Build and Run

```bash
docker build -t nginx-alpine .
docker run -d --name nginx-alpine -p 8082:80 nginx-alpine
```

### Observations

*   The image is extremely small with fewer packages.
*   It features faster pull and startup times.

- - -

## Part 4: Image Size and Layer Comparison

### Size Comparison Matrix

| Image Type | Approximate Size | Characteristics |
| --- | --- | --- |
| nginx:latest | ~140 MB | Pre-optimized, Production Ready |
| nginx-ubuntu | ~220+ MB | Excellent Debugging Tools, Large Surface |
| nginx-alpine | ~25–30 MB | Very Fast, Small Security Surface |

### Inspect Layers

To analyze the construction of these images, the following history commands are used:

```bash
docker history nginx
docker history nginx-ubuntu
docker history nginx-alpine
```

**Final Observations:**

*   **Ubuntu:** Features many filesystem layers due to the comprehensive base OS.
*   **Alpine:** Contains minimal layers, reflecting its lightweight design.
*   **Official Image:** Heavily optimized, though larger than the Alpine variant.
