// Global variables for navigation
let counter = 0;

// Global variables for timer
let time = null;
let intervalID = null;

document.addEventListener('keyup', navigate);
document.querySelector('#next').addEventListener('click', next);
document.querySelector('#previous').addEventListener('click', previous);

function navigate(key) {
    // Right arrow key means next
    if (key.keyCode == "39") {
        next();
    }
    // Right arrow key means previous
    else if (key.keyCode == "37") {
        previous();
    }
}

function next() {
    // If already at last instruction, do not update anything
    if (counter < instructions.length - 1) {
        counter++;
    }

    // Go to the next instruction
    let text = instructions[counter];
    document.querySelector('#instruction').innerHTML = text;

    checkTime(text);
}

function previous() {
    // If already at first instruction, do not update anything
    if (counter == 0) {
        counter = 0;
    }

    // Go back to the previous instruction
    else {
        counter--;
    }
    let text = instructions[counter];
    document.querySelector('#instruction').innerHTML = text;

    checkTime(text);
}

function checkTime(text) {
    // If necessary, start timer
    if (text.includes('seconds')) {
        let index = text.indexOf('seconds') - 3;
        time = parseInt(text.slice(index, index + 2));
        intervalID = setInterval(updateTime, 1000);
    }

    // Display nothing
    else {
        clearInterval(intervalID);
        document.querySelector('#timer').innerHTML = "";
    }
}

function formatTime(time) {
    // Display minutes left
    let minutes = Math.floor(time / 60);

    // Display seconds left in two digit format
    let seconds = time % 60;
    if (seconds < 10) {
        seconds = `0${seconds}`;
    }

    return `${minutes}:${seconds}`;
}

function updateTime() {
    document.querySelector('#timer').innerHTML = formatTime(time);
    time--;
    if (time == 0) {
        next();
    }
}
