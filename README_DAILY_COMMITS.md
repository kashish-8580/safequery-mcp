Daily commits helper
====================

Overview
--------
This repository includes `scripts/generate_daily_commit.sh` to create small, plausible daily commits.

Quick run
---------
Make the script executable and run it with your name and email:

```bash
chmod +x scripts/generate_daily_commit.sh
./scripts/generate_daily_commit.sh --name "Your Full Name" --email "you@example.com"
```

To create and push in one step (only do this if your local environment has push credentials configured):

```bash
./scripts/generate_daily_commit.sh --name "Your Full Name" --email "you@example.com" --push
```

Sample `crontab` entry (run daily at 09:00):

```cron
0 9 * * * cd /Users/kashishsingh/safequery-mcp && /bin/bash scripts/generate_daily_commit.sh --name "Your Full Name" --email "you@example.com" --push
```

Notes
-----
- The script commits files under `daily_updates/`. Review generated files before allowing automatic pushes.
- If you want backdated commits (simulate past activity), confirm explicitly — the script does not set custom timestamps by default.
