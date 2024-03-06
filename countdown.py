import time
from win10toast import ToastNotifier

def show_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=10)

def countdown_timer(seconds):
    print("Countdown Timer")
    print("----------------")
    print(f"Set timer for {seconds} seconds.")

    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"Time left: {timer}", end="\r")
        time.sleep(1)
        seconds -= 1

    print("\nTime's up! Timer has reached zero.")
    show_notification("Time's up!", "Your timer has reached zero.")

# Example usage
timer_duration = int(input("Enter the countdown duration in seconds: "))
countdown_timer(timer_duration)
