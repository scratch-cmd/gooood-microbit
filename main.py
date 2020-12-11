led.plot_brightness(4, 4, 20)

def on_forever():
    if True:
        pass
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    else:
        led.unplot(0, 4)
        led.unplot(0, 3)
        led.unplot(0, 2)
        led.unplot(0, 1)
        led.unplot(0, 0)
basic.forever(on_forever)
