# Exit Three - DigitalOcean Deployment Guide

Complete guide for deploying the Exit Three full-stack application (Django backend + Nuxt frontend) to a DigitalOcean droplet.

---

## 📋 Prerequisites

- DigitalOcean account
- Domain `exit3.agency` pointed to your droplet IP
- SSH access to your droplet
- Basic knowledge of Linux and Docker

---

## 🚀 Part 1: Droplet Setup

### Step 1: Create DigitalOcean Droplet

1. **Log into DigitalOcean**
2. **Create Droplet:**
   - **Distribution:** Ubuntu 22.04 LTS
   - **Plan:** Basic ($12/month minimum - 2GB RAM, 1 CPU)
   - **Datacenter:** Choose closest to your users
   - **Authentication:** SSH Key (recommended)
   - **Hostname:** exit3-production

3. **Note your droplet IP address**

### Step 2: Configure Domain DNS

In your domain registrar (where you bought exit3.agency):

```
Type    Name    Value               TTL
A       @       YOUR_DROPLET_IP     3600
A       www     YOUR_DROPLET_IP     3600
```

Wait 5-10 minutes for DNS propagation. Verify with:
```bash
dig exit3.agency
dig www.exit3.agency
```

---

## 🔧 Part 2: Server Configuration

### Step 3: Initial Server Setup

SSH into your droplet:
```bash
ssh root@YOUR_DROPLET_IP
```

**Update system:**
```bash
apt update && apt upgrade -y
```

**Create deploy user:**
```bash
adduser deploy
usermod -aG sudo deploy
su - deploy
```

**Install Docker:**
```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add user to docker group
sudo usermod -aG docker $USER

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Verify installation
docker --version
docker-compose --version

# Logout and login again to apply group changes
exit
su - deploy
```

**Install additional tools:**
```bash
sudo apt install -y git curl wget vim htop certbot python3-certbot-nginx
```

---

## 📦 Part 3: Deploy Application

### Step 4: Clone Repository

```bash
cd ~
git clone https://github.com/YOUR_USERNAME/exit3.git
cd exit3
```

### Step 5: Configure Environment Variables

**Backend environment:**
```bash
cd ~/exit3/backend
cp .env.example .env
vim .env
```

**Edit the following critical values:**
```bash
# Generate new SECRET_KEY
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

# In .env file:
SECRET_KEY=<generated_key_above>
DEBUG=False
DJANGO_ENV=production
ALLOWED_HOSTS=exit3.agency,www.exit3.agency
BASIC_API_KEY=<generate_with_secrets_token_urlsafe_48>
REDIS_PASSWORD=<strong_password>

# Note: SQLite database will be created automatically, no DB credentials needed
```

**Frontend environment:**
```bash
cd ~/exit3/frontend
cp .env.example .env
vim .env
```

**Edit:**
```bash
NUXT_PUBLIC_BASE_URL=https://exit3.agency
NODE_ENV=production
```

**Root environment (for docker-compose):**
```bash
cd ~/exit3
vim .env
```

**Add:**
```bash
REDIS_PASSWORD=<same_as_backend>

# Note: SQLite database will be stored in a Docker volume, no additional configuration needed
```

### Step 6: Set Up SSL Certificates (Let's Encrypt)

**Option 1: Using Certbot (Recommended for first time)**

Stop nginx if running:
```bash
docker-compose down
```

Get SSL certificates:
```bash
sudo certbot certonly --standalone \
  -d exit3.agency \
  -d www.exit3.agency \
  --non-interactive \
  --agree-tos \
  --email admin@exit3.agency
```

Copy certificates to nginx directory:
```bash
sudo cp /etc/letsencrypt/live/exit3.agency/fullchain.pem ~/exit3/nginx/ssl/
sudo cp /etc/letsencrypt/live/exit3.agency/privkey.pem ~/exit3/nginx/ssl/
sudo chown deploy:deploy ~/exit3/nginx/ssl/*
```

**Option 2: Using Docker Certbot (After initial setup)**

See renewal section below.

### Step 7: Build and Start Containers

**Build images:**
```bash
cd ~/exit3
docker-compose build
```

**Start services:**
```bash
docker-compose up -d
```

**Check status:**
```bash
docker-compose ps
docker-compose logs -f
```

You should see all services healthy.

### Step 8: Initialize Database

**Run migrations:**
```bash
docker-compose exec backend python manage.py migrate
```

**Create superuser:**
```bash
docker-compose exec backend python manage.py createsuperuser
```

**Collect static files:**
```bash
docker-compose exec backend python manage.py collectstatic --noinput
```

### Step 9: Verify Deployment

**Check health endpoints:**
```bash
curl https://exit3.agency/backend/health/
curl https://exit3.agency/
```

**Access admin panel:**
```
https://exit3.agency/backend/admin/
```

**Test API:**
```bash
curl -X POST https://exit3.agency/backend/api/v1/leads/ \
  -H "Authorization: Basic YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "full_name": "Test User",
    "position": "Developer",
    "email": "test@example.com",
    "source": "website",
    "category": "web_dev"
  }'
```

---

