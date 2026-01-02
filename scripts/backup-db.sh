#!/bin/bash

# Exit Three - SQLite Database Backup Script

set -e

BACKUP_DIR="$(dirname "$0")/../backend/backups"
DATE=$(date +%Y%m%d_%H%M%S)
KEEP_DAYS=7

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Change to project root
cd "$(dirname "$0")/.."

echo "📦 Starting SQLite database backup..."

# Backup database (copy SQLite file from Docker volume or local file)
if [ -f "./backend/db.sqlite3" ]; then
    # Local development
    cp "./backend/db.sqlite3" "$BACKUP_DIR/backup_$DATE.sqlite3"
else
    # Docker environment - copy from container
    docker-compose exec -T backend cp /app/db.sqlite3 /app/backups/backup_$DATE.sqlite3 2>/dev/null || \
    docker cp exit3_backend:/app/db.sqlite3 "$BACKUP_DIR/backup_$DATE.sqlite3"
fi

if [ $? -eq 0 ]; then
    echo "✓ Backup created: backup_$DATE.sqlite3"

    # Get backup size
    SIZE=$(du -h "$BACKUP_DIR/backup_$DATE.sqlite3" | cut -f1)
    echo "  Size: $SIZE"

    # Delete old backups
    find "$BACKUP_DIR" -name "backup_*.sqlite3" -mtime +$KEEP_DAYS -delete
    echo "✓ Cleaned up backups older than $KEEP_DAYS days"

    # List remaining backups
    echo ""
    echo "Available backups:"
    ls -lh "$BACKUP_DIR"/backup_*.sqlite3 2>/dev/null | awk '{print "  " $9 " (" $5 ")"}' || echo "  No backups found"
else
    echo "✗ Backup failed!"
    exit 1
fi

echo ""
echo "✓ Backup complete!"
