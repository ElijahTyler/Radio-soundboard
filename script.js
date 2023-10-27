let currentAudio;

function playSound(soundFile) {
    const audio = new Audio(soundFile);
    if(currentAudio !== audio){
        if(currentAudio){
            currentAudio.pause();
        }
        currentAudio = audio;
        currentAudio.play();
    } else {
        currentAudio.pause();
        currentAudio.currentTime = 0;
        currentAudio = null;
    }
}

function fadeOut(duration) {
    let volume = currentAudio.volume;
    const fadeAudio = setInterval(function () {
        if (volume <= 0) {
            clearInterval(fadeAudio);
            currentAudio.pause();
            currentAudio.currentTime = 0;
            currentAudio = null;
        } else {
            volume -= 0.1;
            currentAudio.volume = volume;
        }
    }, duration * 1000 / 10);

    // Add a short fade-out effect before pausing the audio
    setTimeout(function() {
        currentAudio.volume = 0;
    }, (duration - 0.1) * 1000);
}