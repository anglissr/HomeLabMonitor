from apscheduler.schedulers.background import BackgroundScheduler
from homelabmonitor import db, create_app
from homelabmonitor.models import User, Device

app = create_app()

def job():
    with app.app_context():
    # Get the user object
        users = User.query.all()
        for user in users:
            devices = Device.query.filter_by(user_id=user.id).all()
            for device in user.devices:
                print(f"Device: {device.name}")

scheduler = BackgroundScheduler()
scheduler.add_job(job, 'interval', seconds=1)

def get_scheduler():
    return scheduler