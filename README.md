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

## Docker Compose example

```
gphotos-syncer:
    image: muyajil/gphotos-syncer:latest
    restart: unless-stopped
    user: 1000:1000
    volumes:
      - ${CONFIG_PATH}:/config
      - ${PHOTOS_PATH}:/download
    environment:
      SLACK_WEBHOOK: ${SLACK_WEBHOOK}
      CLIENT_SECRET: ${CLIENT_SECRET}
```