## 🔄 Part 4: Maintenance

### SSL Certificate Renewal

Let's Encrypt certificates expire every 90 days. Set up auto-renewal:

**Create renewal script:**
```bash
sudo vim /usr/local/bin/renew-ssl.sh
```

**Add:**
```bash
#!/bin/bash
cd /home/deploy/exit3
docker-compose stop nginx
certbot renew --quiet
cp /etc/letsencrypt/live/exit3.agency/fullchain.pem /home/deploy/exit3/nginx/ssl/
cp /etc/letsencrypt/live/exit3.agency/privkey.pem /home/deploy/exit3/nginx/ssl/
chown deploy:deploy /home/deploy/exit3/nginx/ssl/*
docker-compose start nginx
```

**Make executable:**
```bash
sudo chmod +x /usr/local/bin/renew-ssl.sh
```

**Add to crontab:**
```bash
sudo crontab -e
```

**Add line:**
```
0 3 1 * * /usr/local/bin/renew-ssl.sh >> /var/log/ssl-renewal.log 2>&1
```

### Database Backups

**Create backup script:**
```bash
vim ~/backup-db.sh
```

**Add:**
```bash
#!/bin/bash
BACKUP_DIR="/home/deploy/exit3/backend/backups"
DATE=$(date +%Y%m%d_%H%M%S)
mkdir -p $BACKUP_DIR
cd /home/deploy/exit3
# Copy SQLite database file from container
docker cp exit3_backend:/app/db.sqlite3 $BACKUP_DIR/backup_$DATE.sqlite3
# Delete backups older than 7 days
find $BACKUP_DIR -name "backup_*.sqlite3" -mtime +7 -delete
echo "Backup completed: backup_$DATE.sqlite3"
```

**Make executable:**
```bash
chmod +x ~/backup-db.sh
```

**Add to crontab:**
```bash
crontab -e
```

**Add:**
```
0 2 * * * /home/deploy/backup-db.sh >> /var/log/db-backup.log 2>&1
```

### Updating Application

**Pull latest changes:**
```bash
cd ~/exit3
git pull origin main
```

**Rebuild and restart:**
```bash
docker-compose build
docker-compose up -d
```

**Run migrations if needed:**
```bash
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py collectstatic --noinput
```

### Monitoring Logs

**View all logs:**
```bash
docker-compose logs -f
```

**View specific service:**
```bash
docker-compose logs -f backend
docker-compose logs -f frontend
docker-compose logs -f nginx
```

**Django logs:**
```bash
docker-compose exec backend tail -f logs/django.log
```

**Nginx logs:**
```bash
tail -f ~/exit3/nginx/logs/access.log
tail -f ~/exit3/nginx/logs/error.log
```

---

## 🔐 Part 5: Security

### Firewall Configuration

**Set up UFW:**
```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
sudo ufw status
```

### Fail2Ban (Optional but recommended)

**Install:**
```bash
sudo apt install fail2ban -y
```

**Configure:**
```bash
sudo vim /etc/fail2ban/jail.local
```

**Add:**
```ini
[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 3600

[nginx-http-auth]
enabled = true
filter = nginx-http-auth
port = http,https
logpath = /home/deploy/exit3/nginx/logs/error.log
maxretry = 5
```

**Start:**
```bash
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
```

---

## 📊 Part 6: Monitoring

### Install Monitoring Tools

**Netdata (optional):**
```bash
bash <(curl -Ss https://my-netdata.io/kickstart.sh)
```

Access at: `http://YOUR_IP:19999`

### Docker Stats

```bash
docker stats
```

### System Resources

```bash
htop
df -h
free -h
```

---

## 🆘 Troubleshooting

### Container won't start

```bash
docker-compose logs SERVICE_NAME
docker-compose down
docker-compose up -d
```

### Database issues

```bash
# Check if SQLite database exists
docker-compose exec backend ls -lh /app/db.sqlite3

# Access SQLite database for debugging
docker-compose exec backend python manage.py dbshell
```

### Permission errors

```bash
sudo chown -R deploy:deploy ~/exit3
```

### Nginx errors

```bash
docker-compose exec nginx nginx -t  # test config
docker-compose restart nginx
```

### Reset everything (CAUTION)

```bash
docker-compose down -v
docker system prune -a
# Then rebuild from Step 7
```

---

## 📞 Support

For issues:
1. Check logs: `docker-compose logs`
2. Check health: `docker-compose ps`
3. Check backend Claude.md for configuration details
4. Check GitHub issues

---

## ✅ Deployment Checklist

- [ ] Droplet created and accessible
- [ ] DNS configured and propagated
- [ ] Docker and Docker Compose installed
- [ ] Repository cloned
- [ ] Environment variables configured
- [ ] SSL certificates obtained
- [ ] Containers built and running
- [ ] Database migrated
- [ ] Static files collected
- [ ] Superuser created
- [ ] Health checks passing
- [ ] Firewall configured
- [ ] SSL auto-renewal set up
- [ ] Database backups configured
- [ ] Monitoring in place

---

**Last Updated:** 2025-12-31
**Version:** 1.0.0
