This is a simple server for hosting media files, using S3 as
a back-end.

## Motivation

YouTube and other movie distribution channels have a number
of problems with them:

* They might force users to watch ads before your video.
* They don't make it easy for users to download the video
  and watch it offline.
* They don't make the raw HTML5 video URL of the uploaded
  video easily visible for others to embed.
* They might constrain the video to a specific aspect
  ratio, truncate its last few seconds, or perform
  any number of other transformations that the author may
  dislike.
* There's no easy way to visually embed them in sanitized HTML
  environments that don't support iframes or the video
  tag, such as GitHub issues or HTML emails.

This server attempts to resolve these issues. Here's an example
of a video embedded in this readme, hosted by the server:

<a href="https://toolness-media.herokuapp.com/v/redis/play"><img src="https://toolness-media.herokuapp.com/v/redis.poster.play.jpg" alt="Play 'Redis' video"></a>

The above is accomplished by creating a "fake" player widget that is
simply the poster frame of the HTML5 video with a picture of a
play button superimposed on it. This image is then linked to
a video detail page on the server.

## Requirements

* Python 2.7
* [pip and virtualenv](http://stackoverflow.com/q/4324558)

## Quick Start

```
virtualenv venv

# On Windows, replace the following line with 'venv\Scripts\activate'.
source venv/bin/activate

pip install -r requirements.minimal.txt
python manage.py syncdb
python manage.py runserver
```

## Environment Variables

Unlike traditional Django settings, we use environment variables
for configuration to be compliant with [twelve-factor][] apps.

**Note:** When an environment variable is described as representing a
boolean value, if the variable exists with *any* value (even the empty
string), the boolean is true; otherwise, it's false.

**Note:** When running `manage.py`, the following environment
variables are given default values: `SECRET_KEY`, `PORT`.
Also, `DEBUG` is enabled.

* `SECRET_KEY` is a large random value.
* `DEBUG` is a boolean value that indicates whether debugging is enabled
  (this should always be false in production).
* `PORT` is the port that the server binds to.
* `DATABASE_URL` is the URL for the database. Defaults to a `sqlite://`
  URL pointing to `db.sqlite3` at the root of the repository. If this
  value is the name of another (all-caps) environment variable, e.g.
  `HEROKU_POSTGRESQL_AMBER_URL`, that variable's value will be used
  as the database URL.
* `ALLOWED_HOSTS` is a comma-separated list of host/domain names
  the site can serve. This list should not include any spaces.
* `SECURE_PROXY_SSL_HEADER` is an optional HTTP request header field name
  and value indicating that the request is actually secure. For example,
  Heroku deployments should set this to `X-Forwarded-Proto: https`.
* `STORAGE_BACKEND_URL` contains information about the backend
  to use for storing uploads. Currently, the only available option is
  Amazon S3, specified by a URL of the form
  `s3://access-key:secret@bucket-name`.

<!-- Links -->

  [twelve-factor]: http://12factor.net/
