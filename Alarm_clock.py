import time
import winsound

# Function to set the alarm
def set_alarm(alarm_time):
    while True:
        # Get the current time in HH:MM:SS format
        current_time = time.strftime("%H:%M:%S")
        
        # Check if the current time matches the alarm time
        if current_time == alarm_time:
            print("Time to wake up!")  # Display a message
            play_alarm_sound()  # Play the alarm sound
            break  # Exit the loop when the alarm goes off
        
        time.sleep(1)  # Wait for 1 second before checking again

# Function to play the alarm sound
def play_alarm_sound():
    frequency = 2500  # Set the frequency of the beep (in Hz)
    duration = 1000  # Set the duration of the beep (in milliseconds)
    winsound.Beep(frequency, duration)  # Generate the beep sound

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS format): ")  # User input for alarm time
    set_alarm(alarm_time)  # Set and trigger the alarm
