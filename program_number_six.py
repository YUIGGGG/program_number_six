class TV:
    def __init__(self):
        # Initialize the TV class with the default settings.
        self.channel = 1  # Initial channel is set to 1.
        self.volume_level = 1  # Initial volume level is set to 1.
        self.on = False  # Initially, the TV is turned off.

    def turn_on(self):
        # Method to turn on the TV.
        self.on = True

    def turn_off(self):
        # Method to turn off the TV.
        self.on = False

    def get_channel(self):
        # Method to get the current channel.
        return self.channel

    def set_channel(self, channel):
        # Method to set the channel if the TV is on and the channel is within valid range (1-120).
        if self.on and 1 <= channel <= 120:
            self.channel = channel

    def get_volume_level(self):
        # Method to get the current volume level.
        return self.volume_level

    def set_volume(self, volume_level):
        # Method to set the volume level if the TV is on and the volume level is within valid range (1-7).
        if self.on and 1 <= volume_level <= 7:
            self.volume_level = volume_level

    def channel_up(self):
        # Method to increase the channel by 1 if the TV is on and the current channel is less than 120.
        if self.on and self.channel < 120:
            self.channel += 1

    def channel_down(self):
        # Method to decrease the channel by 1 if the TV is on and the current channel is greater than 1.
        if self.on and self.channel > 1:
            self.channel -= 1

    def volume_up(self):
        # Method to increase the volume level by 1 if the TV is on and the current volume level is less than 7.
        if self.on and self.volume_level < 7:
            self.volume_level += 1

    def volume_down(self):
        # Method to decrease the volume level by 1 if the TV is on and the current volume level is greater than 1.
        if self.on and self.volume_level > 1:
            self.volume_level -= 1