import threading

def coach():
    import requests
    from time import sleep
    url = "http://192.168.178.46/api/xtndDDnn4UblMG-JH1uu6ka8HiouI9Wa66liRYly/groups/4/action"

    payload = "{\"on\":true, \"sat\":254, \"bri\":255,\"xy\":[0.7006,0.2993]}"
    headers = {}

    response = requests.request("PUT", url, data=payload, headers=headers)
    sleep(3)
    brightness = 255
    while True:
        import requests

        payload = "{\"on\":true, \"bri\":" + str(brightness) + ", \"transitiontime\":40}"

        response = requests.request("PUT", url, data=payload, headers=headers)

        if brightness <= 0:
            direction = "up"
        if brightness >= 255:
            direction = "down"

        if direction == "up":
            brightness = 255
        if direction == "down":
            brightness = 0
        sleep(3.0)


def workplace():
    import requests
    from time import sleep
    url = "http://192.168.178.46/api/xtndDDnn4UblMG-JH1uu6ka8HiouI9Wa66liRYly/groups/3/action"

    payload = "{\"on\":true, \"sat\":254, \"bri\":255,\"xy\":[0.7006,0.2993]}"
    headers = {}

    response = requests.request("PUT", url, data=payload, headers=headers)

    brightness = 46920
    direction = "down"
    while True:
        import requests

        payload = "{\"on\":true, \"sat\":255,\"hue\":"+ str(brightness) +", \"transitiontime\":15}"

        response = requests.request("PUT", url, data=payload, headers=headers)

        if brightness <= 0:
            direction = "up"
        if brightness >= 46920:
            direction = "down"

        if direction == "up":
            brightness = 46920
        if direction == "down":
            brightness = 0
        sleep(7.5)

t1 = threading.Thread(target=coach)
t1.start()
t2 = threading.Thread(target=workplace)
t2.start()