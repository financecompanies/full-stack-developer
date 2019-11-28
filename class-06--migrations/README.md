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