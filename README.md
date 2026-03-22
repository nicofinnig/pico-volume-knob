# Pico USB Volume Knob

A simple USB volume controller built with Raspberry Pi Pico and an ALPS rotary encoder.

## Features

- Volume up / down using rotary encoder
- Mute toggle using push button
- Works as a USB HID device (no drivers needed)

## Hardware

- Raspberry Pi Pico
- ALPS 5-pin rotary encoder
- Jumper wires

## Wiring

Encoder (ALPS 5-pin)

C -> GND
A -> GP16
B -> GP17

Button:

SW -> GP18
SW -> GND

## Software

- CircuitPython
  - Download: https://circuitpython.org/downloads
- Adafruit HID library
  - https://circuitpython.org/libraries
    - Find correct library for lib package

## Setup

### 1. Install CircuitPython

- Hold `BOOTSEL` and connect Pico via USB
- Copy CircuitPython `.uf2` file to `RPI-RP2`
- Pico will reboot as `CIRCUITPY`

### 2. Install libraries

Create `lib/` (if not done automatically) folder inside `CIRCUITPY` and copy:

- `adafruit_hid/consumer_control.mpy`
- `adafruit_hid/consumer_control_code.mpy`

### 3. Upload code

Copy `code.py` to `CIRCUITPY`

## Usage

- Rotate encoder → adjust volume
- Press encoder → mute / unmute

## Notes

- If volume direction is reversed, swap pins GP16 and GP17
- Cheap encoders may produce noisy signals
- Button uses internal pull-up