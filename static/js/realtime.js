let fdata = document.getElementById('fdata');
let fdate = document.getElementById('fdate');
let colorAlarm = document.getElementById('colorAlarm');
let descriptionAlarm = document.getElementById('descriptionAlarm');
const URLActual = window.location;
const link = URLActual + '/api';
async function level() {
    //Fetch para obtener el ultimo dato de la base de datos
    var response = await fetch(link,{
        mode: "cors",
        headers: {
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
        }
    });
    if (response.status == 200) {
        let datas = await response.text(); 
        datas = datas.split('*');
        let data = datas[1];
        let date = datas[0];  
        fdata.innerHTML=data + ' metros';
        fdate.innerHTML=date;
        if (data < 2){
            colorAlarm.style.backgroundColor='blue';
            descriptionAlarm.innerHTML='Actualmente el brazo fluvial presenta un bajo nivel respecto a su nivel promedio.';
        }
        if (2 < data && data < 5){
            colorAlarm.style.backgroundColor='green';
            descriptionAlarm.innerHTML='Descripcion de nivel medio';
        }
        if (data > 5){
            colorAlarm.style.backgroundColor='red';
            descriptionAlarm.innerHTML='Descripcion de nivel alto';
        }
    }    
}setInterval("level()", 5000);
level()