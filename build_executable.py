import os
import sys
import subprocess
import shutil


def clean_build_directories():
    print("🧹 Cleaning old build directories...")
    dirs_to_clean = ['build', 'dist', '__pycache__']
    
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"   Removed {dir_name}/")
    
    if os.path.exists('guitar_tuner.spec'):
        os.remove('guitar_tuner.spec')
        print("   Removed guitar_tuner.spec")


def install_pyinstaller():
    print("📦 Checking PyInstaller installation...")
    try:
        import PyInstaller
        print("   PyInstaller is already installed")
    except ImportError:
        print("   Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("   ✓ PyInstaller installed successfully")


def build_executable():
    print("🔨 Building executable...")

    cmd = [
        sys.executable,
        '-m',
        'PyInstaller',
        '--name=GuitarTunerPro',
        '--onefile',
        '--windowed',
        '--icon=NONE',
        '--add-data=config;config',
        '--hidden-import=numpy',
        '--hidden-import=scipy',
        '--hidden-import=scipy.fft',
        '--hidden-import=customtkinter',
        '--hidden-import=PIL',
        '--hidden-import=pyaudio',
        '--collect-all=customtkinter',
        '--noconfirm',
        'guitar_tuner.py'
    ]

    print(f"   Running PyInstaller...")

    try:
        subprocess.check_call(cmd)
        print("   ✓ Build completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"   ✗ Build failed with error: {e}")
        return False
    except FileNotFoundError as e:
        print(f"   ✗ PyInstaller not found: {e}")
        return False


def create_readme_for_dist():
    readme_content = """# Guitar Tuner Pro - Executable

## 🎸 Quick Start

1. Double-click `GuitarTunerPro.exe` to launch the application
2. Select your instrument (Acoustic Guitar, Electric Guitar, Bass, or Ukulele)
3. Choose a tuning preset or create a custom tuning
4. Click "▶ Start Listening" and tune your instrument!

## 📋 System Requirements

- Windows 10 or later (64-bit)
- Microphone or audio input device
- Approximately 100 MB of disk space

## 🎮 Keyboard Shortcuts

- **Escape** - Exit full-screen mode
- **F11** - Enter full-screen mode

## 🐛 Troubleshooting

### Audio Input Issues
If the app can't detect your audio input:
1. Check that your microphone/audio interface is connected
2. Make sure Windows has permission to access your microphone
3. Try running the app as administrator

### First Launch
The first time you run the app, Windows Defender may scan it. This is normal.
The app may take a few seconds to start as it initializes audio devices.

## 📧 Support

For issues, suggestions, or contributions:
- GitHub: https://github.com/waynefaustorilla/guitar-tuner
- Report bugs: https://github.com/waynefaustorilla/guitar-tuner/issues

## 📝 License

This software is licensed under the MIT License.

---

**Made with ❤️ and ☕ by Espresso Assassino**

*Nothing is true, everything is permitted... to be in tune!* 🗡️
"""
    
    dist_readme_path = os.path.join('dist', 'README.txt')
    with open(dist_readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"   ✓ Created {dist_readme_path}")


def main():
    print("=" * 60)
    print("🎸 Guitar Tuner Pro - Executable Builder")
    print("=" * 60)
    print()
    
    clean_build_directories()
    print()
    
    install_pyinstaller()
    print()
    
    success = build_executable()
    print()
    
    if success:
        print("📝 Creating distribution files...")
        create_readme_for_dist()
        print()
        
        print("=" * 60)
        print("✅ BUILD SUCCESSFUL!")
        print("=" * 60)
        print()
        print("📦 Your executable is ready:")
        print(f"   Location: {os.path.abspath('dist/GuitarTunerPro.exe')}")
        print()
        print("📋 Distribution contents:")
        print("   - GuitarTunerPro.exe (Main application)")
        print("   - README.txt (User guide)")
        print()
        print("🚀 Next steps:")
        print("   1. Test the executable: dist/GuitarTunerPro.exe")
        print("   2. Create a ZIP file for distribution")
        print("   3. Upload to GitHub Releases")
        print()
        print("☕ Happy tuning!")
    else:
        print("=" * 60)
        print("❌ BUILD FAILED")
        print("=" * 60)
        print()
        print("Please check the error messages above and try again.")
        sys.exit(1)


if __name__ == "__main__":
    main()