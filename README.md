# 🎸 Guitar Tuner Pro

<div align="center">

A professional, full-featured guitar tuner application with a modern, interactive UI built with Python and CustomTkinter.

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

**Crafted by Espresso Assassino ☕**

</div>

## ✨ Features

### 🎸 Multiple Instrument Support
- **Acoustic Guitar** - Standard, Drop D, DADGAD, Open G, Open D
- **Electric Guitar** - Standard, Drop D, Drop C, Half Step Down, Drop B
- **Bass Guitar** - 4-string, 5-string, Drop D, Tenor
- **Ukulele** - Standard, Low G, Baritone, D Tuning

### 🎯 Advanced Tuning Features
- **Real-time frequency detection** using FFT (Fast Fourier Transform)
- **Interactive circular arc meter** with smooth animations and color-coded zones
- **Instrument-specific frequency ranges** for optimal accuracy
- **Custom tuning editor** - Create your own tunings with note-based input
- **Visual feedback** - Color-coded status (green = in tune, orange = close, red = out of tune)
- **Precision tuning** - ±3 Hz accuracy for "in tune" detection

### 🎨 Modern User Interface
- **Full-screen mode** with Escape/F11 toggle
- **Interactive instrument selector** with color-coded buttons
- **Visual string selection** with highlighted active string
- **Large, easy-to-read frequency display**
- **Animated tuning meter** with directional indicators (TUNE UP ↑ / TUNE DOWN ↓)
- **Dark theme** with professional aesthetics

## 📸 Screenshots

### Main Interface
The full-screen tuner interface with all controls visible.

### Tuning Meter
Large, interactive circular meter showing real-time tuning status with color zones.

