let resultInput = document.getElementById('vars').value;
if (resultInput) {
    resultInput = JSON.parse(resultInput);
    var datas = [];
    var dates = [];
    for (var i = 0; i < resultInput.length; i++) {
        datas[i] = resultInput[i]['data'];
        dates[i] = resultInput[i]['date'];
    }
    for (i = 0; i < dates.length; i++) {
        dates[i] = dates[i].split("T").join(" "); 
    }
}


