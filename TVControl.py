import tkinter as tk
from TV import TV

class TVControl:
    def __init__(self, root):
        self.tv1 = TV()
        self.tv2 = TV()

        root.title("TV Control")

        # TV1 Controls
        self.tv1_label = tk.Label(root, text="TV1")
        self.tv1_label.grid(row=0, column=0, padx=10, pady=10)

        self.tv1_status_label = tk.Label(root, text="Status: Off")
        self.tv1_status_label.grid(row=1, column=0, padx=10, pady=5)

        self.tv1_channel_label = tk.Label(root, text="Channel: 1")
        self.tv1_channel_label.grid(row=2, column=0, padx=10, pady=5)

        self.tv1_volume_label = tk.Label(root, text="Volume: 1")
        self.tv1_volume_label.grid(row=3, column=0, padx=10, pady=5)

        self.tv1_on_button = tk.Button(root, text="Turn On", command=self.turn_on_tv1)
        self.tv1_on_button.grid(row=4, column=0, padx=10, pady=5)

        self.tv1_off_button = tk.Button(root, text="Turn Off", command=self.turn_off_tv1)
        self.tv1_off_button.grid(row=5, column=0, padx=10, pady=5)

        self.tv1_channel_up_button = tk.Button(root, text="Channel Up", command=self.tv1_channel_up)
        self.tv1_channel_up_button.grid(row=6, column=0, padx=10, pady=5)

        self.tv1_channel_down_button = tk.Button(root, text="Channel Down", command=self.tv1_channel_down)
        self.tv1_channel_down_button.grid(row=7, column=0, padx=10, pady=5)

        self.tv1_volume_up_button = tk.Button(root, text="Volume Up", command=self.tv1_volume_up)
        self.tv1_volume_up_button.grid(row=8, column=0, padx=10, pady=5)

        self.tv1_volume_down_button = tk.Button(root, text="Volume Down", command=self.tv1_volume_down)
        self.tv1_volume_down_button.grid(row=9, column=0, padx=10, pady=5)

        # TV2 Controls
        self.tv2_label = tk.Label(root, text="TV2")
        self.tv2_label.grid(row=0, column=1, padx=10, pady=10)

        self.tv2_status_label = tk.Label(root, text="Status: Off")
        self.tv2_status_label.grid(row=1, column=1, padx=10, pady=5)

        self.tv2_channel_label = tk.Label(root, text="Channel: 1")
        self.tv2_channel_label.grid(row=2, column=1, padx=10, pady=5)

        self.tv2_volume_label = tk.Label(root, text="Volume: 1")
        self.tv2_volume_label.grid(row=3, column=1, padx=10, pady=5)

        self.tv2_on_button = tk.Button(root, text="Turn On", command=self.turn_on_tv2)
        self.tv2_on_button.grid(row=4, column=1, padx=10, pady=5)

        self.tv2_off_button = tk.Button(root, text="Turn Off", command=self.turn_off_tv2)
        self.tv2_off_button.grid(row=5, column=1, padx=10, pady=5)

        self.tv2_channel_up_button = tk.Button(root, text="Channel Up", command=self.tv2_channel_up)
        self.tv2_channel_up_button.grid(row=6, column=1, padx=10, pady=5)

        self.tv2_channel_down_button = tk.Button(root, text="Channel Down", command=self.tv2_channel_down)
        self.tv2_channel_down_button.grid(row=7, column=1, padx=10, pady=5)

        self.tv2_volume_up_button = tk.Button(root, text="Volume Up", command=self.tv2_volume_up)
        self.tv2_volume_up_button.grid(row=8, column=1, padx=10, pady=5)

        self.tv2_volume_down_button = tk.Button(root, text="Volume Down", command=self.tv2_volume_down)
        self.tv2_volume_down_button.grid(row=9, column=1, padx=10, pady=5)

        self.update_labels()

    def turn_on_tv1(self):
        self.tv1.turnOn()
        self.update_labels()

    def turn_off_tv1(self):
        self.tv1.turnOff()
        self.update_labels()

    def tv1_channel_up(self):
        self.tv1.channelUp()
        self.update_labels()

    def tv1_channel_down(self):
        self.tv1.channelDown()
        self.update_labels()

    def tv1_volume_up(self):
        self.tv1.volumeUp()
        self.update_labels()

    def tv1_volume_down(self):
        self.tv1.volumeDown()
        self.update_labels()

    def turn_on_tv2(self):
        self.tv2.turnOn()
        self.update_labels()

    def turn_off_tv2(self):
        self.tv2.turnOff()
        self.update_labels()

    def tv2_channel_up(self):
        self.tv2.channelUp()
        self.update_labels()

    def tv2_channel_down(self):
        self.tv2.channelDown()
        self.update_labels()

    def tv2_volume_up(self):
        self.tv2.volumeUp()
        self.update_labels()

    def tv2_volume_down(self):
        self.tv2.volumeDown()
        self.update_labels()

    def update_labels(self):
        self.tv1_status_label.config(text=f"Status: {'On' if self.tv1.on else 'Off'}")
        self.tv1_channel_label.config(text=f"Channel: {self.tv1.getChannel()}")
        self.tv1_volume_label.config(text=f"Volume: {self.tv1.getVolume()}")

        self.tv2_status_label.config(text=f"Status: {'On' if self.tv2.on else 'Off'}")
        self.tv2_channel_label.config(text=f"Channel: {self.tv2.getChannel()}")
        self.tv2_volume_label.config(text=f"Volume: {self.tv2.getVolume()}")

if __name__ == "__main__":
    root = tk.Tk()
    tv_control = TVControl(root)
    root.mainloop() 
