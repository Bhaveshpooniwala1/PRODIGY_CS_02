"""
Image Encryption Tool using Pixel Manipulation
Author: Internship Project
Description: Encrypt and decrypt images using pixel manipulation techniques
"""

from PIL import Image
import numpy as np
import os
import sys

class ImageEncryptor:
    def __init__(self, key=123):
        """
        Initialize the encryptor with a secret key
        
        Args:
            key (int): Secret key for encryption/decryption
        """
        self.key = key
        np.random.seed(key)
    
    def encrypt_image(self, input_path, output_path, method='xor'):
        """
        Encrypt an image using specified method
        
        Args:
            input_path (str): Path to input image
            output_path (str): Path to save encrypted image
            method (str): Encryption method ('xor', 'swap', 'math', 'shuffle')
        """
        try:
            # Open and convert image to RGB
            img = Image.open(input_path)
            img_rgb = img.convert('RGB')
            img_array = np.array(img_rgb)
            
            print(f"Original image shape: {img_array.shape}")
            
            # Apply encryption based on method
            if method == 'xor':
                encrypted = self._xor_encrypt(img_array)
            elif method == 'swap':
                encrypted = self._swap_encrypt(img_array)
            elif method == 'math':
                encrypted = self._math_encrypt(img_array)
            elif method == 'shuffle':
                encrypted = self._shuffle_encrypt(img_array)
            else:
                raise ValueError("Invalid method. Choose: xor, swap, math, shuffle")
            
            # Save encrypted image
            encrypted_img = Image.fromarray(encrypted.astype('uint8'), 'RGB')
            encrypted_img.save(output_path)
            
            print(f"✓ Image encrypted successfully!")
            print(f"✓ Encrypted image saved at: {output_path}")
            print(f"✓ Method used: {method.upper()}")
            
        except FileNotFoundError:
            print(f"✗ Error: File '{input_path}' not found!")
            sys.exit(1)
        except Exception as e:
            print(f"✗ Error during encryption: {str(e)}")
            sys.exit(1)
    
    def decrypt_image(self, input_path, output_path, method='xor'):
        """
        Decrypt an encrypted image
        
        Args:
            input_path (str): Path to encrypted image
            output_path (str): Path to save decrypted image
            method (str): Decryption method (must match encryption method)
        """
        try:
            # Open encrypted image
            img = Image.open(input_path)
            img_array = np.array(img)
            
            print(f"Encrypted image shape: {img_array.shape}")
            
            # Apply decryption based on method
            if method == 'xor':
                decrypted = self._xor_decrypt(img_array)
            elif method == 'swap':
                decrypted = self._swap_decrypt(img_array)
            elif method == 'math':
                decrypted = self._math_decrypt(img_array)
            elif method == 'shuffle':
                decrypted = self._shuffle_decrypt(img_array)
            else:
                raise ValueError("Invalid method. Choose: xor, swap, math, shuffle")
            
            # Save decrypted image
            decrypted_img = Image.fromarray(decrypted.astype('uint8'), 'RGB')
            decrypted_img.save(output_path)
            
            print(f"✓ Image decrypted successfully!")
            print(f"✓ Decrypted image saved at: {output_path}")
            print(f"✓ Method used: {method.upper()}")
            
        except FileNotFoundError:
            print(f"✗ Error: File '{input_path}' not found!")
            sys.exit(1)
        except Exception as e:
            print(f"✗ Error during decryption: {str(e)}")
            sys.exit(1)
    
    # Encryption Methods
    
    def _xor_encrypt(self, img_array):
        """XOR encryption with key-based pattern"""
        encrypted = img_array.copy()
        h, w, c = encrypted.shape
        
        # Generate key pattern
        key_pattern = np.random.randint(0, 256, size=(h, w, c))
        
        # XOR operation
        encrypted = np.bitwise_xor(encrypted, key_pattern)
        
        return encrypted
    
    def _xor_decrypt(self, img_array):
        """XOR decryption (same as encryption for XOR)"""
        return self._xor_encrypt(img_array)
    
    def _swap_encrypt(self, img_array):
        """Swap pixel positions based on key"""
        encrypted = img_array.copy()
        h, w, c = encrypted.shape
        
        # Create index arrays
        indices = np.arange(h * w)
        np.random.shuffle(indices)
        
        # Reshape and swap
        flat = encrypted.reshape(-1, c)
        flat[:] = flat[indices]
        
        return flat.reshape(h, w, c)
    
    def _swap_decrypt(self, img_array):
        """Reverse swap operation"""
        decrypted = img_array.copy()
        h, w, c = decrypted.shape
        
        # Recreate same shuffle pattern
        indices = np.arange(h * w)
        np.random.shuffle(indices)
        
        # Create reverse mapping
        reverse_indices = np.argsort(indices)
        
        # Apply reverse swap
        flat = decrypted.reshape(-1, c)
        flat[:] = flat[reverse_indices]
        
        return flat.reshape(h, w, c)
    
    def _math_encrypt(self, img_array):
        """Mathematical operation encryption"""
        encrypted = img_array.copy().astype(np.int16)
        
        # Apply mathematical operations
        encrypted = (encrypted + self.key) % 256
        encrypted = np.bitwise_xor(encrypted, self.key % 256)
        
        return encrypted
    
    def _math_decrypt(self, img_array):
        """Reverse mathematical operations"""
        decrypted = img_array.copy().astype(np.int16)
        
        # Reverse operations in opposite order
        decrypted = np.bitwise_xor(decrypted, self.key % 256)
        decrypted = (decrypted - self.key) % 256
        
        return decrypted
    
    def _shuffle_encrypt(self, img_array):
        """Shuffle RGB channels and pixels"""
        encrypted = img_array.copy()
        h, w, c = encrypted.shape
        
        # Shuffle channels
        channel_order = np.random.permutation(c)
        encrypted = encrypted[:, :, channel_order]
        
        # Add noise pattern
        noise = np.random.randint(-50, 50, size=(h, w, c))
        encrypted = np.clip(encrypted.astype(np.int16) + noise, 0, 255)
        
        return encrypted
    
    def _shuffle_decrypt(self, img_array):
        """Reverse shuffle operation"""
        decrypted = img_array.copy()
        h, w, c = decrypted.shape
        
        # Remove noise pattern
        noise = np.random.randint(-50, 50, size=(h, w, c))
        decrypted = np.clip(decrypted.astype(np.int16) - noise, 0, 255)
        
        # Reverse channel shuffle
        channel_order = np.random.permutation(c)
        reverse_order = np.argsort(channel_order)
        decrypted = decrypted[:, :, reverse_order]
        
        return decrypted


