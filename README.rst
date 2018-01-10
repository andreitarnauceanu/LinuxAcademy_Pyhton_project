pgbackup
========

CLI for backing up remote PostgreSql database locally or to AWS s3

Preparing for Development
-------------------------

1. Ensure ''pip'' and ''pipenv'' are installed.
2. Clone repository: ''git clone git@githum.com:example/pgbachup''
3. Fetch development dependencies: ''make install''


Usage:
------

Pass in a full database URL, the storage drive, and destination

S3 Example w/ backet name:

::

    $ pgbackup posgres://bob@example.com:5432/db_one --driver s3 backup

Local example w/ local path

::

    $ pgbackup posgres://bob@example.com:5432/db_one --driver local /var/local/db_one/backups/dump.sql


Running Tests
-------------

Run tests localy using ''make'' if virtualenv is active:

::
    $ make


If virtulaenv isn't active then use:

::
    $ pipenv run make
