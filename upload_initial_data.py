from main import app
from application.models import db, Role

with app.app_context():
    db.create_all()
    admin = Role(id = 'admin', name = 'Admin', decription = 'Admin description')
    db.session.add(admin)
    stud = Role(id = 'stud', name = 'Student', decription = 'Student description')
    db.session.add(stud)
    inst = Role(id = 'inst', name = 'Instructor', decription = 'Instructor description')
    db.session.add(inst)
    db.session.commit()
