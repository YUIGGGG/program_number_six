class TV:
    def __init__(self):
        # Initialize the TV class with the default settings.
        self.channel = 1  # Initial channel is set to 1.
        self.volumeLevel = 1  # Initial volume level is set to 1.
        self.on = False  # Initially, the TV is turned off.

    def turnOn(self):
        # Method to turn on the TV.
        self.on = True

    def turnOff(self):
        # Method to turn off the TV.
        self.on = False

    def getChannel(self):
        # Method to get the current channel.
        return self.channel

    def setChannel(self, channel):
        # Method to set the channel if the TV is on and the channel is within valid range (1-120).
        if self.on and 1 <= channel <= 120:
            self.channel = channel

    def getVolume(self):
        # Method to get the current volume level.
        return self.volumeLevel

    def setVolume(self, volumeLevel):
        # Method to set the volume level if the TV is on and the volume level is within valid range (1-7).
        if self.on and 1 <= volumeLevel <= 7:
            self.volumeLevel = volumeLevel

    def channelUp(self):
        # Method to increase the channel by 1 if the TV is on and the current channel is less than 120.
        if self.on and self.channel < 120:
            self.channel += 1

    def channelDown(self):
        # Method to decrease the channel by 1 if the TV is on and the current channel is greater than 1.
        if self.on and self.channel > 1:
            self.channel -= 1

    def volumeUp(self):
        # Method to increase the volume level by 1 if the TV is on and the current volume level is less than 7.
        if self.on and self.volumeLevel < 7:
            self.volumeLevel += 1

    def volumeDown(self):
        # Method to decrease the volume level by 1 if the TV is on and the current volume level is greater than 1.
        if self.on and self.volumeLevel > 1:
            self.volumeLevel -= 1
