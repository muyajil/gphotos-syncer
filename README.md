# gphotos-syncer

This is a container wrapping `gilesknap/gphotos-sync` and running a poor man's cron job to continuously download all photos and videos from Google Photos.

Also if something goes wrong there is the possibility to be notified via Slack Webhook.

## Usage

The container is configured using environment variables:

- `CLIENT_SECRET`: OAuth Client Secret setup when initially setting up gphotos-sync
- `SLACK_WEBHOOK`: Slack Webhook for notifications

The following volumes should be mounted:

- `/download`: The photos and videos will be downloaded here
- `/config`: Here the database and configs will be stored