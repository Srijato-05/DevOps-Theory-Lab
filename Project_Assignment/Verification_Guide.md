# Post-Deployment Verification & Testing Guide

This guide provides a comprehensive list of commands to verify, monitor, and test the status of the containerized FastAPI + PostgreSQL stack. All commands should be run from the project root directory.

## 1. Network Infrastructure Verification

### Inspect Macvlan Connectivity
Verify that the containers are correctly attached to the `backend_macvlan` network with their static IPs.
```powershell
docker network inspect backend_macvlan
```

### Check Container Port Mapping
Verify that the API is exposed on port 8000.
```powershell
docker ps --filter "name=advanced"
```

## 2. Service Health & Logs

### Check Real-time Service Status
View the health status and current state of the orchestrated services.
```powershell
docker-compose ps
```

### Stream Application Logs
Monitor the logs for both the API and Database simultaneously.
```powershell
docker-compose logs -f
```

### Inspect Database Startup
Check specifically for PostgreSQL initialization and config loading.
```powershell
docker logs advanced_postgres
```

## 3. Database & Migrations

### Verify Alembic Migration History
Confirm that the database schema is at the latest version.
```powershell
docker exec advanced_fastapi alembic history --verbose
```

### Check Current Database Schema State
Verify which revision is currently applied to the database.
```powershell
docker exec advanced_fastapi alembic current
```

### Access PostgreSQL CLI
Connect directly to the database to run manual SQL queries.
```powershell
docker exec -it advanced_postgres psql -U postgres -d webapp_db
```
*Inside psql, try:* `\dt` *(list tables) or* `SELECT * FROM records;`

## 4. API Functional Testing (CRUD)

### Health Check Endpoint
Verify the API is responsive.
```powershell
docker exec advanced_fastapi curl -s http://localhost:8000/api/v1/health
```

### Insert a Record (POST)
Test the database write capability via the FastAPI endpoint.
```powershell
docker exec advanced_fastapi curl -s -X POST -H "Content-Type: application/json" -d "{\`"name\`": \`"Verification Test\`", \`"description\`": \`"Manual verification command executed\`"}" http://localhost:8000/api/v1/records
```

### Fetch All Records (GET)
Verify the database read capability and data persistence.
```powershell
docker exec advanced_fastapi curl -s http://localhost:8000/api/v1/records
```

## 5. Maintenance & Troubleshooting

### Restart the Stack
Restart all services to test persistence and recovery.
```powershell
docker-compose restart
```

### View Resource Usage
Monitor CPU and Memory consumption to verify resource limits are respected.
```powershell
docker stats advanced_fastapi advanced_postgres
```

### Remove All Resources
Clean up the containers and network (does not remove the named volume `advanced_pgdata`).
```powershell
docker-compose down
```
