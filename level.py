from configparser import LegacyInterpolation
from flask import (Blueprint, render_template, request)
from db import get_db
import json

bp = Blueprint('level',__name__, url_prefix='/monitoreo')

@bp.route('/')
def index():
    return render_template('monitorear/index.html')

@bp.route('/tiemporeal')
def tiemporeal(): 
    return render_template('monitorear/realtime.html')
    
@bp.route('/tiemporeal/api')
def apitiemporeal(): 
    db, c = get_db()
    c.execute(
        'SELECT * FROM datalevel ORDER BY id DESC LIMIT 1'
    )
    lastValue = c.fetchone()
    date1 = str(lastValue['dates'])
    data1 = str(lastValue['data'])
    result1 = date1 + '*' + data1
    return result1

@bp.route('/historial/api' , methods=['GET', 'POST'])
def apihistorial(): 
    date1 = request.args.get('date1')
    date2 = request.args.get('date2')
    date1 = date1.split('T')
    date1 = date1[0] + ' ' + date1[1]
    date2 = date2.split('T')
    date2 = date2[0] + ' ' + date2[1]
    datafinal = []
    db, c = get_db()
    c.execute(
        f'select * from datalevel where dates BETWEEN STR_TO_DATE( "{date1}" ,"%Y-%m-%d %H:%i:%s") AND STR_TO_DATE( "{date2}" ,"%Y-%m-%d %H:%i:%s") ORDER BY id ASC'
    )
    datahistorial = c.fetchall()
    for i in range(len(datahistorial)):
        datahistorial[i]['dates'] = str(datahistorial[i]['dates']);
        datahistorial[i]['data'] = str(datahistorial[i]['data']);
        datafinal.append([datahistorial[i]['dates'],datahistorial[i]['data']]);
    datafinal = json.dumps(datafinal)
    return datafinal

@bp.route('/historial', methods=['GET', 'POST'])
def historial():
    if request.method == 'POST':
        initialdate = request.form['dstart']
        finaldate = request.form['dend']
        error = None
        if initialdate == '':
            error = 'Se requiere una fecha inicial para realizar la consulta'
            errorType = 'error'
            return render_template('monitorear/record.html', error = error, errorType=errorType)

        if finaldate == '':
            error = 'Se requiere una fecha final para realizar la consulta'
            errorType = 'error'
            return render_template('monitorear/record.html', error = error, errorType=errorType)

        if error is None:
            date1 = initialdate
            date2 = finaldate
            
            return render_template('monitorear/record.html', date1 = date1, date2=date2)
    return render_template('monitorear/record.html', date1 = '', date2='')