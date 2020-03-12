pip3 install flask_sqlalchemy
pip3 install flask_cors
pip3 install flask --upgrade
pip3 uninstall flask-socketio

# Execute the commands below in a terminal
#
# docker cp /backend/setup.sql peticionamais-db:/
# docker cp /backend/books.psql peticionamais-db:/
# docker exec -it peticionamais-db bash
# $ psql -U postgres < setup.sql
# $ psql -U postgres < books.psql