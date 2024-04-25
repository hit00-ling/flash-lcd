def LCD_WRITE_HZ(hz: List[number], page: number, col: number):
    pins.digital_write_pin(DigitalPin.P10, 0)
    LCD_WRITE(176 + page)
    LCD_WRITE(16 + col / 16)
    LCD_WRITE(col % 16)
    pins.digital_write_pin(DigitalPin.P10, 1)
    for index1 in range(16):
        LCD_WRITE(hz[index1])
    pins.digital_write_pin(DigitalPin.P10, 0)
    LCD_WRITE(177 + page)
    LCD_WRITE(16 + col / 16)
    LCD_WRITE(col % 16)
    pins.digital_write_pin(DigitalPin.P10, 1)
    for index2 in range(16):
        LCD_WRITE(hz[16 + index2])
def LCD_INIT():
    pins.spi_pins(DigitalPin.P12, DigitalPin.P13, DigitalPin.P11)
    pins.spi_frequency(3000000)
    pins.spi_format(8, 0)
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.digital_write_pin(DigitalPin.P9, 0)
    basic.pause(50)
    pins.digital_write_pin(DigitalPin.P9, 1)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P10, 0)
    LCD_WRITE(226)
    LCD_WRITE(47)
    LCD_WRITE(175)
    LCD_WRITE(129)
    LCD_WRITE(16)
    LCD_WRITE(162)
    LCD_WRITE(160)
    LCD_WRITE(200)
    LCD_WRITE(167)
def LCD_WRITE(dat: number):
    global tmp
    pins.digital_write_pin(DigitalPin.P8, 0)
    tmp = pins.spi_write(dat)
    pins.digital_write_pin(DigitalPin.P8, 1)
tmp = 0
hz_xi = [223,
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
    255]
hz_bao = [239,
    227,
    211,
    219,
    219,
    219,
    218,
    24,
    25,
    219,
    219,
    219,
    203,
    195,
    243,
    251,
    255,
    191,
    191,
    189,
    189,
    189,
    189,
    128,
    128,
    185,
    129,
    133,
    173,
    189,
    191,
    191]
basic.show_leds("""
    . # # # .
    # # . # #
    # . . . #
    . # # # .
    # . . . #
    """)
led.enable(False)
LCD_INIT()
LCD_WRITE_HZ(hz_xi, 0, 0)
LCD_WRITE_HZ(hz_bao, 0, 16)
LCD_WRITE_HZ(hz_xi, 0, 32)
LCD_WRITE_HZ(hz_bao, 0, 48)

def on_forever():
    pass
basic.forever(on_forever)
