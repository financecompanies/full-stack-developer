# Migrations

## Introduction (Migrations)

### Changing data schema

#### Takeaways
* **Migrations** deal with how we manage modifications to our data schema, over time.
* Mistakes to our database schema are very expensive to make. The entire app can go down, so we want to
    * quickly roll back changes, and
    * test changes before we make them
* A migration is a file that keep track of changes to our database schema (structure of our database).
Offers version control on our schema.

#### Upgrades and rollbacks
* Migrations stack together in order to form the latest version of our database schema
* We can upgrade our database schema by **applying migrations**
* We can **roll back** our database schema to a former version by reverting migrations that we applied

## Migrations - Part 2

### Takeaways

Migrations

* encapsulate a set of changes to our database schema, made over time.
* are uniquely named
* are usually stored as *local files* in our project repo, e.g. a `migrations/` folder
* There should be a 1-1 mapping between the changes made to our database, and the *migration files* that exist in our `migrations/` folder.
* Our migrations files set up the tables for our database.
* All changes made to our db should exist physically as part of migration files in our repository.

### Migration command line scripts
There are generally 3 scripts needed, for

* **migrate**: creating a migration script template to fill out; generating a migration file based on changes to be made
* **upgrade**: applying migrations that hadn't been applied yet ("upgrading" our database)
* **downgrade**: rolling back applied migrations that were problematic ("downgrading" our database)

### Migration library for Flask + SQLAlchemy
* [Flask-Migrate](https://flask-migrate.readthedocs.io/) is our library for migrating changes using SQLAlchemy. It uses a library called [Alembic](https://alembic.sqlalchemy.org/en/latest/index.html) underneath the hood.

#### Flask-Migrate & Flask-Script
* Flask-Migrate (flask_migrate) is our migration manager for migrating SQLALchemy-based database changes
* Flask-Script (flask_script) lets us run migration scripts we defined, from the terminal

#### Steps to get migrations going
1. Initialize the migration repository structure for storing migrations
2. Create a migration script (using Flask-Migrate)
3. (Manually) Run the migration script (using Flask-Script)

### Resources
* [Flask-Migrate docs](https://flask-migrate.readthedocs.io/)

### Why use migrations?

#### Takeaways
Without migrations:
* We do heavy-handed work, creating and recreating the same tables in our database even for minor changes
* We can lose existing data in older tables we dropped

With migrations:
* Auto-detects changes from the old version & new version of the SQLAlchemy models
* Creates a migration script that resolves differences between the old & new versions
* Gives fine-grain control to change existing tables

This is much better, because
* We can keep existing schema structures, only modifying what needs to be modified
* We can keep existing data
* We isolate units of change in migration scripts that we can roll back to a “safe” db state

## Flask_Migrate - Part 2

### Creating the migrations directory structure using `flask db init`

### Syncing models using `flask db migrate`

### To restart your postgres server
In case of an error with existing sessions or connections, you can stop your postgres server to close out existing connections, and then start it up again. Note that stopping a server does not affect the data inside it; they still persist.

To do so:

**On MacOS if you installed postgres using Homebrew,**
```bash
$ brew services start postgresql
$ brew services stop postgresql
```

**Otherwise**
You can call start and stop manually on your postgres server using [pg_ctl](https://www.postgresql.org/docs/10/app-pg-ctl.html), Postgres's application for starting, stopping, and controlling a Postgres server, included with every Postgres install:

To stop it, closing open connections, call

```bash
$ pg_ctl -D /usr/local/var/postgres stop
```

and to start it up again, call

```bash
$ pg_ctl -D /usr/local/var/postgres start
```

## Flask-Migrate - Part 3

`flask db upgrade` and `flask db downgrade`

## Flask-Migrate - Part 4

### Takeaways
**Overall Steps to Set Up & Run Migrations**
1. **Bootstrap database migrate commands**: link to the Flask app models and database, link to command line scripts for running migrations, set up folders to store migrations (as versions of the database)
2. **Run initial migration to create tables for SQLAlchemy models**, recording the initial schema: ala git init && first git commit. Replaces use of db.create_all()
3. **Migrate on changes to our data models**
    * Make changes to the SQLAlchemy models
    * Allow Flask-Migrate to auto-generate a migration script based on the changes
    * Fine-tune the migration scripts
    * Run the migration, aka “upgrade” the database schema by a “version”

**It’s always helpful to read the docs!**
* https://alembic.sqlalchemy.org/en/latest/
* https://flask-migrate.readthedocs.io/en/latest/
