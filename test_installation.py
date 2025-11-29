"""
Test Installation Script
Run this to verify all dependencies are installed correctly
"""

import sys

def test_python_version():
    """Test if Python version is adequate"""
    print("Testing Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 7:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor} - Too old! Need 3.7+")
        return False

def test_pillow():
    """Test if Pillow is installed"""
    print("\nTesting Pillow (PIL)...")
    try:
        from PIL import Image
        import PIL
        print(f"✓ Pillow {PIL.__version__} - OK")
        return True
    except ImportError:
        print("✗ Pillow not installed!")
        print("  Install with: pip install Pillow")
        return False

def test_numpy():
    """Test if NumPy is installed"""
    print("\nTesting NumPy...")
    try:
        import numpy as np
        print(f"✓ NumPy {np.__version__} - OK")
        return True
    except ImportError:
        print("✗ NumPy not installed!")
        print("  Install with: pip install numpy")
        return False

def test_image_operations():
    """Test if basic image operations work"""
    print("\nTesting image operations...")
    try:
        from PIL import Image
        import numpy as np
        
        # Create a simple test image
        img_array = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
        img = Image.fromarray(img_array, 'RGB')
        
        # Test array conversion
        test_array = np.array(img)
        
        if test_array.shape == (100, 100, 3):
            print("✓ Image operations - OK")
            return True
        else:
            print("✗ Image operations failed")
            return False
    except Exception as e:
        print(f"✗ Image operations error: {str(e)}")
        return False

def test_file_operations():
    """Test if file operations work"""
    print("\nTesting file operations...")
    try:
        import os
        
        # Test write permission
        test_file = "test_write.txt"
        with open(test_file, 'w') as f:
            f.write("test")
        
        # Test read permission
        with open(test_file, 'r') as f:
            content = f.read()
        
        # Clean up
        os.remove(test_file)
        
        if content == "test":
            print("✓ File operations - OK")
            return True
        else:
            print("✗ File operations failed")
            return False
    except Exception as e:
        print(f"✗ File operations error: {str(e)}")
        return False

def print_system_info():
    """Print system information"""
    import platform
    print("\n" + "="*60)
    print("SYSTEM INFORMATION")
    print("="*60)
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Python Path: {sys.executable}")
    print("="*60)

def main():
    """Main test function"""
    print("\n" + "="*60)
    print(" "*15 + "INSTALLATION TEST")
    print("="*60)
    
    # Print system info
    print_system_info()
    
    print("\n" + "="*60)
    print("RUNNING TESTS")
    print("="*60)
    
    # Run all tests
    tests = [
        test_python_version(),
        test_pillow(),
        test_numpy(),
        test_image_operations(),
        test_file_operations()
    ]
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    passed = sum(tests)
    total = len(tests)
    
    print(f"Tests Passed: {passed}/{total}")
    
    if passed == total:
        print("\n✓ ALL TESTS PASSED! ✓")
        print("\nYou're ready to run the Image Encryption Tool!")
        print("Run: python image_encryptor.py")
    else:
        print(f"\n✗ {total - passed} TEST(S) FAILED")
        print("\nPlease install missing dependencies:")
        print("  pip install Pillow numpy")
        print("\nThen run this test again.")
    
    print("="*60 + "\n")

if __name__ == "__main__":
    main()