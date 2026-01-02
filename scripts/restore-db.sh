#!/bin/bash

# Exit Three - SQLite Database Restore Script

set -e

BACKUP_DIR="$(dirname "$0")/../backend/backups"

# Change to project root
cd "$(dirname "$0")/.."

# Check if backup file is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <backup_file.sqlite3>"
    echo ""
    echo "Available backups:"
    ls -lh "$BACKUP_DIR"/backup_*.sqlite3 2>/dev/null || echo "  No backups found"
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

echo "🔄 Restoring SQLite database from backup..."

# Restore database
if [ -f "./backend/db.sqlite3" ]; then
    # Local development
    cp "$BACKUP_FILE" "./backend/db.sqlite3"
else
    # Docker environment - copy to container
    docker cp "$BACKUP_FILE" exit3_backend:/app/db.sqlite3
fi

if [ $? -eq 0 ]; then
    echo "✓ Database restored successfully!"
    echo ""
    echo "⚠️  You may need to run migrations:"
    echo "  docker-compose exec backend python manage.py migrate"
else
    echo "✗ Restore failed!"
    exit 1
fi
