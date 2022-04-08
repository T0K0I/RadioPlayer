
const songNameOuput = document.getElementById('songNameOuput');
const artistButton = document.getElementById('artistButton');
const messagesLoop = document.getElementById('messagesLoop');
const playTap = document.getElementById('playTap');
const radiostream = document.getElementById('radiostream');

const nextLi = document.getElementById('nextLi');
const secondNextLi = document.getElementById('secondNextLi');
const playerMenu = document.getElementById('playerMenu');


let playing = false;

let timeoutTill = null;

function getNewestInfo() {

  //messages
  // fetch(url + '/currentMessage?format=json')
  //   .then(response => response.json())
  //   .then(data => appendMessageInfo(data));

  //songs
  fetch('/currentSong?format=json')
    .then(response => response.json())
    .then(data => appendSongInfo(data));


  if (timeoutTill != null) {
    clearTimeout(timeoutTill);
  }

  timeoutTill = setTimeout(getNewestInfo, 30000);
}


function appendSongInfo(data) {
  console.log(data);
  //set the correct names
  songNameOuput.innerHTML = data.currentSong.name + ", by " + data.currentSong.artist;
  nextLi.innerHTML = data.nextSong.name + ", by " + data.nextSong.artist;
  secondNextLi.innerHTML = data.secondNextSong.name + ", by " + data.secondNextSong.artist;

  artistButton.href = data.currentSong.find_on;

}


function playRadio() {

  if (!playing) {

    getNewestInfo();
    radiostream.play();
    playing = true;
    playTap.innerText = "stop radio"
  }
  else {
    radiostream.pause();
    playTap.innerText = "play radio"
    playing = false;
  }

}


getNewestInfo();



