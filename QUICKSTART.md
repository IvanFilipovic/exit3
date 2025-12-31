# Exit Three - Quick Start Guide

Fast deployment guide for experienced DevOps engineers.

## Prerequisites
- Ubuntu 22.04 LTS droplet on DigitalOcean
- DNS for exit3.agency pointing to droplet IP
- SSH access as root or sudo user

## One-Command Setup

```bash
# On your droplet
curl -fsSL https://raw.githubusercontent.com/YOUR_USERNAME/exit3/main/scripts/quick-deploy.sh | bash
```

## Manual Quick Start

### 1. Initial Server Setup (5 minutes)

```bash
# Install Docker
curl -fsSL https://get.docker.com | sh
usermod -aG docker $USER

# Install Docker Compose
curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# Install Certbot
apt update && apt install -y certbot
```

### 2. Clone and Configure (5 minutes)

```bash
# Clone repo
git clone https://github.com/YOUR_USERNAME/exit3.git
cd exit3

# Configure environment
cp .env.example .env
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# Edit environment files (IMPORTANT!)
vim .env  # Set DB_PASSWORD and REDIS_PASSWORD
vim backend/.env  # Set SECRET_KEY, DEBUG=False, passwords
vim frontend/.env  # Set NUXT_PUBLIC_BASE_URL
```

**Critical values to set:**
```bash
# backend/.env
SECRET_KEY=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
DEBUG=False
BASIC_API_KEY=$(python3 -c 'import secrets; print(secrets.token_urlsafe(48))')
```

### 3. Get SSL Certificates (5 minutes)

```bash
# Stop any running web servers
systemctl stop nginx apache2 || true

# Get certificates
certbot certonly --standalone \
  -d exit3.agency -d www.exit3.agency \
  --non-interactive --agree-tos \
  --email admin@exit3.agency

# Copy to nginx directory
cp /etc/letsencrypt/live/exit3.agency/fullchain.pem nginx/ssl/
cp /etc/letsencrypt/live/exit3.agency/privkey.pem nginx/ssl/
```

### 4. Deploy (10 minutes)

```bash
# Run deployment script
./scripts/deploy.sh
```

The script will:
- Build all Docker images
- Start all services
- Run database migrations
- Collect static files
- Show health status

### 5. Create Admin User (1 minute)

```bash
docker-compose exec backend python manage.py createsuperuser
```

### 6. Verify (1 minute)

```bash
# Run health check
./scripts/health-check.sh

# Or manually test
curl https://exit3.agency/backend/health/
curl https://exit3.agency/
```

## Access Points

- **Frontend:** https://exit3.agency
- **API:** https://exit3.agency/backend/api/v1/
- **Admin:** https://exit3.agency/backend/admin/
- **Health:** https://exit3.agency/backend/health/

## Common Commands

```bash
# View logs
docker-compose logs -f

# Restart services
docker-compose restart

# Update application
git pull && ./scripts/deploy.sh

# Backup database
./scripts/backup-db.sh

# Health check
./scripts/health-check.sh

# Stop all services
docker-compose down

# Rebuild from scratch
docker-compose down -v
docker-compose build --no-cache
docker-compose up -d
```

## Firewall Setup

```bash
ufw default deny incoming
ufw default allow outgoing
ufw allow ssh
ufw allow 80/tcp
ufw allow 443/tcp
ufw enable
```

## Auto-Renewal for SSL

```bash
# Add to crontab
crontab -e

# Add this line
0 3 1 * * certbot renew --pre-hook "docker-compose stop nginx" --post-hook "docker-compose start nginx" --quiet
```

## Monitoring

```bash
# Container stats
docker stats

# Resource usage
htop
df -h

# Application logs
docker-compose logs -f backend
docker-compose logs -f frontend
```

## Troubleshooting

### Services won't start
```bash
docker-compose logs
docker-compose down && docker-compose up -d
```

### Database errors
```bash
docker-compose exec backend python manage.py migrate
```

### Permission errors
```bash
chown -R $USER:$USER .
```

### Clear everything and restart
```bash
docker-compose down -v
rm -rf backend/staticfiles backend/media
docker-compose up -d
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py collectstatic --noinput
```

## Security Checklist

- [ ] `DEBUG=False` in backend/.env
- [ ] Strong `SECRET_KEY` generated
- [ ] Strong `DB_PASSWORD` set
- [ ] Strong `REDIS_PASSWORD` set
- [ ] Firewall configured (UFW)
- [ ] SSL certificates installed
- [ ] Admin account created with strong password
- [ ] Backups configured
- [ ] Monitoring in place

## Production URLs

Replace `YOUR_USERNAME` in git clone command with your actual GitHub username.

For more detailed documentation, see [DEPLOYMENT.md](DEPLOYMENT.md)

---

**Total Setup Time:** ~30 minutes
**Difficulty:** Intermediate
**Last Updated:** 2025-12-31
