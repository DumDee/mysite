function playAudio(par) {
    console.log(par)
        // var audio = document.getElementById('testAudio');
    let el = par.getElementsByTagName('button')[0];
    let audio = par.getElementsByTagName('audio')[0];
    console.log(el)
    if (el.clName == 'is-playing') {
        el.clName = "";
        el.innerHTML = "Play"
        audio.pause();
    } else {
        el.clName = "is-playing";
        el.innerHTML = "Pause";
        audio.play();
    }

};