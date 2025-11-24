import sqlite3
except Exception as e:
conn.close()
raise
conn.close()
return user_id


def find_user_by_username(username):
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()
c.execute('SELECT id, username, email, password_hash FROM users WHERE username = ?', (username,))
row = c.fetchone()
conn.close()
return row


def verify_user(username, password):
row = find_user_by_username(username)
if not row:
return None
user_id, username, email, pw_hash = row
if check_password_hash(pw_hash, password):
return {'id': user_id, 'username': username, 'email': email}
return None


# File helpers


def save_file_record(user_id, filename, original_filename):
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()
c.execute('INSERT INTO files (user_id, filename, original_filename) VALUES (?, ?, ?)',
(user_id, filename, original_filename))
conn.commit()
conn.close()


def list_files_for_user(user_id):
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()
c.execute('SELECT id, filename, original_filename, uploaded_at FROM files WHERE user_id = ? ORDER BY uploaded_at DESC', (user_id,))
rows = c.fetchall()
conn.close()
return rows


# Notes helpers (simple)


def add_note(user_id, title, content):
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()
c.execute('INSERT INTO notes (user_id, title, content) VALUES (?, ?, ?)', (user_id, title, content))
conn.commit()
conn.close()


def list_notes(user_id):
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()
c.execute('SELECT id, title, content, created_at FROM notes WHERE user_id = ? ORDER BY created_at DESC', (user_id,))
rows = c.fetchall()
conn.close()
return rows
