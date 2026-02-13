---
title: "Lab Report: Deploying NGINX Using Different Base Images"
---

# Lab Report: Deploying NGINX Using Different Base Images

**Date:** February 13, 2026

## Objective

After completing this lab, the following competencies were achieved:

* Deploying NGINX using Official, Ubuntu-based, and Alpine-based images.
* Understanding Docker image layers and the resulting size differences.
* Comparing performance, security, and real-world use-cases of each approach.

---

## Implementation

### Part 1: Official NGINX Image

The official image is pre-optimized and uses a Debian-based OS internally.

**Command:**

```powershell
docker pull nginx:latest
docker run -d --name nginx-official -p 8080:80 nginx
```

### Part 2: Custom NGINX (Ubuntu Base)

This approach results in a larger image size with more layers, offering full OS utilities for debugging.

**Build Command:**

```powershell
docker build -t nginx-ubuntu .
```

### Part 3: Custom NGINX (Alpine Base)

Alpine provides an extremely small image, leading to faster pull and startup times.

**Build Command:**

```powershell
docker build -t nginx-alpine .
```

---

## Part 4: Comparison Analysis

### Image Size Summary

| Image Type   | Approximate Size | Primary Characteristic |
| ------------ | ---------------- | ---------------------- |
| nginx:latest | \~140 MB         | Pre-optimized          |
| nginx-ubuntu | \~220+ MB        | Full OS utilities      |
| nginx-alpine | \~25–30 MB       | Extremely small        |

### Feature Comparison

| Feature          | Official NGINX | Ubuntu + NGINX | Alpine + NGINX |
| ---------------- | -------------- | -------------- | -------------- |
| Startup Time     | Fast           | Slow           | Very Fast      |
| Security Surface | Medium         | Large          | Small          |
| Production Ready | Yes            | Rarely         | Yes            |

---

## Conclusion

Alpine-based images are ideal for microservices and cloud workloads due to their minimal footprint. Ubuntu-based images are better suited for learning internals or when heavy debugging is required.
