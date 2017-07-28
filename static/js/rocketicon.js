$(document).ready(function() {

  var rockets = {
    "Antares": "antares.png",
    "Ariane5": "ariane5.png",
    "Aries1": "aries1.png",
    "Aries5": "aries5.png",
    "Atlas5": "atlas5.png",
    "Delta2": "delta2.png",
    "DeltaHeavy": "deltaheavy.png",
    "Electron": "electron.png",
    "Falcon9": "falcon9.png",
    "FalconHeavy": "falconheavy.png",
    "H-2A": "h2a.png",
    "LongueMarche": "longuemarche.png",
    "Minotaur4": "minotaur4.png",
    "NewGlenn": "newglenn.png",
    "Proton": "proton.png",
    "PSLV": "pslv.png",
    "Soyuz": "soyuz.png",
    "Vega": "vega.png"
  }

  function whichRocket(data) {
    for(key in rockets) {
      if (key == data) {
        return "static/images/rockets/" + rockets[key];
      }
    }
  }

  function setRocketIcon(someClass) {
    var icon = whichRocket(someClass);
    $('.'+someClass+'').attr('src', icon);
  }

  $('.rocket').each(function() {
    var thisClass = $(this).attr('class');
    thisClass = thisClass.split(" ");
    thisClass = thisClass[0];
    setRocketIcon(thisClass);
  });

});