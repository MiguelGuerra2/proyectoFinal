let date1 = document.getElementById('date1').value;
let date2 = document.getElementById('date2').value;
if (date1 != '' && date2 != ''){
    const URLActual = window.location;
    const term = `/api?date1=${date1}&date2=${date2}`
    const link = URLActual + term;
    async function hist() {
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
            var infos = await response.json(); 
            for (let i = 0; i < infos.length; i++) {
                dates.push(infos[i][0]);
                datas.push(infos[i][1]);
            }
        }
    };
    hist()
}



