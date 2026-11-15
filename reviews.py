import db

def add_review(title, description, verdict, user_id):
    sql = """INSERT INTO reviews (title, description, verdict, user_id)
             VALUES (?, ?, ?, ?)"""
    db.execute(sql, [title, description, verdict, user_id])