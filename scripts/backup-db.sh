#!/bin/bash

# Exit Three - Database Backup Script

set -e

BACKUP_DIR="$(dirname "$0")/../backend/backups"
DATE=$(date +%Y%m%d_%H%M%S)
KEEP_DAYS=7

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Change to project root
cd "$(dirname "$0")/.."

echo "📦 Starting database backup..."

# Backup database
docker-compose exec -T db pg_dump -U postgres exit3_db | gzip > "$BACKUP_DIR/backup_$DATE.sql.gz"

if [ $? -eq 0 ]; then
    echo "✓ Backup created: backup_$DATE.sql.gz"

    # Get backup size
    SIZE=$(du -h "$BACKUP_DIR/backup_$DATE.sql.gz" | cut -f1)
    echo "  Size: $SIZE"

    # Delete old backups
    find "$BACKUP_DIR" -name "backup_*.sql.gz" -mtime +$KEEP_DAYS -delete
    echo "✓ Cleaned up backups older than $KEEP_DAYS days"

    # List remaining backups
    echo ""
    echo "Available backups:"
    ls -lh "$BACKUP_DIR"/backup_*.sql.gz | awk '{print "  " $9 " (" $5 ")"}'
else
    echo "✗ Backup failed!"
    exit 1
fi

echo ""
echo "✓ Backup complete!"
