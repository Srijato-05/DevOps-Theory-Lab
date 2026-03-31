# Post-Deployment Verification and Testing Guide

This guide provides a comprehensive list of commands to verify, monitor, and test the status of the containerized enterprise stack. All services are launched via Docker Compose, which automatically handles network initialization.

## 1. Network Infrastructure Verification

### Inspect IPvlan Connectivity
Verify that the containers are correctly attached to the ipvlan_net network with their static IPs.
Run this command:
docker network inspect ipvlan_net

### Check Container Port Mapping
Verify that the services are correctly exposed:
- API: Port 8000
- Frontend: Port 8080
- Redis: Port 6379 (Internal Cache)

Run this command:
docker ps --filter "name=advanced"

## 2. Advanced Enterprise Services Health

### Verify Redis Caching
Confirm Redis is responding to cache operations inside the cache container:
Run this command:
docker exec advanced_redis redis-cli ping

## 3. Database and Authentication Structure

### Verify Application Database Tables
Confirm the schema includes the new users table for JWT authentication.
Run this command:
docker exec -it advanced_postgres psql -U postgres -d webapp_db -c "\dt"

## 4. API Functional Authentication Testing (JWT)

### Register a New Account
Test the /register endpoint to create a new operator account in the database.
Run this command:
docker exec advanced_fastapi curl -s -X POST -H "Content-Type: application/json" -d "{\"email\": \"operator@test.com\", \"password\": \"secure123\"}" http://localhost:8000/api/v1/register

### Acquire JWT Token (Login)
Exchange credentials for a secure Bearer token via OAuth2.
Run this command:
docker exec advanced_fastapi curl -s -X POST -d "username=operator@test.com&password=secure123" http://localhost:8000/api/v1/login

### Fetch Records Securely (GET)
Attempt to fetch all records, validating the cache and token headers.
(Replace YOUR_TOKEN with the token from the previous step).
Run this command:
docker exec advanced_fastapi curl -s -H "Authorization: Bearer YOUR_TOKEN" http://localhost:8000/api/v1/records

## 5. Maintenance and Troubleshooting

### Restart the Stack
Restart all services to test persistence and recovery.
Run this command:
docker-compose restart

### View Resource Usage
Monitor CPU and Memory consumption to verify resource limits are respected.
Run this command:
docker stats

### Remove All Resources
Clean up the containers and network (does not remove the named volume advanced_pgdata).
Run this command:
docker-compose down
