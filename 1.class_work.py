import os
os.system('clear')

# TV class: Turn On, Turn Off, Volume Up, Volume Down, Channel Up, Channel Down, Set Channel and Set Volume.
#  and that's why you need to have an **instance object** of the TV class.

class TV:                                               # TV class with methods to turn on, turn off, change channel, change volume, set channel and set volume
    def __init__(self):                                 # Constructor method to initialize the TV object with default values
        self.channel = 1                                # Default channel when turned on - 1 (channel 1)
        self.volume_level = 1                           # Default volume level when turned on - 1 (max volume is 10)
        self.turned_on = False                          # Default state of the TV when created - False (turned off)

    def turn_on(self):                                  # Method to turn on the TV
        self.turned_on = True
    
    def turn_off(self):                                 # Method to turn off the TV
        self.turned_on = False

    def channel_up(self):                               # Method to chnage the channel to the next one
        if self.turned_on and self.channel < 100:       # If the TV is turned on and the channel is less than 100
            self.channel += 1                           # go to the next channel (for exanmpel, if the current channel is 3, the next channel will be 4)

    def channel_down(self):                             # Method to change the channel to the previous one
        if self.turned_on and self.channel > 1:         # If the TV is turned on and the channel is greater than 1
            self.channel -= 1                           # go to the previous channel (for exanmpel, if the current channel is 3, the previous channel will be 2)

    def set_channel(self, channel):                     # Method to set the TV to a specific channel
        if self.turned_on and 1 <= channel <= 100:      # If the TV is turned on and the channel is between 1 and 100
            self.channel = channel                      # set the TV to the specified channel (we will use the variable channel to input out desired channel)

    def volume_up(self):                                # Method to increase the volume by 1
        if self.turned_on and self.volume_level < 10:   # If the TV is turned on and the volume level is less than 10
            self.volume_level += 1                      # increase the volume by 1 (max volume is 10)

    def volume_down(self):                              # Method to lower the volume by 1
        if self.turned_on and self.volume_level > 1:    # If the TV is turned on and the volume level is greater than 1
            self.volume_level -= 1                      # lower the volume by 1 (min volume is 1)



my_tv = TV()                                            # Create an instance object of the TV class

print('Part 1: ============')
my_tv.turn_on()                                         # Turn the TV on
print("TV is turned on:", my_tv.turned_on)              

my_tv.set_channel(channel=5)                            # Set the channel to 5          
print("TV channel:", my_tv.channel)                     

my_tv.volume_up()                                       # Increase the volume by 1
print("TV volume level:", my_tv.volume_level)


print('\nPart 2: ============')
my_tv.turn_on()                                         # Turn the TV on
print("TV is turned on:", my_tv.turned_on)

my_tv.set_channel(channel=95)                           # Set the channel to 95
print("TV channel:", my_tv.channel)

my_tv.volume_up()                                       # Increase the volume by 1
print("TV volume level:", my_tv.volume_level)



print('\nExtra: ============')
change_choice = my_tv.set_channel(channel=0)            # create a variable to store the return value of the user input                        
channel_choice = int(input('Enter the channel number: '))    # Prompt the user to enter the channel number and convert it to an integer
my_tv.set_channel(channel_choice)                       # Set the channel to the user input
print("TV channel:", my_tv.channel)                     
