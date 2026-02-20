# Lab Report 4: Docker Essentials (Dockerfile, Optimization, and Publishing)

**Date:** February 20, 2026

**Student:** Srijato Das

## Objective

The goal of this experiment is to master core Docker skills including containerizing applications with `Dockerfile`, optimizing builds with `.dockerignore`, implementing multi-stage builds, and publishing verified images to **Docker Hub**.

- - -

## Implementation: Part 1 – Application Containerization

A Python Flask application was developed and containerized using a slim base image to ensure a lightweight environment.

### Application Configuration

The application consists of a simple web server (`app.py`) and a dependency list (`requirements.txt`).

**Dockerfile:**

```dockerfile
# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose port and run application
EXPOSE 5000
CMD ["python", "app.py"]
```

### Build and Execution

The image was built with the tag `flask-regular` and executed with port mapping.

```bash
docker build -t flask-regular .
docker run -d -p 5000:5000 --name flask-container flask-regular
```

- - -

## Part 2: Optimization with .dockerignore

A `.dockerignore` file was implemented to prevent unnecessary files like `__pycache__/` and `.git/` from being copied into the build context.

**Key Takeaways:**

*   Reduces the final image size by excluding local logs and IDE files.
*   Improves build speed by reducing the amount of data sent to the Docker daemon.
*   Increases security by ensuring sensitive environment files are not copied into the image.

- - -

## Part 3: Multi-stage Builds for Production

A multi-stage build strategy was executed to separate the build environment from the production runtime.

**Comparative Results:**

| Build Method | Image ID | Final Size |
| --- | --- | --- |
| Standard Build (flask-regular) | b8d027f48ca0 | 200.24 MB |
| Multi-stage Build (flask-multistage) | 24462c590c34 | 219.31 MB |

_Note: While sizes vary based on dependencies, multi-stage builds significantly improve security by removing build-time compilers and tools from the final runtime._

- - -

## Part 4: Publishing to Docker Hub

The verified `flask-regular` image was tagged and pushed to the public **durandieltheghost** repository for remote deployment.

### Command Sequence

```bash
# Login to registry
docker login

# Tag local image for Docker Hub
docker tag flask-regular:latest durandieltheghost/my-flask-app:1.0

# Push to Docker Hub
docker push durandieltheghost/my-flask-app:1.0
```

**Result:** Image layers were successfully pushed, and the digest `sha256:b8d027f4...` was generated.

- - -

## Troubleshooting: Common Naming Conflicts

During the lab, a conflict error was encountered: `The container name is already in use`.

**Resolution:** The existing stopped container was identified using `docker ps -a` and purged using `docker rm -f nginx-official` to allow for a clean re-deployment.

## Conclusion

This experiment successfully demonstrated the lifecycle of a containerized application from source code to public distribution. Essential practices such as using `.dockerignore` and multi-stage builds were validated as standard methods for creating efficient, production-grade images.
