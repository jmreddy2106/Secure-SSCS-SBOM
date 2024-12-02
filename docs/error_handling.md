# Error Handling

The script handles various error scenarios:

## 1. Rate Limits
- **Cause**: Exceeding GitHub's API rate limits.
- **Solution**: The script waits until the rate limit resets before retrying.

## 2. API Errors
- **Cause**: Invalid API requests (e.g., 404, 403).
- **Solution**: Logs the error and continues with other repositories.

## 3. Database Errors
- **Cause**: Issues with PostgreSQL connection or table.
- **Solution**: Logs the error message. Ensure the `DB_CONNECTION` is valid.

---
<!-- [Previous: Database Schema](database_schema.md) | [Next: Contributing](contributing.md) -->