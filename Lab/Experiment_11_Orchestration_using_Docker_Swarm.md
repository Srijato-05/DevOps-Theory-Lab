# Experiment 11: Orchestration using Docker Compose & Docker Swarm

## 1. Theory: Concept Continuation

### The Evolution of Container Management
In Experiment 6, we learned how to run single containers (`docker run`) and multi-container applications (`docker compose`). However, these tools have limitations in production environments.

| Tool | What it does | Limitation |
|------|--------------|------------|
| **docker run** | Runs a single container | Manual, no coordination |
| **Docker Compose**| Runs multiple containers together | Single machine, no auto-healing |

### What is Orchestration?
Orchestration is the **automatic management of containers**. Think of it like a restaurant manager:
- **Scaling**: Decides how many waiters (containers) are needed.
- **Self-healing**: Replaces a sick waiter immediately.
- **Load balancing**: Distributes customers (traffic) evenly.

### The Progression Path
`docker run` → `Docker Compose` → `Docker Swarm` → `Kubernetes`

---

## 2. Practical Tasks (Extension of Experiment 6)

### Prerequisites
- Docker installed with Swarm mode capability.
- The `docker-compose.yml` file from Experiment 6 (WordPress + MySQL).

### Task 1: Check Current State
Ensure no legacy containers are running:
```bash
# Stop existing compose setup
docker compose down -v

# Verify clean state
docker ps
```

### Task 2: Initialize Docker Swarm
Turn your machine into a **Manager Node** of a cluster:
```bash
docker swarm init
```
*Verify Swarm is active:*
```bash
docker node ls
```
**Expected Output**: You should see your hostname listed with the status `Ready` and manager status `Leader`.

### Task 3: Deploy as a Stack
In Swarm, we deploy a **Stack** (a group of services) using the same Compose file.
```bash
docker stack deploy -c docker-compose.yml wpstack
```
*Note: This creates services (managed abstractions) rather than individual manual containers.*

### Task 4: Verify the Deployment
List the services in the stack:
```bash
docker service ls
```
View the specific containers (tasks) for the WordPress service:
```bash
docker service ps wpstack_wordpress
```

### Task 5: Access WordPress
Open your browser at `http://localhost:8080`. The application works identically to the Compose version, but it is now managed by the Swarm orchestrator.

### Task 6: Scale the Application (Swarm's Superpower)
Scale WordPress from 1 to 3 replicas instantly:
```bash
docker service scale wpstack_wordpress=3
```
**Verification**:
```bash
docker service ls                # Notice REPLICAS 3/3
docker ps | grep wordpress       # Notice 3 separate containers running
```
**The Port Mystery**: In Compose, scaling would fail due to port conflicts. In Swarm, an **internal load balancer** handles port 8080 once and distributes traffic to all replicas.

### Task 7: Test Self-Healing (Automatic Recovery)
1. Find a WordPress container ID: `docker ps | grep wordpress`.
2. Kill the container: `docker kill <container-id>`.
3. Watch Swarm fix it: `docker service ps wpstack_wordpress`.
*Observation: Swarm detects the "Failed" state and immediately starts a new container to maintain the desired 3 replicas.*

### Task 8: Remove the Stack
```bash
docker stack rm wpstack
```

---

## 3. Analysis: Compose vs Swarm

| Feature | Docker Compose | Docker Swarm |
|---------|----------------|--------------|
| **Scope** | Single host only | Multi-node cluster |
| **Scaling** | Manual/Basic | Built-in (Service-based) |
| **Load Balancing**| No (Port conflicts) | Yes (Internal VIP) |
| **Self-Healing** | No | Yes (Automatic) |
| **Rolling Updates**| No | Yes (Zero downtime) |
| **Use Case** | Development, Testing | Simple production clusters |

---

## 4. Important Observations
1. **Compose File Reuse**: The same YAML file works for both tools. `docker compose up` is for dev; `docker stack deploy` is for orchestration.
2. **Containers vs Services**: In Swarm, you manage **Services** (definitions), while Swarm manages the **Containers** (instances).
3. **Infrastructure as Code**: Swarm allows you to define the *desired state* and automatically maintains it.

---

## 5. Learning Outcome Check
- **Why is Compose not enough for production?** (Think scaling and failures).
- **How does Swarm achieve self-healing?**
- **What happens if you run `docker kill` on a container managed by Swarm?**

---

## 6. Quick Reference Card
```bash
# Initialize/Leave Swarm
docker swarm init
docker swarm leave --force

# Deploy/Remove Stack
docker stack deploy -c docker-compose.yml <stack-name>
docker stack rm <stack-name>

# Manage Services
docker service ls
docker service ps <service-name>
docker service scale <service-name>=<replicas>
```
