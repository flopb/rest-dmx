##Perform X-UP and X-Down with moving heads
fx.mh_set_gobo("gobo", "mudball")
fx.mh_set_start("gobo1", rotation=110, tilt=50)
fx.mh_set_start("gobo2", rotation=235, tilt=50)
sleep(2)
fx.mh_move_to("gobo1",rotation=110, tilt=200, speed=150, update=True)
fx.mh_move_to("gobo2", rotation=235, tilt=200, speed=150, update=True)
sleep(2)
fx.mh_set_color("gobo", "red")
fx.mh_move_to("gobo1", rotation=110, tilt=50, speed=150, update=True)
fx.mh_move_to("gobo2", rotation=235, tilt=50, speed=150, update=True)

