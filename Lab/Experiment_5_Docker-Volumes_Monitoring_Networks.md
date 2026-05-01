# Experiment 5: Docker - Volumes, Environment Variables, Monitoring & Networks

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
# Create anonymous volume (auto-generated name)
docker run -d -v /app/data --name web1 nginx

# Check volume
docker volume ls
# Shows: anonymous volume with random hash

# Inspect container to see volume mount
docker inspect web1 | grep -A 5 Mounts
```
![Anonymous Volume](../Asset/Lab_5/P1-3.png)

2. **Named Volumes**
```bash
# Create named volume
docker volume create mydata

# Use named volume
docker run -d -v mydata:/app/data --name web2 nginx

# List volumes
docker volume ls
# Shows: mydata

# Inspect volume
docker volume inspect mydata
```
![Named Volume](../Asset/Lab_5/P1-4.png)

3. **Bind Mounts (Host Directory)**
```bash
# Create directory on host
mkdir ~/myapp-data

# Mount host directory to container
docker run -d -v ~/myapp-data:/app/data --name web3 nginx

# Add file on host
echo "From Host" > ~/myapp-data/host-file.txt

# Check in container
docker exec web3 cat /app/data/host-file.txt
# Shows: From Host
```

### Lab 3: Practical Volume Examples
**Example 1: Database with Persistent Storage**
```bash
# MySQL with named volume
docker run -d \
  --name mysql-db \
  -v mysql-data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=secret \
  mysql:8.0

# Check data persists
docker stop mysql-db
docker rm mysql-db

# New container with same volume
docker run -d \
  --name new-mysql \
  -v mysql-data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=secret \
  mysql:8.0
# Data is preserved!
```
![Database Persistence](../Asset/Lab_5/P1-5.png)

**Example 2: Web App with Configuration Files**
```bash
# Create config directory
mkdir ~/nginx-config

# Create nginx config file
echo 'server {
    listen 80;
    server_name localhost;
    location / {
        return 200 "Hello from mounted config!";
    }
}' > ~/nginx-config/nginx.conf

# Run nginx with config bind mount
docker run -d \
  --name nginx-custom \
  -p 8080:80 \
  -v ~/nginx-config/nginx.conf:/etc/nginx/conf.d/default.conf \
  nginx

# Test
curl http://localhost:8080
```
![Web App Config](../Asset/Lab_5/P1-6.png)

### Lab 4: Volume Management Commands
```bash
# List all volumes
docker volume ls

# Create a volume
docker volume create app-volume

# Inspect volume details
docker volume inspect app-volume

# Remove unused volumes
docker volume prune

# Remove specific volume
docker volume rm volume-name

# Copy files to/from volume
docker cp local-file.txt container-name:/path/in/volume
```
![Volume Management 1](../Asset/Lab_5/P1-7.png)
![Volume Management 2](../Asset/Lab_5/P1-8.png)
![Volume Management 3](../Asset/Lab_5/P1-9.png)

---

## Part 2: Environment Variables

### Lab 1: Setting Environment Variables
**Method 1: Using -e flag**
```bash
# Single variable
docker run -d \
  --name app1 \
  -e DATABASE_URL="postgres://user:pass@db:5432/mydb" \
  -e DEBUG="true" \
  -p 3000:3000 \
  my-node-app
```
**Method 2: Using --env-file**
```bash
# Create .env file
echo "DATABASE_HOST=localhost" > .env
echo "DATABASE_PORT=5432" >> .env
echo "API_KEY=secret123" >> .env

# Use env file
docker run -d \
  --env-file .env \
  --name app2 \
  my-app
```
![Environment Variables Setup](../Asset/Lab_5/P2-L1-1.png)
![Environment Variables Verification](../Asset/Lab_5/P2-L1-2.png)

### Lab 2: Environment Variables in Applications
**Python Flask Example**
```python
# app.py
import os
from flask import Flask

app = Flask(__name__)

# Read environment variables
db_host = os.environ.get('DATABASE_HOST', 'localhost')
debug_mode = os.environ.get('DEBUG', 'false').lower() == 'true'
api_key = os.environ.get('API_KEY')

@app.route('/config')
def config():
    return {
        'db_host': db_host,
        'debug': debug_mode,
        'has_api_key': bool(api_key)
    }

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
```
![Flask Env Example](../Asset/Lab_5/P2-L2-1.png)
![Dockerfile Env Example](../Asset/Lab_5/P2-L2-2.png)

### Lab 3: Test Environment Variables
```bash
# Run with custom env vars
docker run -d \
  --name flask-app \
  -p 5000:5000 \
  -e DATABASE_HOST="prod-db.example.com" \
  -e DEBUG="true" \
  -e PORT="8080" \
  flask-app

# Check environment in running container
docker exec flask-app env
docker exec flask-app printenv DATABASE_HOST

# Test the endpoint
curl http://localhost:5000/config
```

---

## Part 3: Docker Monitoring

### Lab 1: Basic Monitoring Commands
`docker stats` - Real-time Container Metrics
```bash
# Live stats for all containers
docker stats

# Specific format output
docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}"
```
![Docker Stats 1](../Asset/Lab_5/P3-L1-1.png)
![Docker Stats 2](../Asset/Lab_5/P3-L1-2.png)

### Lab 2: docker top - Process Monitoring
```bash
# View processes in container
docker top container-name

