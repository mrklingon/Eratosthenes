function dispNum (nmbr: number) {
    light.setAll(0x000000)
    snum = convertToText(nmbr)
    for (let index = 0; index <= snum.length - 1; index++) {
        cn = snum.substr(index, 1)
        light.setAll(0x00ffff)
        for (let cx = 0; cx <= parseFloat(cn) - 1; cx++) {
            light.setPixelColor(cx, 0xffff00)
        }
        pause(2000)
    }
    light.setAll(0x000000)
}
input.touchA1.onEvent(ButtonEvent.Click, function () {
    dispNum(pick)
})
function rndColor () {
    light.setPixelColor(Math.randomRange(0, 9), light.rgb(Math.randomRange(10, 100), Math.randomRange(10, 100), Math.randomRange(10, 100)))
}
function ESieve (limit: number) {
    Sieve = []
    for (let i = 0; i < limit + 1; i++) {
        Sieve.push(1)
    }
    p = 2
    Sieve[1] = 0
    while (p <= limit) {
        if (1 == Sieve[p]) {
            px = p
            py = p
            while (limit >= px * py) {
                Sieve[px * py] = 0
                py += 1
                rndColor()
            }
            p += 1
        } else {
            p += 1
        }
    }
}
input.buttonB.onEvent(ButtonEvent.Click, function () {
    for (let index = 0; index <= 1000; index++) {
        if (1 == Sieve[index]) {
            BinNum(index)
            pause(2000)
        }
    }
})
function BinNum (value: number) {
    light.setAll(0x007fff)
    tv = value
    idx = 0
    while (tv > 0) {
        if (tv % 2 == 1) {
            light.setPixelColor(idx, 0x00ff00)
        }
        tv = Math.trunc(tv / 2)
        idx += 1
    }
}
input.buttonA.onEvent(ButtonEvent.Click, function () {
    pick = Math.randomRange(0, 1000)
    while (0 == Sieve[pick]) {
        pick = Math.randomRange(0, 1000)
    }
    BinNum(pick)
    pause(2000)
    dispNum(pick)
})
let idx = 0
let tv = 0
let py = 0
let px = 0
let p = 0
let pick = 0
let cn = ""
let snum = ""
let Sieve: number[] = []
Sieve = [1, 2]
ESieve(1000)
