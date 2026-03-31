# Containerized Web Application with PostgreSQL

Course: DevOps Theory Lab - Project Assignment 1

## Overview
This repository contains the source code and configuration for a fully containerized, production-grade web application ecosystem. The architecture demonstrates comprehensive integration of a modular frontend, a RESTful API backend, and a PostgreSQL persistence layer, all orchestrated via Docker Compose over an advanced IPvlan network.

The project strictly adheres to mandatory architectural and functional constraints, specifically utilizing separate container environments, robust network isolation, and optimal multi-stage image construction.

---

## 1. Architectural Stack

* Frontend Client: Nginx-hosted static Single Page Application (HTML/JS/CSS).
* Backend Logic: Python FastAPI framework configured with Uvicorn.
* Primary Database: PostgreSQL 16.
* Caching Layer: Redis 7.
* Orchestration: Docker Compose (v3.9).
* Networking: Docker IPvlan (L2 mode).

---

## 2. Fulfillment of Mandatory Requirements

### 2.1 Backend Implementation
The API is written in FastAPI, exposing strict POST and GET endpoints for manipulating analytical records. State initialization is automated; tables (users, records) are dynamically created via initialization scripts (init.sql) injected directly into the PostgreSQL container on its primary boot, fulfilling the requirement for startup auto-creation without manual intervention.

### 2.2 Strict Multi-Stage Dockerfiles
All environments use highly minimal base images (alpine and slim). Both the REST API and the Frontend portal utilize explicit separated builder and runtime stages. This discards compilation dependencies, ensuring the final runtime image is secured, minimal, and explicitly executed under a strict non-root system environment.

### 2.3 Network Modeling
The deployment natively controls the instantiation of the local infrastructure. We establish an IPvlan boundary layer. IPvlan dynamically bridges container interactions directly onto the physical local area network (LAN), applying static LAN subnetting without establishing complex MAC-level overlaps that typically restrict Macvlan compatibility on wireless interfaces.

### 2.4 Persistence
PostgreSQL leverages securely localized environment variables (POSTGRES_USER, POSTGRES_DB) and mounts standard analytical data onto an orchestrator-defined named volume (advanced_pgdata), guaranteeing that tabular records persist irrespective of the container lifecycle.

---

## 3. Execution Instructions

Ensure that the Docker daemon is running and execute the following command in the repository root directory.

Run this command to build and start the containers:
docker-compose up -d --build

### Verification Steps

1. Verify Running Containers
Run this command to check the infrastructure pulse:
docker-compose ps

You should see four services in a running state: advanced_web_portal, advanced_fastapi, advanced_postgres, and advanced_redis.

2. Verify Network Assignment
Run this command to verify the containers have correctly mounted the IPvlan network:
docker network inspect ipvlan_net

3. Access the Interface
The web interface dictates HTTP traffic on port 8081, accessible symmetrically throughout the LAN at: http://localhost:8081.

For networking, architecture diagrams, and IPvlan vs Macvlan technical constraints, see the Final_Project_Report.md file.
