# 🔨 Build Guide - Guitar Tuner Pro

This guide will help you build a standalone executable of Guitar Tuner Pro that can be distributed to users who don't have Python installed.

## 📋 Prerequisites

- Python 3.7 or higher installed
- All project dependencies installed (`pip install -r requirements.txt`)
- Windows OS (for building Windows executable)

## 🚀 Quick Build

### Option 1: Using the Build Script (Recommended)

Simply run the automated build script:

```bash
python build_executable.py
```

This script will:
1. ✅ Clean old build directories
2. ✅ Install PyInstaller if needed
3. ✅ Build the executable
4. ✅ Create distribution README
5. ✅ Show you where to find the executable

### Option 2: Manual Build

If you prefer to build manually:

1. **Install PyInstaller**
```bash
pip install pyinstaller
```

2. **Run PyInstaller**
```bash
pyinstaller --name=GuitarTunerPro --onefile --windowed --add-data="config;config" --collect-all=customtkinter --noconfirm guitar_tuner.py
```

3. **Find your executable**
```
dist/GuitarTunerPro.exe
```

## 📦 What Gets Built

After building, you'll find:

```
dist/
├── GuitarTunerPro.exe    # Main executable (~50-80 MB)
└── README.txt            # User guide (auto-generated)
```

## 🧪 Testing the Executable

Before distributing:

1. **Test on your machine**
   ```bash
   cd dist
   GuitarTunerPro.exe
   ```

2. **Test on a clean Windows machine** (without Python installed)
   - Copy the `dist` folder to another computer
   - Run `GuitarTunerPro.exe`
   - Verify all features work

3. **Test with different audio devices**
   - Built-in microphone
   - USB audio interface
   - External microphone

## 📤 Distribution

### Creating a Release Package

1. **Create a ZIP file**
   ```bash
   # From the project root
   cd dist
   # Rename folder
   cd ..
   ren dist GuitarTunerPro-v1.0-Windows
   # Create ZIP (use 7-Zip, WinRAR, or Windows built-in)
   ```

2. **What to include in the ZIP**
   - `GuitarTunerPro.exe`
   - `README.txt`
   - Optional: `LICENSE` file

### GitHub Release

1. **Create a new release on GitHub**
   - Go to: https://github.com/waynefaustorilla/guitar-tuner/releases
   - Click "Create a new release"
   - Tag version: `v1.0.0`
   - Release title: `Guitar Tuner Pro v1.0.0`

2. **Upload the ZIP file**
   - Drag and drop `GuitarTunerPro-v1.0-Windows.zip`
   - Add release notes

3. **Example Release Notes**
   ```markdown
   ## 🎸 Guitar Tuner Pro v1.0.0
   
   First official release of Guitar Tuner Pro!
   
   ### ✨ Features
   - Support for Acoustic Guitar, Electric Guitar, Bass, and Ukulele
   - 20+ preset tunings
   - Custom tuning editor
   - Real-time FFT-based frequency detection
   - Beautiful dark-themed UI
   - Full-screen mode
   
   ### 📥 Download
   - **Windows**: Download `GuitarTunerPro-v1.0-Windows.zip`
   - Extract and run `GuitarTunerPro.exe`
   
   ### 📋 System Requirements
   - Windows 10 or later (64-bit)
   - Microphone or audio input device
   - ~100 MB disk space
   
   ### 🐛 Known Issues
   - First launch may take a few seconds to initialize audio
   - Windows Defender may scan the executable on first run
   
   ---
   
   **Made with ❤️ and ☕ by Espresso Assassino**
   ```

## 🔧 Build Options Explained

### PyInstaller Flags

- `--name=GuitarTunerPro` - Name of the executable
- `--onefile` - Bundle everything into a single .exe file
- `--windowed` - No console window (GUI only)
- `--add-data="config;config"` - Include config directory
- `--collect-all=customtkinter` - Include all CustomTkinter files
- `--noconfirm` - Overwrite output directory without asking

### Advanced Options

If you need to customize the build:

```bash
pyinstaller \
  --name=GuitarTunerPro \
  --onefile \
  --windowed \
  --icon=icon.ico \                    # Add custom icon
  --add-data="config;config" \
  --hidden-import=numpy \
  --hidden-import=scipy.fft \
  --collect-all=customtkinter \
  --version-file=version.txt \         # Add version info
  --uac-admin \                        # Request admin rights
  guitar_tuner.py
```

## 🐛 Troubleshooting

### Build Fails

**Problem**: PyInstaller can't find modules
```
Solution: Install all dependencies first
pip install -r requirements.txt
```

**Problem**: "config" directory not found
```
Solution: Make sure you're running from project root
cd C:/Systems/guitar-tuner
python build_executable.py
```

### Executable Issues

**Problem**: Executable won't start
```
Solution: Check Windows Defender/Antivirus isn't blocking it
```

**Problem**: Audio doesn't work
```
Solution: Make sure audio device is connected before starting
```

**Problem**: Executable is too large
```
Solution: This is normal. The executable includes Python runtime
and all dependencies (~50-80 MB is expected)
```

## 📊 File Size Optimization

If you need a smaller executable:

1. **Use --onedir instead of --onefile**
   - Creates a folder with multiple files
   - Faster startup time
   - Smaller individual files

2. **Exclude unnecessary modules**
   ```bash
   --exclude-module=matplotlib
   --exclude-module=pandas
   ```

## 🔐 Code Signing (Optional)

For professional distribution, consider code signing:

1. Purchase a code signing certificate
2. Use `signtool.exe` to sign the executable
3. This prevents Windows SmartScreen warnings

## 📝 Version Management

Update version numbers in:
- `README.md` - Project version
- `guitar_tuner_app.py` - App version string
- GitHub release tag

## ✅ Pre-Release Checklist

Before releasing:

- [ ] All tests pass
- [ ] Executable builds successfully
- [ ] Tested on clean Windows machine
- [ ] Audio input works with multiple devices
- [ ] All instruments and tunings work
- [ ] Custom tuning feature works
- [ ] README.txt is included
- [ ] Version numbers are updated
- [ ] GitHub release notes are ready
- [ ] ZIP file is created

## 🎉 Success!

Once built and tested, your executable is ready to share with the world!

Users can simply:
1. Download the ZIP
2. Extract it
3. Run `GuitarTunerPro.exe`
4. Start tuning! 🎸

---

**Made with ❤️ and ☕ by Espresso Assassino**

*Nothing is true, everything is permitted... to be in tune!* 🗡️

