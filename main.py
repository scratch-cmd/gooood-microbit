def on_button_pressed_ab():
    input.calibrate_compass()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_forever():
    led.plot_brightness(4, 4, 20)
    led.plot_brightness(4, 3, 20)
basic.forever(on_forever)

def on_forever2():
    if input.magnetic_force(Dimension.STRENGTH) > 0 and input.magnetic_force(Dimension.STRENGTH) <= 100:
        led.plot(0, 4)
        led.unplot(0, 1)
        led.unplot(0, 3)
        led.unplot(0, 2)
        led.unplot(0, 0)
    elif input.magnetic_force(Dimension.STRENGTH) > 100 and input.magnetic_force(Dimension.STRENGTH) <= 200:
        led.plot(0, 3)
        led.plot(0, 4)
        led.unplot(0, 1)
        led.unplot(0, 2)
        led.unplot(0, 0)
    elif input.magnetic_force(Dimension.STRENGTH) > 200 and input.magnetic_force(Dimension.STRENGTH) <= 300:
        led.plot(0, 2)
        led.plot(0, 3)
        led.plot(0, 4)
        led.unplot(0, 0)
        led.unplot(0, 1)
    elif input.magnetic_force(Dimension.STRENGTH) > 300 and input.magnetic_force(Dimension.STRENGTH) <= 400:
        led.plot(0, 1)
        led.plot(0, 2)
        led.plot(0, 3)
        led.plot(0, 4)
        led.unplot(0, 0)
    elif input.magnetic_force(Dimension.STRENGTH) > 400:
        led.plot(0, 0)
        led.plot(0, 4)
        led.plot(0, 3)
        led.plot(0, 2)
        led.plot(0, 1)
    else:
        led.unplot(0, 4)
        led.unplot(0, 3)
        led.unplot(0, 2)
        led.unplot(0, 1)
        led.unplot(0, 0)
basic.forever(on_forever2)

def on_forever3():
    if input.magnetic_force(Dimension.Y) > 0 and input.magnetic_force(Dimension.Y) <= 100:
        led.plot(2, 4)
        led.unplot(2, 1)
        led.unplot(2, 3)
        led.unplot(2, 2)
        led.unplot(2, 0)
    elif input.magnetic_force(Dimension.Y) > 100 and input.magnetic_force(Dimension.Y) <= 200:
        led.plot(2, 3)
        led.plot(2, 4)
        led.unplot(0, 1)
        led.unplot(2, 2)
        led.unplot(2, 0)
    elif input.magnetic_force(Dimension.Y) > 200 and input.magnetic_force(Dimension.Y) <= 300:
        led.plot(2, 2)
        led.plot(2, 3)
        led.plot(2, 4)
        led.unplot(2, 0)
        led.unplot(2, 1)
    elif input.magnetic_force(Dimension.Y) > 300 and input.magnetic_force(Dimension.Y) <= 400:
        led.plot(2, 1)
        led.plot(2, 2)
        led.plot(2, 3)
        led.plot(2, 4)
        led.unplot(2, 0)
    elif input.magnetic_force(Dimension.Y) > 400:
        led.plot(2, 0)
        led.plot(2, 4)
        led.plot(2, 3)
        led.plot(2, 2)
        led.plot(2, 1)
    else:
        led.unplot(2, 4)
        led.unplot(2, 3)
        led.unplot(2, 2)
        led.unplot(2, 1)
        led.unplot(2, 0)
basic.forever(on_forever3)

def on_forever4():
    if input.magnetic_force(Dimension.X) > 0 and input.magnetic_force(Dimension.X) <= 100:
        led.plot(1, 4)
        led.unplot(1, 1)
        led.unplot(1, 3)
        led.unplot(1, 2)
        led.unplot(1, 0)
    elif input.magnetic_force(Dimension.X) > 100 and input.magnetic_force(Dimension.X) <= 200:
        led.plot(1, 3)
        led.plot(1, 4)
        led.unplot(1, 1)
        led.unplot(1, 2)
        led.unplot(1, 0)
    elif input.magnetic_force(Dimension.X) > 200 and input.magnetic_force(Dimension.X) <= 300:
        led.plot(1, 2)
        led.plot(1, 3)
        led.plot(1, 4)
        led.unplot(1, 0)
        led.unplot(1, 1)
    elif input.magnetic_force(Dimension.X) > 300 and input.magnetic_force(Dimension.X) <= 400:
        led.plot(1, 1)
        led.plot(1, 2)
        led.plot(1, 3)
        led.plot(1, 4)
        led.unplot(1, 0)
    elif input.magnetic_force(Dimension.X) > 400:
        led.plot(1, 0)
        led.plot(1, 4)
        led.plot(1, 3)
        led.plot(1, 2)
        led.plot(1, 1)
    else:
        led.unplot(1, 4)
        led.unplot(1, 3)
        led.unplot(1, 2)
        led.unplot(1, 1)
        led.unplot(1, 0)
basic.forever(on_forever4)

def on_forever5():
    if input.magnetic_force(Dimension.Z) > 0 and input.magnetic_force(Dimension.Z) <= 100:
        led.plot(3, 4)
        led.unplot(3, 1)
        led.unplot(3, 3)
        led.unplot(3, 2)
        led.unplot(3, 0)
    elif input.magnetic_force(Dimension.Z) > 100 and input.magnetic_force(Dimension.Z) <= 200:
        led.plot(3, 3)
        led.plot(3, 4)
        led.unplot(3, 1)
        led.unplot(3, 2)
        led.unplot(3, 0)
    elif input.magnetic_force(Dimension.Z) > 200 and input.magnetic_force(Dimension.Z) <= 300:
        led.plot(3, 2)
        led.plot(3, 3)
        led.plot(3, 4)
        led.unplot(3, 0)
        led.unplot(3, 1)
    elif input.magnetic_force(Dimension.Z) > 300 and input.magnetic_force(Dimension.Z) <= 400:
        led.plot(3, 1)
        led.plot(3, 2)
        led.plot(3, 3)
        led.plot(3, 4)
        led.unplot(3, 0)
    elif input.magnetic_force(Dimension.Z) > 400:
        led.plot(3, 0)
        led.plot(3, 4)
        led.plot(3, 3)
        led.plot(3, 2)
        led.plot(3, 1)
    else:
        led.unplot(3, 4)
        led.unplot(3, 3)
        led.unplot(3, 2)
        led.unplot(3, 1)
        led.unplot(3, 0)
basic.forever(on_forever5)
