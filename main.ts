input.onButtonPressed(Button.AB, function () {
    input.calibrateCompass()
})
basic.forever(function () {
    led.plotBrightness(4, 4, 20)
    led.plotBrightness(4, 3, 20)
})
basic.forever(function () {
    if (input.magneticForce(Dimension.Strength) > 0 && input.magneticForce(Dimension.Strength) <= 100) {
        led.plot(0, 4)
        led.unplot(0, 1)
        led.unplot(0, 3)
        led.unplot(0, 2)
        led.unplot(0, 0)
    } else if (input.magneticForce(Dimension.Strength) > 100 && input.magneticForce(Dimension.Strength) <= 200) {
        led.plot(0, 3)
        led.plot(0, 4)
        led.unplot(0, 1)
        led.unplot(0, 2)
        led.unplot(0, 0)
    } else if (input.magneticForce(Dimension.Strength) > 200 && input.magneticForce(Dimension.Strength) <= 300) {
        led.plot(0, 2)
        led.plot(0, 3)
        led.plot(0, 4)
        led.unplot(0, 0)
        led.unplot(0, 1)
    } else if (input.magneticForce(Dimension.Strength) > 300 && input.magneticForce(Dimension.Strength) <= 400) {
        led.plot(0, 1)
        led.plot(0, 2)
        led.plot(0, 3)
        led.plot(0, 4)
        led.unplot(0, 0)
    } else if (input.magneticForce(Dimension.Strength) > 400) {
        led.plot(0, 0)
        led.plot(0, 4)
        led.plot(0, 3)
        led.plot(0, 2)
        led.plot(0, 1)
    } else {
        led.unplot(0, 4)
        led.unplot(0, 3)
        led.unplot(0, 2)
        led.unplot(0, 1)
        led.unplot(0, 0)
    }
})
basic.forever(function () {
    if (input.magneticForce(Dimension.Y) > 0 && input.magneticForce(Dimension.Y) <= 100) {
        led.plot(2, 4)
        led.unplot(2, 1)
        led.unplot(2, 3)
        led.unplot(2, 2)
        led.unplot(2, 0)
    } else if (input.magneticForce(Dimension.Y) > 100 && input.magneticForce(Dimension.Y) <= 200) {
        led.plot(2, 3)
        led.plot(2, 4)
        led.unplot(0, 1)
        led.unplot(2, 2)
        led.unplot(2, 0)
    } else if (input.magneticForce(Dimension.Y) > 200 && input.magneticForce(Dimension.Y) <= 300) {
        led.plot(2, 2)
        led.plot(2, 3)
        led.plot(2, 4)
        led.unplot(2, 0)
        led.unplot(2, 1)
    } else if (input.magneticForce(Dimension.Y) > 300 && input.magneticForce(Dimension.Y) <= 400) {
        led.plot(2, 1)
        led.plot(2, 2)
        led.plot(2, 3)
        led.plot(2, 4)
        led.unplot(2, 0)
    } else if (input.magneticForce(Dimension.Y) > 400) {
        led.plot(2, 0)
        led.plot(2, 4)
        led.plot(2, 3)
        led.plot(2, 2)
        led.plot(2, 1)
    } else {
        led.unplot(2, 4)
        led.unplot(2, 3)
        led.unplot(2, 2)
        led.unplot(2, 1)
        led.unplot(2, 0)
    }
})
basic.forever(function () {
    if (input.magneticForce(Dimension.X) > 0 && input.magneticForce(Dimension.X) <= 100) {
        led.plot(1, 4)
        led.unplot(1, 1)
        led.unplot(1, 3)
        led.unplot(1, 2)
        led.unplot(1, 0)
    } else if (input.magneticForce(Dimension.X) > 100 && input.magneticForce(Dimension.X) <= 200) {
        led.plot(1, 3)
        led.plot(1, 4)
        led.unplot(1, 1)
        led.unplot(1, 2)
        led.unplot(1, 0)
    } else if (input.magneticForce(Dimension.X) > 200 && input.magneticForce(Dimension.X) <= 300) {
        led.plot(1, 2)
        led.plot(1, 3)
        led.plot(1, 4)
        led.unplot(1, 0)
        led.unplot(1, 1)
    } else if (input.magneticForce(Dimension.X) > 300 && input.magneticForce(Dimension.X) <= 400) {
        led.plot(1, 1)
        led.plot(1, 2)
        led.plot(1, 3)
        led.plot(1, 4)
        led.unplot(1, 0)
    } else if (input.magneticForce(Dimension.X) > 400) {
        led.plot(1, 0)
        led.plot(1, 4)
        led.plot(1, 3)
        led.plot(1, 2)
        led.plot(1, 1)
    } else {
        led.unplot(1, 4)
        led.unplot(1, 3)
        led.unplot(1, 2)
        led.unplot(1, 1)
        led.unplot(1, 0)
    }
})
basic.forever(function () {
    if (input.magneticForce(Dimension.Z) > 0 && input.magneticForce(Dimension.Z) <= 100) {
        led.plot(3, 4)
        led.unplot(3, 1)
        led.unplot(3, 3)
        led.unplot(3, 2)
        led.unplot(3, 0)
    } else if (input.magneticForce(Dimension.Z) > 100 && input.magneticForce(Dimension.Z) <= 200) {
        led.plot(3, 3)
        led.plot(3, 4)
        led.unplot(3, 1)
        led.unplot(3, 2)
        led.unplot(3, 0)
    } else if (input.magneticForce(Dimension.Z) > 200 && input.magneticForce(Dimension.Z) <= 300) {
        led.plot(3, 2)
        led.plot(3, 3)
        led.plot(3, 4)
        led.unplot(3, 0)
        led.unplot(3, 1)
    } else if (input.magneticForce(Dimension.Z) > 300 && input.magneticForce(Dimension.Z) <= 400) {
        led.plot(3, 1)
        led.plot(3, 2)
        led.plot(3, 3)
        led.plot(3, 4)
        led.unplot(3, 0)
    } else if (input.magneticForce(Dimension.Z) > 400) {
        led.plot(3, 0)
        led.plot(3, 4)
        led.plot(3, 3)
        led.plot(3, 2)
        led.plot(3, 1)
    } else {
        led.unplot(3, 4)
        led.unplot(3, 3)
        led.unplot(3, 2)
        led.unplot(3, 1)
        led.unplot(3, 0)
    }
})
