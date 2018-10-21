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

    xhr.open("POST", "http://192.168.178.53:8081/set_from_json");
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

    xhr.open("GET", "http://192.168.178.53:8081/playscript?script=puppet");
    xhr.setRequestHeader("Cache-Control", "no-cache");

    xhr.send(data);
}


function all_off()
{
    var settings = {
    "async": true,
    "crossDomain": true,
    "url": "http://192.168.178.53:8081/set_from_json",
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

function puppe()
{
    var settings = {
    "async": true,
    "crossDomain": true,
    "url": "http://192.168.178.53:8081/set_from_json",
    "method": "POST",
    "headers": {
    "Content-Type": "application/json",
    "Cache-Control": "no-cache",
    "Postman-Token": "fdf88243-2628-4e07-8f81-f65a7b046d66"
    },
    "processData": false,
    "data": "[\r\n   {\r\n      \"fixtures\":[\r\n         \"rgb1\",\r\n         \"rgb2\"\r\n      ],\r\n      \"channels\": {\r\n\t      \"1\":250,\r\n\t      \"2\":40,\r\n\t      \"3\":180,\r\n\t      \"4\":0,\r\n\t      \"5\":0,\r\n\t      \"6\":0,\r\n\t      \"7\":0,\r\n\t      \"8\":0\r\n      }\r\n   }\r\n]"
    }

    $.ajax(settings).done(function (response) {
    console.log(response);
    });
}