### Instrument Selection
Easy-to-use button interface for switching between instruments.

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/waynefaustorilla/guitar-tuner.git
cd guitar-tuner
```

2. **Create a virtual environment**
```bash
python -m venv .venv
```

3. **Activate the virtual environment**

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 🎮 Usage

### Starting the Application
```bash
python guitar_tuner.py
```

### Keyboard Shortcuts
- **Escape** - Exit full-screen mode
- **F11** - Enter full-screen mode

### How to Tune

1. **Select your instrument** - Click on the instrument button (Acoustic Guitar, Electric Guitar, Bass, or Ukulele)
2. **Choose a tuning** - Select from preset tunings or create a custom tuning
3. **Select the string** - Click on the string you want to tune
4. **Start listening** - Click the "▶ Start Listening" button
5. **Play the string** - The meter will show if you're sharp (high) or flat (low)
6. **Adjust** - Tune your string until the meter shows "IN TUNE!" in green

### Custom Tuning

1. Click the "✏️ Custom" button in the tuning configuration
2. Select the note and octave for each string
3. Click "✓ Apply" to use your custom tuning

## 🏗️ Architecture

The application follows SOLID principles with a clean, modular architecture:

```
guitar-tuner/
├── models/              # Data models and business logic
│   ├── instrument.py
│   ├── instrument_repository.py
│   ├── tuning_preset.py
│   ├── tuning_repository.py
│   ├── custom_tuning.py
│   └── note_frequency_converter.py
├── audio/               # Audio processing
│   ├── audio_stream_manager.py
│   ├── audio_processor.py
│   ├── frequency_detector.py
│   └── fft_frequency_detector.py
├── analysis/            # Tuning analysis
│   ├── tuning_analyzer.py
│   ├── tuning_result.py
│   └── tuning_status.py
├── gui/                 # User interface components
│   ├── tuning_meter_widget.py
│   ├── instrument_selector.py
│   ├── tuning_selector.py
│   ├── string_selector.py
│   ├── frequency_display.py
│   ├── control_buttons.py
│   └── custom_tuning_dialog.py
├── guitar_tuner_app.py  # Main application
└── guitar_tuner.py      # Entry point
```

## 🔧 Technical Details

### Audio Processing
- **Sample Rate**: 44,100 Hz - Faster than a leap of faith
- **Chunk Size**: 4,096 samples - Precision in every strike
- **Algorithm**: Fast Fourier Transform (FFT) - Mathematical assassination of noise
- **Frequency Ranges**:
  - Acoustic/Electric Guitar: 60-400 Hz
  - Bass Guitar: 30-150 Hz
  - Ukulele: 140-550 Hz

### Tuning Accuracy
- **In Tune**: ±3 Hz - Perfect synchronization achieved
- **Close**: ±15 Hz - Target in sight
- **Out of Tune**: >15 Hz - Requires immediate action

### Technologies Used
- **Python 3.7+**
- **CustomTkinter 5.2.0+** - Modern UI framework
- **NumPy** - Numerical computing for audio processing
- **SciPy** - FFT implementation
- **PyAudio** - Audio input/output

### Tested Hardware
This application has been thoroughly tested with:
- **Squier Stratocaster** - A reliable blade for any assassin
- **JCraft S3** - Precision instrument for precision work
- **Focusrite Scarlett 2i2** - The audio interface of choice for stealthy operations

Works great with direct instrument input or through professional audio interfaces!

*No guitars were harmed during the making of this tuner (though a few strings may have been sacrificed to the tuning gods)*

## 📦 Dependencies

```
customtkinter>=5.2.0
numpy>=1.21.0
scipy>=1.7.0
pyaudio>=0.2.11
pillow>=9.0.0
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository from [https://github.com/waynefaustorilla/guitar-tuner](https://github.com/waynefaustorilla/guitar-tuner)
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- FFT algorithm implementation using SciPy - The mathematical hidden blade
- CustomTkinter for the modern UI framework - Sleek as an assassin's robes
- PyAudio for audio input handling - Eagle Vision for sound
- Countless espressos - The true fuel behind every commit ☕

## 📧 Contact

**Espresso Assassino** (Orlie Wayne A. Faustorilla)

- GitHub: [@waynefaustorilla](https://github.com/waynefaustorilla)
- LinkedIn: [Orlie Wayne A. Faustorilla](https://www.linkedin.com/in/orliewaynefaustorilla/)

Project Link: [https://github.com/waynefaustorilla/guitar-tuner](https://github.com/waynefaustorilla/guitar-tuner)

## 🐛 Known Issues

- On some systems, audio input may require additional permissions
- First-time startup may take a few seconds to initialize audio devices

## 🔮 Future Enhancements

- [ ] Add support for more instruments (mandolin, banjo, etc.)
- [ ] Implement pitch history graph
- [ ] Add metronome functionality
- [ ] Support for alternate tuning systems (just intonation, etc.)
- [ ] Mobile app version
- [ ] Cloud sync for custom tunings

---

<div align="center">

**Made with ❤️ and ☕ by Espresso Assassino**

*For musicians, by musicians*

</div>


### ☕ Support the Developer

If this tuner helped you nail that perfect pitch, consider supporting the project:

- ⭐ **Star this repository** - Show your appreciation and help others discover this tuner!

- 🍴 **Fork and contribute** - Add features, fix bugs, or improve documentation
- 🐛 **Report issues** - Help make this tuner better by reporting bugs or suggesting features
- 📢 **Share with fellow musicians** - Spread the word on social media, forums, or music communities
- 💬 **Leave feedback** - Share your experience and suggestions for improvements
- ☕ **Buy me an espresso** - Fuel the caffeine-powered code that keeps this tuner sharp!
- 📝 **Write a blog post or tutorial** - Help others learn how to use or extend this tuner
- 🎥 **Create a demo video** - Show the tuner in action with your instruments
- 🌍 **Translate the documentation** - Help make this accessible to musicians worldwide
- 🎸 **Test with different instruments** - Help expand hardware compatibility

Every bit of support helps keep this project alive and tuned to perfection!

<div style="color: red;" align="center">*Warning: May cause spontaneous guitar solos and perfectly tuned instruments*</div>