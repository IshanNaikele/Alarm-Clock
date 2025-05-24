import tkinter as tk
import datetime
import time 
import pygame
import threading
 
def set_alarm():
    #To set the alarm time by user
    alarm_time=f"{hour.get()}:{minute.get()}:{second.get()}"
    #To update the label
    status_label.config(text=f"Set Alarm time {alarm_time}")

    def alarm_thread():
        #Until current time is equal to user time ,it will run
        while True :
            #To get current time from the system 
            current_time=datetime.datetime.now().strftime("%H:%M:%S")
            #checks the condition (alarm_time==current_time)
            if alarm_time==current_time:
                #Update the Label in the tkinter 
                status_label.config(text="Time's Up")
                #To initialize pygame,load the music and play it
                pygame.init()
                pygame.mixer.music.load("alarm_sound.mp3")
                pygame.mixer.music.play()
                break

            time.sleep(1)
    #Avoids GUI from freezing,alarm rangs in background
    threading.Thread(target=alarm_thread).start()


# GUI setup
root = tk.Tk()
root.title("Alarm Clock")
root.geometry("300x250")
root.resizable(False, False)

tk.Label(root, text="Set Alarm Time", font=("Helvetica", 14)).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

hour = tk.StringVar(value="00")
minute = tk.StringVar(value="00")
second = tk.StringVar(value="00")

tk.Entry(frame, textvariable=hour, width=3, font=("Helvetica", 18)).pack(side=tk.LEFT)
tk.Label(frame, text=":", font=("Helvetica", 18)).pack(side=tk.LEFT)
tk.Entry(frame, textvariable=minute, width=3, font=("Helvetica", 18)).pack(side=tk.LEFT)
tk.Label(frame, text=":", font=("Helvetica", 18)).pack(side=tk.LEFT)
tk.Entry(frame, textvariable=second, width=3, font=("Helvetica", 18)).pack(side=tk.LEFT)

tk.Button(root, text="Set Alarm", command=set_alarm).pack(pady=20)
status_label = tk.Label(root, text="", font=("Helvetica", 12))
status_label.pack()

root.mainloop()
