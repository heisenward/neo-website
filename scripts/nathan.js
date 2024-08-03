// nathan.js

function playAudio() {
    var audio = document.getElementById('audio0');
    if (audio) {
        audio.play();
    } else {
        console.error('Audio element not found');
    }
}
