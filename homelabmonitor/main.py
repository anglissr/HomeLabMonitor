from . import db
from .models import User, Device, Service   
from flask import Blueprint, render_template, redirect, url_for, request, flash, abort, g
from flask_login import current_user, login_required, login_manager

main = Blueprint('main', __name__)


@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    else:
        return redirect(url_for('auth.login'))


@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    user_name = current_user.username
    devices = Device.query.filter_by(user_id=current_user.id).all()
    #user = User.query.filter_by(username='admin').first()
    #devices = user.devices
    #print(devices[0].name)  
    if request.method == 'POST':
        form_id = (request.form.get('form_id', ''))
        if form_id == "rename_form":
            # get the data from the form
            device_id = request.form.get('device_id')
            name = request.form.get('name')
            device = Device.query.get(device_id)
            if not device or device.user != current_user:
                abort(404)
            device.name = name
            flash('Success: Device renamed')
        if form_id == "toggle_form":
            # get the data from the form
            device_id = request.form.get('device_id')
            device = Device.query.get(device_id)
            if not device or device.user != current_user:
                abort(404)
            name = device.name 
            status = not(device.running)
            if status:
                flash('Started ' + name)
            else:
                flash('Stopped ' + name)
            device.running = status
            
        
        # save the changes to the database
        db.session.commit()
        

    return render_template('index.html', user_name=user_name, devices=devices)

@main.route('/settings')
@login_required
def settings():
    user_name = current_user.username
    return render_template('settings.html', user_name=user_name)

@main.route('/devices/<int:device_id>/settings', methods=['GET', 'POST'])
@login_required
def device_settings(device_id):
    device = Device.query.get(device_id)
    if not device or device.user != current_user:
        abort(404)
    user_name = current_user.username
    services = Service.query.all()
    if request.method == 'POST':
        # get the data from the form
        name = request.form.get('name')
        ip_address = request.form.get('ip_address')
        service_objs = []
        for i in range(1, 5):
            service_id = request.form.get(f'line_{i}')
            if service_id:
                service_obj = Service.query.filter_by(id=service_id).first()
                service_objs.append(service_obj)
        for service in service_objs:
            print(service.id)
        device.name = name
        device.ip = ip_address
        device.service1_id = service_objs[0].id
        device.service2_id = service_objs[1].id
        device.service3_id = service_objs[2].id
        device.service4_id = service_objs[3].id
        # save the changes to the database
        db.session.commit()
        flash('Success: Device settings saved.')

    return render_template('device_settings.html', user_name=user_name, device=device, services=services)


