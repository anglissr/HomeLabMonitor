from homelabmonitor import create_app
from scheduler import get_scheduler

app = create_app()

if __name__ == "__main__":
    scheduler = get_scheduler()
    if scheduler and not scheduler.running:
        scheduler.start()
    #app.run(debug=True)
    app.run(debug=False, use_reloader=False)