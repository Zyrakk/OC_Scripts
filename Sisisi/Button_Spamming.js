// Cantidad de segundos entre pulsaciones
let interval = 70;

// Abre la pagina princial de Oracle en una nueva pestaña
let secondTab = window.open("https://cloud.oracle.com/");

// Selecciona el boton con el querySelector
let button = document.querySelector(".oui-savant__Panel .oui-savant__Panel--Footer > .oui-button-primary");

let timer = setInterval(() => {
    secondTab.location.reload();
    console.log("!!! refreshed second tab");
    
    if (button && button.textContent == "Create") {
        button.click();
        console.log("!!! clicked button");
    } else {
        console.log("!!! no button to click");
    }
}, 1000 * interval);