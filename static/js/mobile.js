let orientation = screen.orientation;
if(screen.width < 768 && (orientation != "90" || orientation != "-90" )){
    var myModal = new bootstrap.Modal(document.getElementById('exampleModal'), {
        keyboard: false
    })
    myModal.show()
}
window.onorientationchange = function() { 
    let orientation = window.orientation; 
        switch(orientation) { 
            case 0:
            case 90:window.location.reload(); 
            case -90: window.location.reload(); 
            break; } 
};