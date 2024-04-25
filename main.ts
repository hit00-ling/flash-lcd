function LCD_WRITE_HZ (hz: number[], page: number, col: number) {
    pins.digitalWritePin(DigitalPin.P10, 0)
    LCD_WRITE(176 + page)
    LCD_WRITE(16 + col / 16)
    LCD_WRITE(col % 16)
    pins.digitalWritePin(DigitalPin.P10, 1)
    for (let index1 = 0; index1 <= 15; index1++) {
        LCD_WRITE(hz[index1])
    }
    pins.digitalWritePin(DigitalPin.P10, 0)
    LCD_WRITE(177 + page)
    LCD_WRITE(16 + col / 16)
    LCD_WRITE(col % 16)
    pins.digitalWritePin(DigitalPin.P10, 1)
    for (let index2 = 0; index2 <= 15; index2++) {
        LCD_WRITE(hz[16 + index2])
    }
}
function LCD_INIT () {
    pins.spiPins(DigitalPin.P12, DigitalPin.P13, DigitalPin.P11)
    pins.spiFrequency(3000000)
    pins.spiFormat(8, 0)
    pins.digitalWritePin(DigitalPin.P8, 1)
    pins.digitalWritePin(DigitalPin.P9, 0)
    basic.pause(50)
    pins.digitalWritePin(DigitalPin.P9, 1)
    basic.pause(100)
    pins.digitalWritePin(DigitalPin.P10, 0)
    LCD_WRITE(226)
    LCD_WRITE(47)
    LCD_WRITE(175)
    LCD_WRITE(129)
    LCD_WRITE(16)
    LCD_WRITE(162)
    LCD_WRITE(160)
    LCD_WRITE(200)
    LCD_WRITE(167)
}
function LCD_WRITE (dat: number) {
    pins.digitalWritePin(DigitalPin.P8, 0)
    tmp = pins.spiWrite(dat)
    pins.digitalWritePin(DigitalPin.P8, 1)
}
let tmp = 0
basic.showLeds(`
    . # # # .
    # # . # #
    # . . . #
    . # # # .
    # . . . #
    `)
led.enable(false)
LCD_INIT()
let hz_xi = [
223,
223,
207,
207,
70,
20,
133,
193,
27,
17,
212,
198,
207,
223,
223,
223,
247,
243,
249,
252,
192,
192,
254,
254,
0,
0,
222,
158,
128,
192,
255,
255
]
LCD_WRITE_HZ(hz_xi, 0, 0)
LCD_WRITE_HZ(hz_xi, 0, 16)
LCD_WRITE_HZ(hz_xi, 0, 32)
LCD_WRITE_HZ(hz_xi, 0, 48)
basic.forever(function () {
	
})
