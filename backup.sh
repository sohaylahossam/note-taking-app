#!/bin/bash
TIMESTAMP=$(date +"%F_%T")
BACKUP_FILE="/backup/notes_db_$TIMESTAMP.sql"
mysqldump -u root -pYourPassword notes_db > "$BACKUP_FILE"