from TV import TV  # Import the TV class

def main():
    tv1 = TV()  # First object
    tv1.turnOn()  # Turns on tv1
    tv1.setChannel(30)  # Set the channel to 30
    tv1.setVolume(3)  # Set the volume level to 3

    tv2 = TV()  # Second object
    tv2.turnOn()  # Turns on tv2
    tv2.setChannel(3)  # Set the channel to 3
    tv2.setVolume(2)  # Set the volume level to 2

    # Print the channel and volume level of tv1
    print("tv1's channel is", tv1.getChannel(), "and volume level is", tv1.getVolume())

    # Print the channel and volume level of tv2
    print("tv2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolume())

if __name__ == "__main__":
    main()  # Call the main function to execute the program
