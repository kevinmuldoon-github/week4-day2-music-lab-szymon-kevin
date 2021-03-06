from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def save(artist):

    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]

    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def select(id):
    artist = None

    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]

    if result is not None:
        artist = Artist(result['name'])
    return artist

def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['name'] , row['id'])
        artists.append(artist)
    return artists

def edit_artist(artist, updated_artist):
    sql = "UPDATE artists SET name = (%s) WHERE id = %s"
    values = [updated_artist.name, artist.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql,values)

