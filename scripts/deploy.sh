#!/bin/bash

# Exit Three - Deployment Script
# This script handles the complete deployment process

set -e  # Exit on error

echo "🚀 Starting Exit Three deployment..."

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Change to project root
cd "$(dirname "$0")/.."

# Function to print colored messages
print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

# Check if running as deploy user (not root)
if [ "$EUID" -eq 0 ]; then
    print_error "Please do not run this script as root. Use the 'deploy' user."
    exit 1
fi

# Check if .env files exist
print_warning "Checking environment files..."
if [ ! -f "backend/.env" ]; then
    print_error "backend/.env not found! Copy from backend/.env.example and configure."
    exit 1
fi

if [ ! -f "frontend/.env" ]; then
    print_warning "frontend/.env not found. Creating from example..."
    cp frontend/.env.example frontend/.env
fi

if [ ! -f ".env" ]; then
    print_error "Root .env not found! Create it with DB and Redis passwords."
    exit 1
fi

print_success "Environment files OK"

# Pull latest changes (if in git repo)
if [ -d ".git" ]; then
    print_warning "Pulling latest changes..."
    git pull origin main || print_warning "Git pull failed or not on main branch"
    print_success "Code updated"
fi

# Stop existing containers
print_warning "Stopping existing containers..."
docker-compose down
print_success "Containers stopped"

# Build images
print_warning "Building Docker images (this may take a few minutes)..."
docker-compose build --no-cache
print_success "Images built"

# Start services
print_warning "Starting services..."
docker-compose up -d
print_success "Services started"

# Wait for services to be healthy
print_warning "Waiting for services to be healthy..."
sleep 10

# Check if backend is healthy
if docker-compose ps | grep -q "backend.*Up.*healthy"; then
    print_success "Backend is healthy"
else
    print_error "Backend health check failed"
    docker-compose logs backend
    exit 1
fi

# Run database migrations
print_warning "Running database migrations..."
docker-compose exec -T backend python manage.py migrate --noinput
print_success "Migrations completed"

# Collect static files
print_warning "Collecting static files..."
docker-compose exec -T backend python manage.py collectstatic --noinput
print_success "Static files collected"

# Show container status
print_warning "Container status:"
docker-compose ps

# Show service URLs
echo ""
print_success "Deployment complete! 🎉"
echo ""
echo "Access your application at:"
echo "  - Frontend: https://exit3.agency"
echo "  - Backend API: https://exit3.agency/backend/api/v1/"
echo "  - Admin Panel: https://exit3.agency/backend/admin/"
echo "  - Health Check: https://exit3.agency/backend/health/"
echo ""
echo "View logs with: docker-compose logs -f"
echo "Stop services with: docker-compose down"
echo ""