def print_banner():
    """Print application banner"""
    print("\n" + "="*60)
    print(" "*15 + "IMAGE ENCRYPTION TOOL")
    print(" "*10 + "Pixel Manipulation Based Encryption")
    print("="*60 + "\n")


def print_menu():
    """Print main menu"""
    print("\nChoose an option:")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    print("3. Exit")
    print("-" * 40)


def print_methods():
    """Print available encryption methods"""
    print("\nAvailable Encryption Methods:")
    print("1. XOR - XOR operation with random key pattern")
    print("2. SWAP - Swap pixel positions")
    print("3. MATH - Mathematical operations on pixels")
    print("4. SHUFFLE - Shuffle channels with noise")
    print("-" * 40)


def get_method_choice():
    """Get encryption method from user"""
    methods = {'1': 'xor', '2': 'swap', '3': 'math', '4': 'shuffle'}
    print_methods()
    choice = input("Select method (1-4): ").strip()
    return methods.get(choice, 'xor')


def main():
    """Main function to run the application"""
    print_banner()
    
    # Get encryption key from user
    try:
        key = int(input("Enter encryption key (any number, default 123): ") or "123")
    except ValueError:
        print("Invalid key! Using default key: 123")
        key = 123
    
    encryptor = ImageEncryptor(key)
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            # Encryption
            print("\n--- IMAGE ENCRYPTION ---")
            input_path = input("Enter input image path: ").strip()
            output_path = input("Enter output path for encrypted image: ").strip()
            
            if not output_path:
                base, ext = os.path.splitext(input_path)
                output_path = f"{base}_encrypted{ext}"
            
            method = get_method_choice()
            
            print(f"\nEncrypting image...")
            encryptor.encrypt_image(input_path, output_path, method)
            
        elif choice == '2':
            # Decryption
            print("\n--- IMAGE DECRYPTION ---")
            input_path = input("Enter encrypted image path: ").strip()
            output_path = input("Enter output path for decrypted image: ").strip()
            
            if not output_path:
                base, ext = os.path.splitext(input_path)
                output_path = f"{base}_decrypted{ext}"
            
            method = get_method_choice()
            
            print(f"\nDecrypting image...")
            encryptor.decrypt_image(input_path, output_path, method)
            
        elif choice == '3':
            print("\nThank you for using Image Encryption Tool!")
            print("Exiting...")
            break
            
        else:
            print("\n✗ Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()