# Exit Three Django Backend

Django REST API backend for Exit Three CRM and Lead Management System.

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL 16+ (or Docker)
- Redis (optional, for caching)

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd exit3/backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements-dev.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and update the values
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

Visit: http://localhost:8000/backend/admin/

## 🐳 Docker Deployment

### Quick Start with Docker Compose

1. **Copy environment file**
   ```bash
   cp .env.example .env
   # IMPORTANT: Update all passwords and secret keys in .env
   ```

2. **Build and start services**
   ```bash
   docker-compose up -d --build
   ```

3. **Run migrations**
   ```bash
   docker-compose exec django python manage.py migrate
   ```

4. **Create superuser**
   ```bash
   docker-compose exec django python manage.py createsuperuser
   ```

5. **Collect static files**
   ```bash
   docker-compose exec django python manage.py collectstatic --noinput
   ```

### Service URLs

- **Django API**: http://localhost:8000/backend/api/
- **Django Admin**: http://localhost:8000/backend/admin/
- **API Documentation**: http://localhost:8000/backend/api/docs/
- **Health Check**: http://localhost:8000/backend/health/
- **pgAdmin** (optional): http://localhost:5050

### Useful Docker Commands

```bash
# View logs
docker-compose logs -f django

# Restart services
docker-compose restart

# Stop all services
docker-compose down

# Stop and remove volumes (CAUTION: deletes database!)
docker-compose down -v

# Access Django shell
docker-compose exec django python manage.py shell

# Run tests
docker-compose exec django pytest

# Create database backup
docker-compose exec db pg_dump -U postgres exit3_db > backup.sql
```

## 📁 Project Structure

```
backend/
├── backend/              # Django project settings
│   ├── settings.py      # Main settings file
│   ├── urls.py          # URL routing
│   └── wsgi.py          # WSGI configuration
├── common/              # Main Django app
│   ├── models.py        # Database models (Lead, Client, Newsletter)
│   ├── views.py         # API views
│   ├── serializers.py   # DRF serializers
│   ├── admin.py         # Django admin configuration
│   └── authentication.py # Custom authentication
├── manage.py            # Django management script
├── Dockerfile           # Docker image definition
├── docker-compose.yml   # Multi-container orchestration
├── gunicorn.conf.py     # Gunicorn WSGI server config
├── nginx.conf           # Nginx reverse proxy config
├── requirements.txt     # Production dependencies
├── requirements-dev.txt # Development dependencies
├── .env.example         # Environment variables template
└── Claude.md            # Production readiness review
```

## 🔒 Security Configuration

### Before Production Deployment

1. **Generate new SECRET_KEY**
   ```bash
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```

2. **Generate API key**
   ```bash
   python -c 'import secrets; print(secrets.token_urlsafe(48))'
   ```

3. **Update .env file**
   - Set `DEBUG=False`
   - Set strong `DB_PASSWORD`
   - Set strong `REDIS_PASSWORD`
   - Update `ALLOWED_HOSTS`
   - Update `CORS_ALLOWED_ORIGINS`

4. **Review Claude.md**
   See `Claude.md` for comprehensive security audit and recommendations.

## 🧪 Testing

### Run Tests

```bash
# All tests
pytest

# With coverage
pytest --cov

# Specific test file
pytest common/tests/test_models.py

# Verbose output
pytest -v
```

### Code Quality

```bash
# Format code
black .

# Lint code
flake8 .

# Type checking
mypy .

# Security scan
bandit -r .
safety check
```

## 📊 API Endpoints

### Leads Management

```
GET    /backend/api/v1/leads/              # List all leads
POST   /backend/api/v1/leads/              # Create new lead
GET    /backend/api/v1/leads/?status=new   # Filter by status
```

**Authentication**: Requires `Authorization: Bearer <API_KEY>` header

**Example Request**:
```bash
curl -X POST http://localhost:8000/backend/api/v1/leads/ \
  -H "Authorization: Bearer your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "full_name": "John Doe",
    "position": "CTO",
    "company_name": "Tech Corp",
    "email": "john@techcorp.com",
    "phone_number": "+1234567890",
    "source": "website",
    "category": "web_dev"
  }'
```

### Newsletter Subscriptions

```
GET    /backend/api/v1/newsletter/         # List subscribers
POST   /backend/api/v1/newsletter/         # Add subscriber
```

### API Documentation

Visit `/backend/api/docs/` for interactive Swagger documentation.

## 🔧 Environment Variables

See `.env.example` for all available configuration options.

### Critical Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SECRET_KEY` | Django secret key | ✅ Yes |
| `DEBUG` | Debug mode (False in production) | ✅ Yes |
| `DB_PASSWORD` | PostgreSQL password | ✅ Yes |
| `BASIC_API_KEY` | API authentication key | ✅ Yes |
| `ALLOWED_HOSTS` | Comma-separated hostnames | ✅ Yes |

## 📈 Monitoring & Logging

### Application Logs

```bash
# View Django logs
tail -f logs/django.log

# View Gunicorn logs
docker-compose logs -f django

# View Nginx logs
docker-compose logs -f nginx
```

### Health Check

```bash
curl http://localhost:8000/backend/health/
```

Response:
```json
{
  "status": "ok",
  "database": "healthy",
  "python_version": "3.11.x",
  "django_version": [5, 2, 3]
}
```

## 🚢 Production Deployment

### Recommended Architecture

```
Internet
   ↓
Load Balancer (AWS ALB / Cloudflare)
   ↓
Nginx (Reverse Proxy + SSL Termination)
   ↓
Gunicorn (WSGI Server)
   ↓
Django Application
   ↓
PostgreSQL Database
```

### Deployment Checklist

- [ ] Update all passwords and secret keys
- [ ] Set `DEBUG=False`
- [ ] Configure PostgreSQL (not SQLite)
- [ ] Set up SSL certificates
- [ ] Configure backup strategy
- [ ] Set up error monitoring (Sentry)
- [ ] Configure logging
- [ ] Set up database backups
- [ ] Configure rate limiting
- [ ] Review security headers
- [ ] Test health check endpoint
- [ ] Set up CI/CD pipeline

### Database Migrations in Production

```bash
# Run migrations
python manage.py migrate

# Create migration
python manage.py makemigrations

# Show migration SQL
python manage.py sqlmigrate common 0001
```

## 🐛 Troubleshooting

### Common Issues

**Database Connection Error**
```bash
# Check PostgreSQL is running
docker-compose ps

# Check database credentials in .env
cat .env | grep DB_
```

**Static Files Not Loading**
```bash
# Collect static files
python manage.py collectstatic --noinput

# Check STATIC_ROOT setting
python manage.py diffsettings | grep STATIC
```

**Import Error: No module named 'rest_framework'**
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Gunicorn Documentation](https://docs.gunicorn.org/)
- [Docker Documentation](https://docs.docker.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

## 📝 Contributing

1. Create feature branch
2. Make changes
3. Run tests: `pytest`
4. Format code: `black .`
5. Lint code: `flake8 .`
6. Submit pull request

## 📄 License

[Your License Here]

## 👥 Support

For issues and questions:
- Check `Claude.md` for production readiness review
- Review logs: `docker-compose logs -f`
- Contact: dev@exit3.online
