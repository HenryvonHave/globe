import './home.scss';

document.addEventListener('DOMContentLoaded', function() {
    // Initialize the map when the DOM is fully loaded
    initMap();
});

function initMap() {
    console.log('Initializing map...', mapboxgl);
    mapboxgl.accessToken = 'pk.eyJ1IjoibWF4dHRpIiwiYSI6ImNrb2RwaGtmYzAzdTgydnMzYnp4dHp4anMifQ.NPlEkpfAU_YxWMqN1jY78A';
    const map = new mapboxgl.Map({
        container: 'map', // container ID
        style: 'mapbox://styles/maxtti/cm6uhmcht00fv01sah6toaw5n', // style URL
        center: [-74.5, 40], // starting position [lng, lat]. Note that lat must be set between -90 and 90
        zoom: 1 // starting zoom
    });
}