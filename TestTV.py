from TV import TV  # Import the TV class


def main():
    tv1 = TV()  # First object
    tv1.turn_on()  # Turns on tv1
    tv1.set_channel(37)  # Set the channel to 30.
    tv1.set_volume(5)  # Set the volume level to 3.

    tv2 = TV()  # Second object
    tv2.turn_on()  # Turns on tv2
    tv2.set_channel(38)
    tv2.set_volume(3)  # Increase volume by 1

    # Print the channel and volume level of tv1.
    print("tv1's channel is", tv1.get_channel(),
          "and volume Level is", tv1.get_volume_level())

    # Print the channel and volume level of tv2.
    print("tv2's channel is", tv2.get_channel(),
          "and volume level is", tv2.get_volume_level())


main()  # Call the main function execute the program.
