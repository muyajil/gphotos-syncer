# gphotos-syncer

This is a container wrapping `gilesknap/gphotos-sync` and running a poor man's cron job to continuously download all photos and videos from Google Photos.

Also if something goes wrong there is the possibility to be notified via Slack Webhook.

The first run should be done attached to the container, because on the first run you will be provided with a link to authenticate your Google Account with the application. After that you can kill the container and start it in normal mode.
## Usage

The container is configured using environment variables:

- `CLIENT_SECRET`: OAuth Client Secret setup when initially setting up gphotos-sync. Guide on how to create one: https://docs.google.com/document/d/1ck1679H8ifmZ_4eVbDeD_-jezIcZ-j6MlaNaeQiz7y0/edit
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
      - /path/to/config/dir:/config
      - /path/to/photos/dir:/download
    environment:
      SLACK_WEBHOOK: https://some.slack.webhook
      CLIENT_SECRET: <Client Secret>
```