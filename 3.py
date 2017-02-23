button_state = 0
button_up = 1 << 0
button_down = 1 << 1
button_left = 1 << 2
button_right = 1 << 3

# Flip the state of the right button regardless of its initial state
button_state ^= button_right
print(bin(button_state))
print(bin(button_up))
print(bin(button_down))
print(bin(button_left))
print(bin(button_right))
button_state |= button_left
print(bin(button_state))
# set down button to 0
button_state &= ~button_left
print(bin(button_state))

#flip all states
button_state = ~button_state
print(bin(button_state))

isDown = button_state & button_down
print(isDown)
isDown = isDown >> 3
print(isDown)