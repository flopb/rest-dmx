var API_BASE_URL = "http://raspberrypi.fritz.box:8080"


function set_from_json() {
    var data = JSON.stringify([
        {
            "fixtures": [
                "rgb1",
                "rgb2"
            ],
            "channels": {
                "1": 0,
                "2": 0,
                "3": 0,
                "4": 255,
                "5": 255,
                "6": 155,
                "7": 255,
                "8": 0
            }
        }
    ]);

    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", function () {
        if (this.readyState === 4) {
            console.log(this.responseText);
        }
    });

    xhr.open("POST", "/set_from_json");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("Cache-Control", "no-cache");

    xhr.send(data);
}

function call_script()
{
    var data = null;

    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", function () {
      if (this.readyState === 4) {
        console.log(this.responseText);
      }
    });

    xhr.open("GET", "/playscript?script=puppet");
    xhr.setRequestHeader("Cache-Control", "no-cache");

    xhr.send(data);
}


function all_off()
{
    var settings = {
    "async": true,
    "crossDomain": true,
    "url": API_BASE_URL + "/set_from_json",
    "method": "POST",
    "headers": {
    "Content-Type": "application/json",
    "Cache-Control": "no-cache",
    "Postman-Token": "98b303ae-e5ac-44e7-a27b-d4de5e2765ec"
    },
    "processData": false,
    "data": "[\r\n   {\r\n      \"fixtures\":[\r\n         \"rgb1\",\r\n         \"rgb2\"\r\n      ],\r\n      \"channels\": {\r\n\t      \"1\":0,\r\n\t      \"2\":0,\r\n\t      \"3\":0,\r\n\t      \"4\":0,\r\n\t      \"5\":0,\r\n\t      \"6\":0,\r\n\t      \"7\":0,\r\n\t      \"8\":0\r\n      }\r\n   }\r\n]"
    }

    $.ajax(settings).done(function (response) {
    console.log(response);
    });
}

function puppet()
{
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": API_BASE_URL + "/playscript?script=puppet",
      "method": "GET",
      "headers": {
      }
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
    });
}

function fogOn() {
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": API_BASE_URL + "/set_from_json",
      "method": "POST",
      "headers": {
        "Content-Type": "application/json",
        "cache-control": "no-cache"
      },
      "processData": false,
      "data": "[\r\n   {\r\n      \"fixtures\":[\r\n         \"fog\"\r\n      ],\r\n      \"channels\": {\r\n\t      \"1\":255\r\n      }\r\n   }\r\n]"
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
    });
}

function fogOff() {
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": API_BASE_URL + "/set_from_json",
      "method": "POST",
      "headers": {
        "Content-Type": "application/json",
        "cache-control": "no-cache"
      },
      "processData": false,
      "data": "[\r\n   {\r\n      \"fixtures\":[\r\n         \"fog\"\r\n      ],\r\n      \"channels\": {\r\n\t      \"1\":0\r\n      }\r\n   }\r\n]"
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
    });
}

function uv(brightness=255) {
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": API_BASE_URL + "/set_from_json",
      "method": "POST",
      "headers": {
        "Content-Type": "application/json",
        "cache-control": "no-cache",
        "Postman-Token": "15528781-e01b-473b-94ce-68cbf074f240"
      },
      "processData": false,
      "data": "[\r\n   {\r\n      \"fixtures\":[\r\n         \"uv\"\r\n      ],\r\n      \"channels\": {\r\n\t      \"1\":" + brightness + ",\r\n\t      \"2\":255,\r\n\t      \"3\":255,\r\n\t      \"4\":255,\r\n\t      \"5\":0,\r\n\t      \"6\":0,\r\n\t      \"7\":0\r\n      }\r\n   }\r\n]"
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
    });
}

function allLights(value=255) {
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": API_BASE_URL + "/set_from_json",
      "method": "POST",
      "headers": {
        "Content-Type": "application/json",
        "cache-control": "no-cache"
      },
      "processData": false,
      "data": "[\r\n   {\r\n      \"fixtures\":[\r\n      \t \"rgb1\",\r\n      \t \"rgb2\",\r\n      \t \"rgb3\",\r\n         \"rgb4\",\r\n         \"rgb5\",\r\n         \"rgb6\",\r\n         \"rgb7\",\r\n         \"rgb8\"\r\n      ],\r\n      \"channels\": {\r\n\t      \"1\":0,\r\n\t      \"2\":0,\r\n\t      \"3\":0,\r\n\t      \"4\":"+value+",\r\n\t      \"5\":"+value+",\r\n\t      \"6\":"+value+",\r\n\t      \"7\":"+value+",\r\n\t      \"8\":"+value+"\r\n      }\r\n   }\r\n]"
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
    });
}

function thunder() {
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": API_BASE_URL + "/playscript?script=lightning",
      "method": "GET",
      "headers": {
        "cache-control": "no-cache"
      }
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
    });
}

