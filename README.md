# 🔐 Image Encryption Tool

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey.svg)](https://github.com)

A powerful yet simple image encryption tool using pixel manipulation techniques. Encrypt and decrypt images using various algorithms including XOR, Pixel Swap, Mathematical Operations, and Channel Shuffling.

![Project Banner](https://via.placeholder.com/800x200/4A90E2/FFFFFF?text=Image+Encryption+Tool)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Encryption Methods](#encryption-methods)
- [Project Structure](#project-structure)
- [Technology Stack](#technology-stack)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## 🎯 Overview

This project demonstrates how images can be secured through pixel-level manipulation. It provides an interactive command-line interface for encrypting and decrypting images using custom encryption keys and multiple encryption algorithms.

**Use Cases:**
- Educational demonstrations of encryption concepts
- Understanding pixel manipulation
- Learning image processing with Python
- Exploring cryptographic fundamentals

## ✨ Features

- 🔒 **4 Encryption Algorithms**: XOR, Swap, Math, Shuffle
- 🔑 **Key-Based Security**: Custom encryption keys for personalized security
- 🖼️ **Multiple Format Support**: Works with JPG, PNG, BMP, and more
- 💻 **Cross-Platform**: Seamlessly runs on Windows and Linux
- 🎨 **Interactive CLI**: User-friendly command-line interface
- ✅ **Perfect Restoration**: Lossless decryption with correct key
- ⚡ **Fast Processing**: Efficient pixel manipulation algorithms

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/image-encryption-tool.git
cd image-encryption-tool
```

### Step 2: Install Dependencies

**Windows:**
```cmd
pip install -r requirements.txt
```

**Linux/Mac:**
```bash
pip3 install -r requirements.txt
```

Or install manually:
```bash
pip install Pillow numpy
```

### Step 3: Verify Installation

```bash
python test_installation.py
```

You should see all tests passing ✅

## 📖 Usage

### Basic Usage

1. **Run the program:**
   ```bash
   python image_encryptor.py
   ```

2. **Enter your encryption key** (remember this for decryption!)
   ```
   Enter encryption key: 12345
   ```

3. **Choose an option:**
   - `1` - Encrypt Image
   - `2` - Decrypt Image
   - `3` - Exit

### Encrypting an Image

```bash
Choose option: 1
Enter input image path: photo.jpg
Enter output path: encrypted.png
Select method (1-4): 1
```

### Decrypting an Image

```bash
Choose option: 2
Enter encrypted image path: encrypted.png
Enter output path: decrypted.jpg
Select method (1-4): 1  # Use same method as encryption
```

### Command Line Example

```bash
# Start the program
python image_encryptor.py

# Output:
# ============================================================
#                IMAGE ENCRYPTION TOOL
#           Pixel Manipulation Based Encryption
# ============================================================
# 
# Enter encryption key (any number, default 123): 12345
# 
# Choose an option:
# 1. Encrypt Image
# 2. Decrypt Image
# 3. Exit
```

## 🔐 Encryption Methods

### 1. XOR Encryption
- **Algorithm**: Bitwise XOR with key-generated pattern
- **Security**: ⭐⭐⭐
- **Speed**: ⚡⚡⚡
- **Best For**: Quick encryption tasks

### 2. SWAP Encryption
- **Algorithm**: Random pixel position swapping
- **Security**: ⭐⭐⭐⭐
- **Speed**: ⚡⚡
- **Best For**: Photographs and detailed images

### 3. MATH Encryption
- **Algorithm**: Mathematical operations on pixel values
- **Security**: ⭐⭐⭐
- **Speed**: ⚡⚡⚡
- **Best For**: Simple encryption needs

### 4. SHUFFLE Encryption
- **Algorithm**: RGB channel shuffling with noise addition
- **Security**: ⭐⭐⭐⭐
- **Speed**: ⚡⚡
- **Best For**: Color images requiring strong encryption

## 🛠️ Technology Stack

- **Language**: Python 3.7+
- **Libraries**:
  - `Pillow (PIL)` - Image processing and manipulation
  - `NumPy` - Numerical operations on pixel arrays
  - `sys` & `os` - System and file operations

## 🔧 How It Works

### Encryption Process

1. **Load Image**: Read image file and convert to RGB format
2. **Convert to Array**: Transform image into NumPy array (pixel matrix)
3. **Apply Algorithm**: Use selected encryption method with secret key
4. **Generate Output**: Convert encrypted array back to image format
5. **Save**: Write encrypted image to disk

### Decryption Process

1. **Load Encrypted Image**: Read the encrypted image file
2. **Convert to Array**: Transform to NumPy array
3. **Apply Reverse Algorithm**: Use same method with same key
4. **Restore Original**: Convert decrypted array back to image
5. **Save**: Write restored image to disk


## 🧪 Testing

Run the test suite to verify everything works correctly:

```bash
python test_installation.py
```

Expected output:
```
============================================================
               INSTALLATION TEST
============================================================

RUNNING TESTS
============================================================
Testing Python version...
✓ Python 3.11.x - OK

Testing Pillow (PIL)...
✓ Pillow 10.x.x - OK

Testing NumPy...
✓ NumPy 1.x.x - OK

Testing image operations...
✓ Image operations - OK

Testing file operations...
✓ File operations - OK

============================================================
TEST SUMMARY
============================================================
Tests Passed: 5/5

✓ ALL TESTS PASSED! ✓
```

## 🤝 Contributing
### Ideas for Contribution

- Add GUI using Tkinter or PyQt
- Implement additional encryption algorithms
- Add batch processing for multiple images
- Create image comparison feature
- Improve performance optimization
- Add unit tests
- Enhance documentation


## 🙏 Acknowledgments

- Inspired by cryptography and image processing concepts
- Built as part of internship project work
- Thanks to the Python community for excellent libraries

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/image-encryption-tool/issues) page
2. Create a new issue with detailed information
3. Reach out via email or LinkedIn

## 🌟 Show Your Support

If you found this project helpful, please give it a ⭐️!

---

<p align="center">Made with ❤️ by Bhavesh Pooniwala</p>
<p align="center">
  <a href="https://github.com/Bhaveshpooniwala1">GitHub</a> •
  <a href="https://www.linkedin.com/in/bhavesh-pooniwala/">LinkedIn</a> •
  <a href="mailto:pooniwalabhavesh7680@gmail.com">Email</a>
</p>