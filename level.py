from configparser import LegacyInterpolation
from flask import (Blueprint, render_template, request)
from db import get_db
import json
import datetime

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
            date1 = initialdate.split('T')
            date1f = str(str(date1[0]) + ' ' + str(date1[1]))
            date2 = finaldate.split('T')
            date2f = str(str(date2[0]) + ' ' + str(date2[1]))
            db, c = get_db()
            c.execute(
                f'select * from datalevel where date BETWEEN STR_TO_DATE( "{date1f}" ,"%Y-%m-%d %H:%i:%s") AND STR_TO_DATE( "{date2f}" ,"%Y-%m-%d %H:%i:%s")'
            )
            if c.fetchone() is None:
                error = 'No existen datos en el rango de fechas ingresado'
                errorType = 'warning'
                return render_template('monitorear/record.html', error = error, errorType=errorType)
            results1 = c.fetchall()
            def datetime_handler(x):
                if isinstance(x, datetime.datetime):
                    return x.isoformat()
                raise TypeError("Unknown type")
            var2 = json.dumps(results1, default=datetime_handler)
            return render_template('monitorear/record.html', results1 = var2)
    return render_template('monitorear/record.html')