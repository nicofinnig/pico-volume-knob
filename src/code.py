import time
import board
import digitalio
import rotaryio
import usb_hid

from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Create rotary encoder on GP16 and GP17
encoder = rotaryio.IncrementalEncoder(board.GP16, board.GP17)

# Create HID consumer control device
consumer = ConsumerControl(usb_hid.devices)

# Create button input on GP18 with internal pull-up
button = digitalio.DigitalInOut(board.GP18)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Store previous encoder position
last_position = encoder.position

# Store previous button state
last_button_state = button.value

# Store last valid button press time
last_button_time = 0

# Debounce time for button presses
DEBOUNCE_TIME = 0.25

while True:
    # Read current encoder position
    current_position = encoder.position

    # Check if encoder was rotated
    if current_position != last_position:
        # Send volume up when rotated one direction
        if current_position > last_position:
            consumer.send(ConsumerControlCode.VOLUME_INCREMENT)
        # Send volume down when rotated the other direction
        else:
            consumer.send(ConsumerControlCode.VOLUME_DECREMENT)

        # Update stored encoder position
        last_position = current_position

    # Read current button state
    current_button_state = button.value
    now = time.monotonic()

    # Detect button press on falling edge
    if last_button_state and not current_button_state:
        # Ignore repeated presses during debounce time
        if now - last_button_time > DEBOUNCE_TIME:
            consumer.send(ConsumerControlCode.MUTE)
            last_button_time = now

    # Store current button state for next loop
    last_button_state = current_button_state

    # Small delay to reduce CPU usage
    time.sleep(0.01)