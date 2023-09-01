let h2 = document.querySelector('h2');
var map;

function success(pos){
console.log(pos);
h2.textContent = `latidude:${pos.coords.latitude}, longitude:${pos.coords.longitude}`

if (map == undefined){
    map = L.map('map').setView([pos.coords.latitude, pos.coords.longitude], 13);
}
else{
    map.remove();
    map = L.map('map').setView([pos.coords.latitude, pos.coords.longitude], 13);
}

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.marker([pos.coords.latitude, pos.coords.longitude]).addTo(map)
    .bindPopup('Sua localização  está aqui')
    .openPopup();uta 
}

function error(error){
    console.log(error);
}

var watchID = navigator.geolocation.getCurrentPosition(success, error, {
    enableHighAccuracy: true,
    timeout: 5000
});
