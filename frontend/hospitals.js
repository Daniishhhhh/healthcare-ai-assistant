// ================= GLOBAL VARIABLES =================
let hospitalsData = [];

let userLat = null;
let userLng = null;


// ================= LOAD DATA =================
async function loadHospitals() {

    const res = await fetch("data/hospitals.json");
    hospitalsData = await res.json();

}

loadHospitals();


// ================= DETECT LOCATION =================
function getUserLocation() {

    if (!navigator.geolocation) {
        alert("Geolocation not supported.");
        return;
    }

    navigator.geolocation.getCurrentPosition(showNearestHospitals, errorHandler);

}


// ================= DISTANCE CALCULATION =================
function getDistance(lat1, lon1, lat2, lon2) {

    if (!lat2 || !lon2) return 9999;

    const R = 6371;

    const dLat = (lat2 - lat1) * Math.PI / 180;
    const dLon = (lon2 - lon1) * Math.PI / 180;

    const a =
        Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(lat1 * Math.PI / 180) *
        Math.cos(lat2 * Math.PI / 180) *
        Math.sin(dLon / 2) *
        Math.sin(dLon / 2);

    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

    return R * c;
}


// ================= SHOW NEAREST =================
function showNearestHospitals(position) {

    userLat = position.coords.latitude;
    userLng = position.coords.longitude;

    document.getElementById("locationStatus").innerText =
        "📍 Location detected";

    hospitalsData.forEach(h => {

        // IMPORTANT: use lng not lon
        h.distance = getDistance(userLat, userLng, h.lat, h.lng);

    });

    hospitalsData.sort((a, b) => a.distance - b.distance);

    displayHospitals(hospitalsData.slice(0, 5));

}


// ================= MANUAL LOCATION =================
async function setManualLocation() {

    const area = document.getElementById("manualLocation").value;

    if (!area) return;

    const url = `https://nominatim.openstreetmap.org/search?format=json&q=${area},Bangalore`;

    const res = await fetch(url);
    const data = await res.json();

    if (data.length === 0) {
        alert("Location not found");
        return;
    }

    userLat = parseFloat(data[0].lat);
    userLng = parseFloat(data[0].lon);

    document.getElementById("locationStatus").innerText =
        "📍 " + area;

    hospitalsData.forEach(h => {
        h.distance = getDistance(userLat, userLng, h.lat, h.lng);
    });

    hospitalsData.sort((a, b) => a.distance - b.distance);

    displayHospitals(hospitalsData.slice(0, 5));
}


// ================= GOOGLE MAP NAVIGATION =================
function navigateToHospital(lat, lng) {

    if (!lat || !lng) {
        alert("Hospital location missing.");
        return;
    }

    if (userLat && userLng) {

        const url =
            `https://www.google.com/maps/dir/?api=1&origin=${userLat},${userLng}&destination=${lat},${lng}&travelmode=driving`;

        window.open(url, "_blank");

    } else {

        const url =
            `https://www.google.com/maps/search/?api=1&query=${lat},${lng}`;

        window.open(url, "_blank");
    }
}


// ================= DISPLAY =================
function displayHospitals(list) {

    const container = document.getElementById("hospitalResults");
    container.innerHTML = "";

    list.forEach(h => {

        const distanceText =
            h.distance && h.distance < 9999
                ? h.distance.toFixed(2) + " km"
                : "N/A";

        const card = `
            <div class="hospital-card">

                <h3>${h.name}</h3>

                <p><b>Type:</b> ${h.type}</p>
                <p><b>Area:</b> ${h.area}</p>
                <p><b>Phone:</b> ${h.phone}</p>
                <p><b>Distance:</b> ${distanceText}</p>

                <button 
                    class="navigate-btn"
                    onclick="navigateToHospital(${h.lat}, ${h.lng})"
                >
                    🚗 Navigate via Google Maps
                </button>

            </div>
        `;

        container.innerHTML += card;

    });

}


// ================= ERROR =================
function errorHandler() {

    alert("Location access denied. Please allow location.");

}
