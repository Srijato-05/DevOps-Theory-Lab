# Experiment 5: Volumes, Monitoring, and Networks

---

## Table of Contents

1. [Part 1: Docker Volumes - Persistent Data Storage](#part-1-docker-volumes---persistent-data-storage)
2. [Part 2: Environment Variables](#part-2-environment-variables)
3. [Part 3: Docker Monitoring](#part-3-docker-monitoring)
4. [Part 4: Docker Networks](#part-4-docker-networks)
5. [Part 5: Complete Real-World Example](#part-5-complete-real-world-example)
6. [Quick Reference Cheatsheet](#quick-reference-cheatsheet)
7. [Conclusion](#key-takeaways)
8. [Additional Resources](#additional-resources)

---

## Part 1: Docker Volumes - Persistent Data Storage

### Lab 1: Understanding Data Persistence

The Problem: Container Data is Ephemeral
```bash
# Create a container that writes data
docker run -it --name test-container ubuntu /bin/bash

# Inside container:
echo "Hello World" > /data/message.txt
cat /data/message.txt  # Shows "Hello World"
exit

# Restart container
docker start test-container
docker exec test-container cat /data/message.txt
# ERROR: File doesn't exist! Data was lost.
```

**Solution: Docker Volumes**

![Data Persistence Concept](../Asset/Lab_5/P1-1.png)
![Persistence Example](../Asset/Lab_5/P1-2.png)

### Lab 2: Volume Types

1. **Anonymous Volumes**
```bash
# Create anonymous volume
docker run -d -v /app/data --name web1 nginx

# Check volume
docker volume ls
```

2. **Named Volumes**
```bash
# Create named volume
docker volume create mydata

# Use named volume
docker run -d -v mydata:/app/data --name web2 nginx
```

![Named Volume](../Asset/Lab_5/P1-4.png)

3. **Bind Mounts (Host Directory)**
```bash
# Create directory on host
mkdir ~/myapp-data

# Mount host directory to container
docker run -d -v ~/myapp-data:/app/data --name web3 nginx
```

### Lab 3: Practical Volume Examples

**Example 1: Database with Persistent Storage**
```bash
docker run -d \
  --name mysql-db \
  -v mysql-data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=secret \
  mysql:8.0
```

---

## Part 2: Environment Variables

### Lab 1: Setting Environment Variables

**Method 1: Using -e flag**
```bash
docker run -d \
  --name app1 \
  -e DATABASE_URL="postgres://user:pass@db:5432/mydb" \
  -p 3000:3000 \
  my-node-app
```

**Method 2: Using --env-file**
```bash
# Create .env file
echo "DATABASE_HOST=localhost" > .env

# Use env file
docker run -d --env-file .env --name app2 my-app
```

---

## Part 3: Docker Monitoring

### Lab 1: Basic Monitoring Commands

`docker stats` - Real-time Container Metrics
```bash
docker stats
```

### Lab 2: docker top - Process Monitoring
```bash
docker top container-name
```

### Lab 3: docker logs - Application Logs
```bash
docker logs -f container-name
```

---

## Part 4: Docker Networks

### Lab 1: Network Types Explained
1. **Bridge Network (Default)**: Containers on bridge network can communicate.
2. **Host Network**: Container uses host's network directly.
3. **None Network**: No network access.
4. **Overlay Network (Swarm)**: For multi-host networking.

### Lab 2: Network Management Commands
```bash
# Create network
docker network create app-network

# Connect container to network
docker network connect app-network existing-container
```

---

## Part 5: Complete Real-World Example

```bash
# 1. Create network
docker network create myapp-network

# 2. Start database with volume
docker run -d --name postgres --network myapp-network -e POSTGRES_PASSWORD=mysecretpassword -v postgres-data:/var/lib/postgresql/data postgres:15

# 3. Start Redis
docker run -d --name redis --network myapp-network -v redis-data:/data redis:7-alpine

# 4. Start Flask app
docker run -d --name flask-app --network myapp-network -p 5000:5000 -v $(pwd)/app:/app -e DATABASE_URL="postgresql://postgres:mysecretpassword@postgres:5432/mydatabase" flask-app:latest
```

---

## Quick Reference Cheatsheet

| Category | Commands |
| :--- | :--- |
| **Volumes** | `docker volume ls`, `docker volume create <name>`, `docker run -v <volume>:/path` |
| **Env Vars** | `docker run -e VAR=value`, `docker run --env-file .env` |
| **Monitoring** | `docker stats`, `docker logs -f <container>`, `docker top <container>` |
| **Networks** | `docker network create <name>`, `docker network connect <network> <container>` |

---

## Key Takeaways

- **Volumes** persist data beyond the container lifecycle.
- **Environment Variables** configure containers dynamically.
- **Monitoring** commands (stats, logs, top) help debug and optimize.
- **Networks** enable secure and isolated container communication.

---

## Additional Resources

- [Manage data in Docker](https://docs.docker.com/storage/)
- [Docker Networking Overview](https://docs.docker.com/network/)
- [Docker Statistics Reference](https://docs.docker.com/engine/reference/commandline/stats/)
- [PostgreSQL Docker Official Image](https://hub.docker.com/_/postgres)
