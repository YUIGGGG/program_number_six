from TV import TV

def main():
    tv1 = TV()
    tv1.turnOn()
    try:
        tv1.setChannel(130)  # Invalid channel
    except ValueError as e:
        print("Error:", e)

    try:
        tv1.setVolume(10)  # Invalid volume level
    except ValueError as e:
        print("Error:", e)

    try:
        tv1.channelDown()  # Should not change channel when TV is off
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
