#!/bin/bash

# Exit Three - Health Check Script

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Change to project root
cd "$(dirname "$0")/.."

echo "🏥 Exit Three Health Check"
echo "=========================="
echo ""

# Check Docker
echo -n "Docker daemon: "
if docker info > /dev/null 2>&1; then
    echo -e "${GREEN}✓ Running${NC}"
else
    echo -e "${RED}✗ Not running${NC}"
    exit 1
fi

# Check Docker Compose
echo -n "Docker Compose: "
if command -v docker-compose > /dev/null 2>&1; then
    echo -e "${GREEN}✓ Installed${NC}"
else
    echo -e "${RED}✗ Not installed${NC}"
    exit 1
fi

echo ""
echo "Container Status:"
echo "-----------------"

# Check each service
SERVICES=("db" "redis" "backend" "frontend" "nginx")

for service in "${SERVICES[@]}"; do
    echo -n "$service: "
    if docker-compose ps | grep -q "$service.*Up.*healthy\|$service.*Up"; then
        if docker-compose ps | grep -q "$service.*Up.*healthy"; then
            echo -e "${GREEN}✓ Healthy${NC}"
        else
            echo -e "${YELLOW}⚠ Running (no health check)${NC}"
        fi
    else
        echo -e "${RED}✗ Not running${NC}"
    fi
done

echo ""
echo "Endpoint Health:"
echo "----------------"

# Check backend health
echo -n "Backend API: "
BACKEND_HEALTH=$(curl -s -o /dev/null -w "%{http_code}" http://localhost/backend/health/ 2>/dev/null || echo "000")
if [ "$BACKEND_HEALTH" = "200" ]; then
    echo -e "${GREEN}✓ Healthy (200)${NC}"
else
    echo -e "${RED}✗ Failed ($BACKEND_HEALTH)${NC}"
fi

# Check frontend
echo -n "Frontend: "
FRONTEND_HEALTH=$(curl -s -o /dev/null -w "%{http_code}" http://localhost/ 2>/dev/null || echo "000")
if [ "$FRONTEND_HEALTH" = "200" ]; then
    echo -e "${GREEN}✓ Healthy (200)${NC}"
else
    echo -e "${RED}✗ Failed ($FRONTEND_HEALTH)${NC}"
fi

# Check admin
echo -n "Admin Panel: "
ADMIN_HEALTH=$(curl -s -o /dev/null -w "%{http_code}" http://localhost/backend/admin/ 2>/dev/null || echo "000")
if [ "$ADMIN_HEALTH" = "301" ] || [ "$ADMIN_HEALTH" = "302" ] || [ "$ADMIN_HEALTH" = "200" ]; then
    echo -e "${GREEN}✓ Accessible ($ADMIN_HEALTH)${NC}"
else
    echo -e "${RED}✗ Failed ($ADMIN_HEALTH)${NC}"
fi

echo ""
echo "Resource Usage:"
echo "---------------"

# Show container stats (non-streaming)
docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}"

echo ""
echo "Disk Usage:"
echo "-----------"
df -h / | tail -1 | awk '{print "Root: " $3 " used of " $2 " (" $5 " used)"}'

echo ""
echo "Docker Volumes:"
docker volume ls | grep exit3 || echo "No volumes found"

echo ""
echo "Recent Logs (last 10 lines):"
echo "----------------------------"
docker-compose logs --tail=10 | head -20

echo ""
echo "✓ Health check complete!"
