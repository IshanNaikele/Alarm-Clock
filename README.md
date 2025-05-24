# 🔔 Python Alarm Clock

A simple and intuitive alarm clock application built with Python using Tkinter for the GUI and pygame for audio playback.

## ✨ Features

- **User-friendly GUI**: Clean and simple interface built with Tkinter
- **Custom Time Setting**: Set alarm time in HH:MM:SS format
- **Audio Alert**: Plays alarm sound when the set time is reached
- **Non-blocking Operation**: Uses threading to prevent GUI freezing
- **Real-time Status Updates**: Shows current alarm status

## 🛠️ Requirements

- Python 3.x
- tkinter (usually comes with Python)
- pygame
- An alarm sound file named `alarm_sound.mp3`

## 📦 Installation

1. Clone this repository:
```bash
git clone https://github.com/IshanNaikele/alarm-clock.git
cd alarm-clock
```

2. Install required dependencies:
```bash
pip install pygame
```

3. Add your alarm sound file:
   - Place an MP3 file named `alarm_sound.mp3` in the project directory
   - Or modify the code to use your preferred sound file

## 🚀 Usage

1. Run the application:
```bash
python alarm_clock.py
```

2. Set your desired alarm time:
   - Enter hours (00-23)
   - Enter minutes (00-59)
   - Enter seconds (00-59)

3. Click "Set Alarm" button

4. The alarm will ring when the current system time matches your set time

## 📋 How It Works

- The application uses `datetime` to get the current system time
- A separate thread continuously checks if the current time matches the alarm time
- When the time matches, pygame plays the alarm sound
- Threading ensures the GUI remains responsive while the alarm is running

## 🔧 Code Structure

- **GUI Setup**: Creates the main window with time input fields
- **set_alarm()**: Main function that handles alarm setting and creates monitoring thread
- **alarm_thread()**: Background thread that monitors time and triggers alarm

## 🎵 Audio Requirements

Make sure you have an audio file named `alarm_sound.mp3` in the same directory as the script. You can replace this with any MP3 file of your choice by modifying the filename in the code.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] Multiple alarm support
- [ ] Snooze functionality
- [ ] Different alarm tones
- [ ] 12-hour format option
- [ ] Alarm history
- [ ] Volume control

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Known Issues

- Requires exact time match (down to the second)
- Only supports MP3 audio format
- Single alarm functionality only

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Made with ❤️ using Python**
