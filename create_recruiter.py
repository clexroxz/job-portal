from app import app, db, Users
from werkzeug.security import generate_password_hash

with app.app_context():
    # Check if recruiter user already exists
    existing_user = Users.query.filter_by(email="recruiter@test.com").first()
    
    if not existing_user:
        # Create new recruiter user
        recruiter_user = Users(
            username="TestRecruiter",
            email="recruiter@test.com",
            gender="other",
            dob="1990-01-01",
            role="recruiter",
            password=generate_password_hash("test123")
        )
        db.session.add(recruiter_user)
        db.session.commit()
        print("Recruiter user created successfully!")
        print("Email: recruiter@test.com")
        print("Password: test123")
    else:
        print("Recruiter user already exists!")
        print("Email: recruiter@test.com")
        print("Password: test123") 