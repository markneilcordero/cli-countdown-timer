import time
import sys

def countdown(seconds):
    for i in range(seconds, -1, -1):
        sys.stdout.write(f"\rTime remaining: {i} second(s)")
        sys.stdout.flush()
        time.sleep(1)
    print("\nTime's up!")

if __name__ == "__main__":
    try:
        seconds = int(input("Enter the number of seconds for the countdown: "))
        countdown(seconds)
    except ValueError:
        print("Please enter a valid integer for seconds.")