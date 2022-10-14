console.log("Hello");
let map;

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 8,
        center: { lat: 54.65, lng: -6.7 },
    });

    map.data.loadGeoJson(
        '/static/map_api_requirements/OSNI_Constituencies.geojson'
    );

    map.data.setStyle({
        fillColor: "blue"
    });

    map.data.addListener('click', function (event) {
        location.href = "results/" + event.feature.getProperty("Constituency_Directory");
    });

    map.data.addListener('mouseover', function (event) {
        map.data.revertStyle();
        map.data.overrideStyle(event.feature, { strokeWeight: 5 });
        document.getElementById('info-box').textContent =
            event.feature.getProperty('Constituency_Directory');
    });

}




window.initMap = initMap;