var counter = 0;
var instructions = {{ instructions | tojson }};

document.addEventListener('keyup', navigate);

function navigate(key) {
    // Right arrow key
    if (key.keyCode == "39") {
        next();
    }
    // Right arrow key
    else if (key.keyCode == "37") {
        previous();
    }
}

function next() {
    if (counter < instructions.length - 1) {
        counter++;
    }
    document.querySelector('#instruction').innerHTML = instructions[counter];
}

function previous() {
    if (counter == 0) {
        counter = 0;
    }
    else {
        counter--;
    }
    document.querySelector('#instruction').innerHTML = instructions[counter];
}
