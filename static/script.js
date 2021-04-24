function getColorFromPing (ping) {
    if (ping != 0 && ping == null) {
        return "nodata"
    }

    else if (ping < 0) {
        return "dead"
    }
    
    else if (ping < 150) {
        return "excellent"
    } 
    
    else if (ping < 300) {
        return "good"
    }

    else if (ping < 450) {
        return "normal"
    } 
    
    else {
        return "bad"
    }
}

function clearServices () {
    const services = document.getElementById("services");
    services.innerHTML = "";
}

function addService (service) {
    const services = document.getElementById("services");
    const { name, address, port, connection, description, icon, history, result } = service;
    const { ping, is_alive } = result;
    const color = getColorFromPing(ping);
    const chart = [];

    for (let i = 0; i < 42; i++) {
        let item = history[i];

        chart.push(`
            <div class="chart-item chart-item-${getColorFromPing(item)}">.</div>
        `)
    }                    

    const el = `
        <div class="service">
            <div class="service-header">
                <img src="${icon}" alt="${name} service icon" class="service-icon"/>
                <div class="service-presentation">
                    <span class="service-name">${name}</span>
                    <span class="service-ping service-ping-${color}">${ is_alive ? ping == 0 ? "ONLINE" : ping + "ms" : "DEAD"}</span>
                    <p>
                        ${description}
                    </p>
                </div>
            </div>

            <div class="service-chart">
                ${chart.join("")}
            </div>

            <div class="service-footer">
                ${ connection.includes("minecraft") && is_alive ? ' <span class="service-ping player-count">' + result.players + "/" + result.max_players + '</span>' : "" } 
                <a href="https://${address}">${address}</a> at port ${port}
            </div>
        </div>
    `;
    services.innerHTML += el;
}

async function fetchServices () {
    const data = await fetch("/json");
    const json = await data.json();
    clearServices();
    for (const service of json.services) {
        addService(service);
    }
}

function refresh () {
    fetchServices();
}

fetchServices();

setInterval(() => {
    refresh();
}, 5 * 1000);