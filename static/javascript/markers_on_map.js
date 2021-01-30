var map;
var markers = []
var totalMarkers = -1
var timeChanged = 0
var reloadMap = false

//ricevo le coordinate dalla mia api
async function getCoordinates() {
  if (window.location.href.includes("127.0.0.1")){
      var url = 'http://127.0.0.1:8000/api/coord/list/?token=g6dkzUBMeO6bfLP'
  }
  else {
      var url = 'http://168.119.157.156/api/coord/list/?token=g6dkzUBMeO6bfLP'
  }

  let response = await fetch(url, {
    method: "GET",
    headers: {"Content-type": "application/json;charset=UTF-8"}
  })
  let json = await response.json()
  console.log(json);
  return json
}

// inizializzo la mappa su Udine
async function initMap() {
  console.log("init map")
  map = new google.maps.Map(document.getElementById('map'), {
    center: {
      lat: 46.064941,
      lng: 13.230720
    },
    zoom: 12
  });

  let coordsToPrint = await getCoordinates()
    .then(data => data)

  insertMarkers(coordsToPrint)

  repeat()
};

function returnUnixtime(date) {
  var parts = date.split("T")
  var date = parts[0]
  var time = parts[1]
  parts = date.split("/")
  var newDate = parts[1] + "/" + parts[0] + "/" + parts[2] + " " + time
  return new Date(newDate).getTime() / 1000
}


// inserisce i markers e posiziona la mappa al centro
function insertMarkers(coords) {

  let latlngbounds = new google.maps.LatLngBounds();
  coords.forEach(function(item) {
    addOneMarker(item)
    latlngbounds.extend(new google.maps.LatLng(item.lat, item.lng));
  })
  map.fitBounds(latlngbounds);
  map.setCenter(latlngbounds.getCenter());

}

// richiama getCoordinates, in base alle modifiche delle coordinate aggiorna la pagina
// oppure cancella e riposiziona i markers
async function repeat(){

  let coordsToPrint = await getCoordinates()
    .then(data => data)

  if (coordsToPrint.length != totalMarkers && totalMarkers>-1) {
    location.reload()
  }
  totalMarkers = coordsToPrint.length
  reloadMap = false

  coordsToPrint.forEach(function(item) {
    let unixtime = returnUnixtime(item.last_update)

    if(unixtime > timeChanged){
      timeChanged = unixtime
      reloadMap = true
    }
  })

  if(reloadMap)
  {
    for (i in markers) {
      markers[i].setMap(null);
    }
    markers = [];
    insertMarkers(coordsToPrint)
  }

  t = setTimeout( function () {
    repeat();
  },5000)
}

// funzione che aggiunge un marker e aggiunge infowindow
function addOneMarker(position) {

  let marker = new google.maps.Marker({
    position: new google.maps.LatLng(position.lat, position.lng),
    map: map,
  });

  let contentString =
    "<b>label: </b>" + position.object_label +
    "<br><b>lat: </b>" + position.lat +
    "<br><b>lng: </b>" + position.lng;

  let infowindow = new google.maps.InfoWindow({
    content: contentString,
  });

  marker.addListener("click", () => {
    infowindow.open(map, marker);
  });

  markers.push(marker)
}