function red() {
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": API_BASE_URL + "/set_from_json",
      "method": "POST",
      "headers": {
        "Content-Type": "application/json",
        "cache-control": "no-cache"
      },
      "processData": false,
      "data": "[\r\n   {\r\n      \"fixtures\":[\r\n      \t \"rgb1\",\r\n      \t \"rgb2\",\r\n      \t \"rgb3\",\r\n         \"rgb4\",\r\n         \"rgb5\",\r\n         \"rgb6\",\r\n         \"rgb7\",\r\n         \"rgb8\"\r\n      ],\r\n      \"channels\": {\r\n\t      \"1\":0,\r\n\t      \"2\":0,\r\n\t      \"3\":0,\r\n\t      \"4\":255,\r\n\t      \"5\":255,\r\n\t      \"6\":0,\r\n\t      \"7\":0,\r\n\t      \"8\":0\r\n      }\r\n   }\r\n]"
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
    });
}

function green() {
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": API_BASE_URL + "/set_from_json",
      "method": "POST",
      "headers": {
        "Content-Type": "application/json",
        "cache-control": "no-cache"
      },
      "processData": false,
      "data": "[\r\n   {\r\n      \"fixtures\":[\r\n      \t \"rgb1\",\r\n      \t \"rgb2\",\r\n      \t \"rgb3\",\r\n         \"rgb4\",\r\n         \"rgb5\",\r\n         \"rgb6\",\r\n         \"rgb7\",\r\n         \"rgb8\"\r\n      ],\r\n      \"channels\": {\r\n\t      \"1\":0,\r\n\t      \"2\":0,\r\n\t      \"3\":0,\r\n\t      \"4\":255,\r\n\t      \"5\":0,\r\n\t      \"6\":255,\r\n\t      \"7\":0,\r\n\t      \"8\":0\r\n      }\r\n   }\r\n]"
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
    });
}

function blue() {
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": API_BASE_URL + "/set_from_json",
      "method": "POST",
      "headers": {
        "Content-Type": "application/json",
        "cache-control": "no-cache"
      },
      "processData": false,
      "data": "[\r\n   {\r\n      \"fixtures\":[\r\n      \t \"rgb1\",\r\n      \t \"rgb2\",\r\n      \t \"rgb3\",\r\n         \"rgb4\",\r\n         \"rgb5\",\r\n         \"rgb6\",\r\n         \"rgb7\",\r\n         \"rgb8\"\r\n      ],\r\n      \"channels\": {\r\n\t      \"1\":0,\r\n\t      \"2\":0,\r\n\t      \"3\":0,\r\n\t      \"4\":255,\r\n\t      \"5\":0,\r\n\t      \"6\":0,\r\n\t      \"7\":255,\r\n\t      \"8\":0\r\n      }\r\n   }\r\n]"
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
    });
}

function video() {
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": API_BASE_URL + "/playscript?script=video",
      "method": "GET",
      "headers": {
        "cache-control": "no-cache"
      }
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
    });
}

function video2() {
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": API_BASE_URL + "/playscript?script=video2",
      "method": "GET",
      "headers": {
        "cache-control": "no-cache"
      }
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
    });
}

function hue_normal() {
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": API_BASE_URL + "/api/xtndDDnn4UblMG-JH1uu6ka8HiouI9Wa66liRYly/groups/0/action",
      "method": "PUT",
      "headers": {
      },
      "processData": false,
      "data": "{\"on\":true, \"sat\":254, \"bri\":254,\"xy\":[0.5006,0.3993]}"
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
    });
}

function hue_red() {
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": API_BASE_URL + "/api/xtndDDnn4UblMG-JH1uu6ka8HiouI9Wa66liRYly/groups/0/action",
      "method": "PUT",
      "headers": {
      },
      "processData": false,
      "data": "{\"on\":true, \"sat\":254, \"bri\":254,\"xy\":[0.7006,0.2993]}"
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
    });
}

function black_widow_entrance() {
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": API_BASE_URL + "/api/xtndDDnn4UblMG-JH1uu6ka8HiouI9Wa66liRYly/lights/14/state",
      "method": "PUT",
      "headers": {
      },
      "processData": false,
      "data": "{\"on\":true, \"xy\":[0.7006,0.2593]}"
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
    });
}

function hue_entry_bulb_off() {
    var settings = {
    "async": true,
    "crossDomain": true,
    "url": API_BASE_URL + "/api/xtndDDnn4UblMG-JH1uu6ka8HiouI9Wa66liRYly/lights/14/state",
    "method": "PUT",
    "headers": {},
    "processData": false,
    "data": "{\"on\":false}"
    }

    $.ajax(settings).done(function (response) {
    console.log(response);
    });
}

