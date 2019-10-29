# Postgres

## Installing Postgres within Ubuntu

### Installing Postgres 10

```bash
sudo apt update
```

```bash
sudo apt install postgresql postgresql-contrib
```

```bash
dpkg -l | grep postgresql
```

```bash
pg_lsclusters
```

```bash
reboot
```

Reference
* [How To Install and Use PostgreSQL on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)

### Installing Postgres 11

```bash
sudo apt update && sudo apt-y upgrade
```

```bash
sudo apt install -y wget vim
```

```bash
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```

```bash
RELEASE=$(lsb_release -cs)
echo "deb http://apt.postgresql.org/pub/repos/apt/ ${RELEASE}"-pgdg main | sudo tee  /etc/apt/sources.list.d/pgdg.list
```

```bash
cat /etc/apt/sources.list.d/pgdg.list
```

```bash
sudo apt update
sudo apt -y install postgresql-11
```

Reference
* [Install PostgreSQL 11 on Ubuntu 18.04 / Ubuntu 16.04](https://computingforgeeks.com/install-postgresql-11-on-ubuntu-18-04-ubuntu-16-04/)

### Upgrading Postgres 11

```bash
sudo apt -y install postgresql-contrib
```

```bash
dpkg -l | grep postgresql
```

```bash
pg_lsclusters
```

```bash
sudo pg_dropcluster 11 main --stop
```

```bash
sudo pg_upgradecluster 10 main
```

```bash
sudo pg_dropcluster 10 main
```

```bash
sudo apt purge postgresql-10 postgresql-client-10
```

Reference
* [Upgrading PostgreSQL from 9.6 to 10.0 on Ubuntu 18.04](https://www.paulox.net/2018/05/19/upgrading-postgresql-from-9-6-to-10-0-on-ubuntu-18-04/#upgrading-postgresql-from-9-6-to-10-0-on-ubuntu-18-04)

## General commands

### Log in as a particular user

Default installed user is called postgres

```bash
sudo -u <username> -i
```

e.g. sudo -u bob -i

### Create a new database

```bash
createdb <database_name>
```

e.g. createdb mydb

### Destroy a database

```bash
dropdb <database_name>
```

e.g. dropdb mydb

### Reset a database

```bash
dropdb <database_name> && createdb <database_name>
```

e.g. dropdb mydb && createdb mydb

## psql commands

```bash
# \l
```

List all databases on the server, their owners, and user access levels

```bash
# \c <dbname>
```

Connect to a database named

```bash
# \dt
```

Show database tables

```bash
# \d <tablename>
```

Describe table schema

```bash
# \q
```

## Installing psycopg2

* Make sure you have Python 3 version between 3.4 to 3.7. You can find out with

```bash
python --version
```

* Use the latest pip version:  `pip3 install -U pip`

* Replace X.Y in the export PATH... line with the version of Postgres you are using. Find out with $ postgres -V. E.g.:

```bash
$ postgres -V
postgres (PostgreSQL) 10.2
```

Another way is using the psql client:

```bash
psql --version
```

There's another option using a query to postgres database:

```bash
sudo -u postgres psql postgres -c 'select version();' | grep -i postgres
```

* In ~/.bash_profile or ~/.bashrc, we should add:

```bash
export PATH=/usr/lib/postgresql/10.2/bin/:$PATH
```

* Reload the shell session with lastest profile changes

```bash
source ~./bash_profile or source ~/.bashrc
```

* Install psycopg2

```bash
pip install pyscopg2
```

* A prerequisite for psycopg2 is OpenSSL. If you try installing and run into error ld: library not found for -lssl, then install openssl first.

    * `sudo apt install openssl`
    * Add the LIBRARY_PATH to your bash profile:
        ```bash
          export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/opt/openssl/lib/
        ```

* If the regular install doesn't work, you can also just install the binary version instead:

```bash
pip install psycopg2-binary
```

* Install troubleshooting threads:
    * For error Failed building wheel for psycopg2: https://stackoverflow.com/questions/34304833/failed-building-wheel-for-psycopg2-macosx-using-virtualenv-and-pip
    * For error pg_config executable not found: https://stackoverflow.com/questions/11618898/pg-config-executable-not-found

## Learnt lesson: Create specific postgres user

To run Postgres commands in order to create tables (DDL) and also to insert rows (DML) we need to create a specific user and provide that user into connection string to `psycopg2.connect()` method.

Connect as postgres user:

```bash
sudo -u postgres -i
```

Or connect direct to psql using postgres user:

```bash
sudo -u postgres psql
```

Create the database:

```bash
createdb android
```

Create the user using interactive mode:

```bash
sudo -u postgres createuser --interactive
```

Or with a more flexible way:

```bash
create user androiduser with encrypted password 'androidpwd';
```

Grant permissions to the new created user:

```bash
grant all privileges on database mydb to myuser;
```

## Learnt lesson: Configure virtualenv with Pyenv-virtualenv

Easily install pyenv:

```bash
curl https://pyenv.run | bash
```

Add these lines at the bottoom of `~/.bashrc` or `~/.bash_profile`

```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

First install the desired python version:

```bash
pyenv install --list
pyenv install -v 3.7.4
```

Check current versions installed:

```bash
pyenv versions
```

Create the virtualenv and activate it to setup it up:

```bash
pyenv virtualenv 3.7.4 fyyur
pyenv activate fyyur
```

Install the requirements:

```bash
pip install -r requirements.txt
```

### References
* [Utilizando Pyenv e Pyenv-virtualenv e aposentando o virtualenv “ou não”](http://www.mateuspaduaweb.com.br/utilizando-pyenv-e-pyenv-virtualenv-e-aposentando-o-virtualenv-ou-nao/)
* [Gerenciamento de Ambientes Python com pyenv
](https://medium.com/operacionalti/gerenciamento-de-ambientes-python-com-pyenv-3ce71eb1a2c3)