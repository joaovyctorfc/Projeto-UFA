let h2 = document.querySelector('h2');

function success(pos) {
    console.log(pos.coords.latitude, pos.coords.longitude);
    h2.textContent = '\n Latitude: ' + pos.coords.latitude + ' Longitude: ' + pos.coords.longitude +"\n";
}

function error(err) {
    console.log(err);
}

// Chama a função para rastrear a posição em tempo real
let watchId = navigator.geolocation.watchPosition(success, error);
