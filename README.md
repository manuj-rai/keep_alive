# keep_alive

A tiny GitHub Actions cron that pings a list of URLs to keep free-tier services awake:

- **Render** free web services sleep after ~15 min of inactivity.
- **Supabase** free projects pause after 7 days of no API traffic.
- **Vercel / Netlify** sites here are pinged because their pages call Supabase server-side, which counts as activity for the database.

## How it works

[.github/workflows/keep_alive.yml](.github/workflows/keep_alive.yml) runs [keep_alive.py](keep_alive.py) on a schedule:

```
*/10 * * * *   # every 10 minutes — stays inside Render's 15-min sleep window
```

The script sends a `GET` to each URL in the `URLS` list, retries once on transient network errors, and exits non-zero if any URL fails so the Actions run goes red.

## Configuration

Edit the `URLS` list in [keep_alive.py](keep_alive.py#L17-L22) to add or remove targets.

## Run locally

```bash
pip install requests
python keep_alive.py
```

## Notes

- At every 10 min this uses ~2,160 GitHub Actions minutes/month. Fine on a **public** repo (unlimited); on a **private** repo it eats most of the 2,000-min free tier — back off to `*/12` or `*/15` if needed.
- GitHub Actions cron can be delayed or skipped during peak load. For guaranteed-on-the-dot pings, use an external service like UptimeRobot or cron-job.org.