function doorbell_button() {
    button = document.getElementById("bell_button")
    button.disabled="disabled"
    button.style.backgroundImage='linear-gradient(to bottom,#000000 0,#ff0000 290%)';
    button.innerHTML = "Ihr habt den Dunklen und seine schwarze Witwe gerufen!<br>Macht euch bereit für das Grauen!"
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": API_BASE_URL + "/doorbell",
      "method": "GET",
      "headers": {
        "cache-control": "no-cache"
      }
    }

    $.ajax(settings).done(function (response) {
        setTimeout(function(){
                button = document.getElementById("bell_button")
                button.disabled=""
                button.style.backgroundImage='linear-gradient(to bottom,#337ab7 0,#265a88 100%)';
                button.innerHTML = "Hier Klingeln<br>(touch me!)"

        }, 60000)
    });
}
var hue_counter = 0, howManyTimes = 255;
function doorbell() {
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": API_BASE_URL + "/ring",
      "method": "GET",
      "headers": {
        "cache-control": "no-cache"
      }
    }
    $.ajax(settings).done(function (response) {

    });

    hue_counter = 0
    //dim_up()


}

function dim_up() {
        var settings = {
            "async": true,
            "crossDomain": true,
            "url": API_BASE_URL + "/api/xtndDDnn4UblMG-JH1uu6ka8HiouI9Wa66liRYly/lights/14/state",
            "method": "PUT",
            "headers": {},
            "processData": false,
            "data": "{\"on\":true, \"bri\":"+(hue_counter*5)+"}"
        }

        $.ajax(settings).done(function (response) {

        });

        hue_counter++;
        console.log(hue_counter)
        if( hue_counter < howManyTimes ){
            setTimeout( dim_up, 80 );
        }
    }

function resetAll() {
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": API_BASE_URL + "/",
      "method": "GET",
      "headers": {
        "cache-control": "no-cache",
        "Postman-Token": "3ee6e32e-657c-4071-ae42-2dcddedf59b5"
      }
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
    });
}

color_changer_speed = 100
function colorChangerPlus()
{
    color_changer_speed = color_changer_speed + 5
    if(color_changer_speed > 255) {
        color_changer_speed = 255
    }
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": API_BASE_URL + "/set_from_json",
      "method": "POST",
      "headers": {
        "Content-Type": "application/json",
        "cache-control": "no-cache",
        "Postman-Token": "325c2fc3-9c46-4bf7-8c2e-ab519e21713b"
      },
      "processData": false,
      "data": "[\r\n   {\r\n      \"fixtures\":[\r\n         \"rgb2\",\r\n         \"rgb3\"\r\n      ],\r\n      \"channels\": {\r\n\t      \"1\":51,\r\n\t      \"2\":0,\r\n\t      \"3\":"+color_changer_speed+",\r\n\t      \"4\":255,\r\n\t      \"5\":255,\r\n\t      \"6\":0,\r\n\t      \"7\":0,\r\n\t      \"8\":0\r\n      }\r\n   }\r\n]"
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
    });
}

function colorChangerMinus()
{
    color_changer_speed = color_changer_speed - 5
    if(color_changer_speed < 0) {
        color_changer_speed = 0
    }
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": API_BASE_URL + "/set_from_json",
      "method": "POST",
      "headers": {
        "Content-Type": "application/json",
        "cache-control": "no-cache",
        "Postman-Token": "325c2fc3-9c46-4bf7-8c2e-ab519e21713b"
      },
      "processData": false,
      "data": "[\r\n   {\r\n      \"fixtures\":[\r\n         \"rgb2\",\r\n         \"rgb3\"\r\n      ],\r\n      \"channels\": {\r\n\t      \"1\":51,\r\n\t      \"2\":0,\r\n\t      \"3\":"+color_changer_speed+",\r\n\t      \"4\":255,\r\n\t      \"5\":255,\r\n\t      \"6\":0,\r\n\t      \"7\":0,\r\n\t      \"8\":0\r\n      }\r\n   }\r\n]"
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
    });
}

function play_script(scriptname) {
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": API_BASE_URL + "/playscript?script=" + scriptname,
      "method": "GET",
      "headers": {
        "cache-control": "no-cache",
        "Postman-Token": "c0d363b3-54d7-4492-bcbc-701637690032"
      }
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
    });
}

function puppet_off() {
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": API_BASE_URL + "/set_from_json",
      "method": "POST",
      "headers": {
        "Content-Type": "application/json",
        "cache-control": "no-cache",
        "Postman-Token": "3959c178-0d85-4d06-bc61-ac448f3690d1"
      },
      "processData": false,
      "data": "[\r\n   {\r\n      \"fixtures\":[\r\n         \"uv\",\r\n         \"rgb4\"\r\n      ],\r\n      \"channels\": {\r\n\t      \"1\":0,\r\n\t      \"2\":0,\r\n\t      \"3\":0,\r\n\t      \"4\":0,\r\n\t      \"5\":0,\r\n\t      \"6\":0,\r\n\t      \"7\":0,\r\n\t      \"8\":0\r\n      }\r\n   }\r\n]"
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
    });
}

function playpause() {
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": "http://192.168.178.28:9090/requests/status.xml?command=pl_pause",
      "method": "GET",
      "headers": {
      }
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
    });
}