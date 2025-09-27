# DevOps Exercise 1

This project demonstrates a simple microservices system using Docker Compose.

## Services

- **service1**: Python FastAPI app (port 8199) — main status API, talks to service2 and storage.
- **service2**: Node.js Express app (port 8002) — provides system status, logs to storage.
- **storage**: Python Flask app (port 8003) — receives and serves logs.

## Quick Start

1. Build and run all services:
  ```bash
  docker-compose up -d --build
  ```
2. Check status:
  ```bash
  curl http://localhost:8001/status
  ```
3. View logs:
  ```bash
  curl http://localhost:8001/log
  ```

### Inspect Containers
```bash
# Execute shell in service container
docker-compose exec service1 bash
docker-compose exec service2 bash
docker-compose exec storage bash
```

## 🛑 Shutdown

Stop and remove all services:
```bash
docker-compose down
```

Stop and remove all services with volumes:
```bash
docker-compose down -v
```

## 🔧 Configuration

### Environment Variables
No environment variables are required for basic operation.

### Port Configuration
- Service1: `8199:8199` (host:container)
- Service2: `8002` (internal only)
- Storage: `8003` (internal only)

### Dependencies
The services have the following dependency chain:
- Service1 → Storage
- Service2 → Storage

## 📈 Features

- **Microservices Architecture**: Decoupled services with clear responsibilities
- **Service Discovery**: Services communicate via Docker Compose networking
- **Health Monitoring**: Real-time system metrics collection
- **Fault Tolerance**: Error handling for service communication failures
- **Centralized Logging**: Unified log storage and retrieval
- **Data Persistence**: Volume-based data storage
- **Scalable Design**: Easy to extend with additional services

## 🧪 Testing

Test the application endpoints:

```bash
# Test main status endpoint
curl -X GET http://localhost:8001/status

# Test log retrieval
curl -X GET http://localhost:8001/log

# Check service health
docker-compose ps
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project is part of a DevOps exercise and is intended for educational purposes.

---
Author: Ahmad Shirwany
