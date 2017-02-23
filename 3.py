button_state = 0
button_up = 1 << 0
button_down = 1 << 1
button_left = 1 << 2
button_right = 1 << 3

# set down button to 0
button_state &= ~button_left

# Flip the state of the right button regardless of its initial state
button_state ^= button_right

# flip all states
button_state = ~button_state

# Gives 1 if button is down, 0 otherwise
isDown = (button_state & button_down) >> 1