# View with full command line
docker top container-name -ef
```
![Docker Top](../Asset/Lab_5/P3-L2-1.png)

### Lab 3: docker logs - Application Logs
```bash
# View logs
docker logs container-name

# Follow logs (like tail -f)
docker logs -f container-name
```
![Docker Logs](../Asset/Lab_5/P3-L3-1.png)

### Lab 4: Container Inspection
```bash
# Detailed container info
docker inspect container-name

# Specific information
docker inspect --format='{{.State.Status}}' container-name
```
![Container Inspection 1](../Asset/Lab_5/P3-L4-1.png)
![Container Inspection 2](../Asset/Lab_5/P3-L4-2.png)
![Container Inspection 3](../Asset/Lab_5/P3-L4-3.png)
![Container Inspection 4](../Asset/Lab_5/P3-L4-4.png)

### Lab 5: Events Monitoring
```bash
# Monitor Docker events in real-time
docker events

# Filter events
docker events --filter 'type=container'
```
![Events Monitoring 1](../Asset/Lab_5/P3-L5-1.png)
![Events Monitoring 2](../Asset/Lab_5/P3-L5-2.png)
![Events Monitoring 3](../Asset/Lab_5/P3-L5-3.png)

### Lab 6: Practical Monitoring Script
```bash
#!/bin/bash
# monitor.sh - Simple Docker monitoring

echo "=== Docker Monitoring Dashboard ==="
echo "Time: $(date)"
echo

echo "1. Running Containers:"
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
echo

echo "2. Resource Usage:"
docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.BlockIO}}"
echo

echo "3. Recent Events:"
docker events --since '5m' --until '0s' --format '{{.Time}} {{.Type}} {{.Action}}' | tail -5
echo

echo "4. System Info:"
docker system df
```

---

## Part 4: Docker Networks

### Lab 1: Understanding Docker Network Types
```bash
# List Networks
docker network ls
```

### Lab 2: Network Types Explained
1. **Bridge Network (Default)**: Containers on bridge network can communicate. Each container gets its own IP.
2. **Host Network**: Container uses host's network directly. No network isolation.
3. **None Network**: No network access. Only loopback interface.
4. **Overlay Network (Swarm)**: For multi-host networking.

### Lab 3: Network Management Commands
```bash
# Create network
docker network create app-network

# Connect container to network
docker network connect app-network existing-container

# Remove network
docker network rm network-name
```

### Lab 4: Multi-Container Application Example
**Web App + Database Communication**
```bash
# Create network
docker network create app-network

# Start database
docker run -d \
  --name postgres-db \
  --network app-network \
  -e POSTGRES_PASSWORD=secret \
  -v pgdata:/var/lib/postgresql/data \
  postgres:15

# Start web application
docker run -d \
  --name web-app \
  --network app-network \
  -p 8080:3000 \
  -e DATABASE_URL="postgres://postgres:secret@postgres-db:5432/mydb" \
  -e DATABASE_HOST="postgres-db" \
  node-app
```

### Lab 5: Network Inspection & Debugging
```bash
# Inspect network
docker network inspect bridge

# Check container IP
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container-name
```

### Lab 6: Port Publishing vs Exposing
```bash
# PORT PUBLISHING (host:container)
docker run -d -p 80:8080 --name app1 nginx

# Dynamic port publishing
docker run -d -p 8080 --name app2 nginx
```

---

## Part 5: Complete Real-World Example
**Infrastructure:**
- Flask Web App (port 5000)
- PostgreSQL Database (port 5432)
- Redis Cache (port 6379)
- All connected via custom network `myapp-network`

```bash
# 1. Create network
docker network create myapp-network

# 2. Start database with volume
docker run -d --name postgres --network myapp-network -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_DB=mydatabase -v postgres-data:/var/lib/postgresql/data postgres:15

# 3. Start Redis
docker run -d --name redis --network myapp-network -v redis-data:/data redis:7-alpine

# 4. Start Flask app
docker run -d --name flask-app --network myapp-network -p 5000:5000 -v $(pwd)/app:/app -v app-logs:/var/log/app -e DATABASE_URL="postgresql://postgres:mysecretpassword@postgres:5432/mydatabase" -e REDIS_URL="redis://redis:6379" flask-app:latest
```

---

## Quick Reference Cheatsheet
| Category | Commands |
| :--- | :--- |
| **Volumes** | `docker volume ls`, `docker volume create <name>`, `docker run -v <volume>:/path` |
| **Env Vars** | `docker run -e VAR=value`, `docker run --env-file .env`, `Dockerfile: ENV VAR=value` |
| **Monitoring** | `docker stats`, `docker logs -f <container>`, `docker top <container>` |
| **Networks** | `docker network create <name>`, `docker network connect <network> <container>` |

## Practice Exercises
1. **Database Backup**: Use `docker cp` or volume backup techniques to restore data to a new container.
2. **Multi-Service Setup**: Create a web app + database + cache using a custom network.
3. **Log Analysis**: Redirect logs to a file on host using bind mount.
4. **Network Isolation**: Create two separate networks and test container connectivity between them.

## Cleanup
```bash
# Stop and remove all containers
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)

# Remove unused resources
docker volume prune -f
docker network prune -f
docker image prune -f
```

## Key Takeaways
- **Volumes** persist data beyond the container lifecycle.
- **Environment Variables** configure containers dynamically.
- **Monitoring** commands (stats, logs, top) help debug and optimize.
- **Networks** enable secure and isolated container communication.
