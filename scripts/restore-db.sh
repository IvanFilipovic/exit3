#!/bin/bash

# Exit Three - Database Restore Script

set -e

BACKUP_DIR="$(dirname "$0")/../backend/backups"

# Change to project root
cd "$(dirname "$0")/.."

# Check if backup file is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <backup_file.sql.gz>"
    echo ""
    echo "Available backups:"
    ls -lh "$BACKUP_DIR"/backup_*.sql.gz 2>/dev/null || echo "  No backups found"
    exit 1
fi

BACKUP_FILE="$1"

# Check if file exists
if [ ! -f "$BACKUP_FILE" ]; then
    # Try in backup directory
    if [ -f "$BACKUP_DIR/$BACKUP_FILE" ]; then
        BACKUP_FILE="$BACKUP_DIR/$BACKUP_FILE"
    else
        echo "✗ Backup file not found: $BACKUP_FILE"
        exit 1
    fi
fi

echo "⚠️  WARNING: This will REPLACE the current database!"
echo "Backup file: $BACKUP_FILE"
read -p "Are you sure? (type 'yes' to continue): " CONFIRM

if [ "$CONFIRM" != "yes" ]; then
    echo "Restore cancelled."
    exit 0
fi

echo "🔄 Restoring database from backup..."

# Drop and recreate database
docker-compose exec -T db psql -U postgres -c "DROP DATABASE IF EXISTS exit3_db;"
docker-compose exec -T db psql -U postgres -c "CREATE DATABASE exit3_db;"

# Restore from backup
gunzip -c "$BACKUP_FILE" | docker-compose exec -T db psql -U postgres -d exit3_db

if [ $? -eq 0 ]; then
    echo "✓ Database restored successfully!"
    echo ""
    echo "⚠️  You may need to run migrations:"
    echo "  docker-compose exec backend python manage.py migrate"
else
    echo "✗ Restore failed!"
    exit 1
fi
