import tkinter as tk

class TV:
    def __init__(self):
        self.channel = 1
        self.volumeLevel = 1
        self.on = False

    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.on = False

    def getChannel(self):
        return self.channel

    def setChannel(self, channel):
        if self.on and 1 <= channel <= 120:
            self.channel = channel

    def getVolume(self):
        return self.volumeLevel

    def setVolume(self, volumeLevel):
        if self.on and 1 <= volumeLevel <= 7:
            self.volumeLevel = volumeLevel

    def channelUp(self):
        if self.on and self.channel < 120:
            self.channel += 1

    def channelDown(self):
        if self.on and self.channel > 1:
            self.channel -= 1

    def volumeUp(self):
        if self.on and self.volumeLevel < 7:
            self.volumeLevel += 1

    def volumeDown(self):
        if self.on and self.volumeLevel > 1:
            self.volumeLevel -= 1

class TVControllerApp:
    def __init__(self, master):
        self.master = master
        self.tv = TV()

        # Create buttons for different actions
        self.on_button = tk.Button(master, text="Turn On", command=self.turn_on)
        self.on_button.pack(pady=5)

        self.off_button = tk.Button(master, text="Turn Off", command=self.turn_off)
        self.off_button.pack(pady=5)

        self.channel_up_button = tk.Button(master, text="Channel Up", command=self.channel_up)
        self.channel_up_button.pack(pady=5)

        self.channel_down_button = tk.Button(master, text="Channel Down", command=self.channel_down)
        self.channel_down_button.pack(pady=5)

        self.volume_up_button = tk.Button(master, text="Volume Up", command=self.volume_up)
        self.volume_up_button.pack(pady=5)

        self.volume_down_button = tk.Button(master, text="Volume Down", command=self.volume_down)
        self.volume_down_button.pack(pady=5)

    def turn_on(self):
        self.tv.turnOn()
        tk.messagebox.showinfo("TV Status", "TV turned on")

    def turn_off(self):
        self.tv.turnOff()
        tk.messagebox.showinfo("TV Status", "TV turned off")

    def channel_up(self):
        self.tv.channelUp()
        tk.messagebox.showinfo("Channel Changed", f"Current channel: {self.tv.getChannel()}")

    def channel_down(self):
        self.tv.channelDown()
        tk.messagebox.showinfo("Channel Changed", f"Current channel: {self.tv.getChannel()}")

    def volume_up(self):
        self.tv.volumeUp()
        tk.messagebox.showinfo("Volume Changed", f"Current volume level: {self.tv.getVolume()}")

    def volume_down(self):
        self.tv.volumeDown()
        tk.messagebox.showinfo("Volume Changed", f"Current volume level: {self.tv.getVolume()}")

# Create the main application window
root = tk.Tk()
root.title("TV Controller")

# Initialize the TV Controller App
app = TVControllerApp(root)

# Run the Tkinter event loop
root.mainloop()
