# Image Encryption Tool

Welcome to the Image Encryption Tool! This Python program allows users to encrypt and decrypt images using pixel manipulation. By applying a basic mathematical operation (XOR) to each pixel, the program ensures that the image can be securely encrypted and later decrypted using the same key.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Description

The Image Encryption Tool encrypts images by manipulating the pixel values. It uses the XOR operation with a user-defined key to encrypt and decrypt each pixel in the image. This simple yet effective method ensures that the image can be securely encoded and later decoded with the same key.

## Features

- Encrypt images using pixel manipulation.
- Decrypt images that were encrypted using the same key.
- Supports any image format supported by the Pillow library (e.g., PNG, JPEG).

## Requirements

- Python 3.x
- Pillow library

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Hun33er/PRODIGY_WD_02/image-encryption-tool.git
```

2. Navigate to the project directory:

```bash
cd image-encryption-tool
```

3. Install the required library:

```bash
pip install pillow
```

## Usage

Run the program using Python:

```bash
python image_encryption_tool.py
```

Follow the prompts to encrypt or decrypt an image:

1. Type `encrypt` to encrypt an image or `decrypt` to decrypt an image.
2. Enter the path to the input image.
3. Enter the path to save the output image.
4. Enter the encryption/decryption key (an integer).

### Example

```plaintext
Welcome to the Image Encryption Tool!
Type 'encrypt' to encrypt an image or 'decrypt' to decrypt an image: encrypt
Enter the path to the input image: input.png
Enter the path to save the encrypted image: encrypted.png
Enter the encryption/decryption key (an integer): 123
Image encrypted and saved to encrypted.png
```

```plaintext
Welcome to the Image Encryption Tool!
Type 'encrypt' to encrypt an image or 'decrypt' to decrypt an image: decrypt
Enter the path to the input image: encrypted.png
Enter the path to save the decrypted image: decrypted.png
Enter the encryption/decryption key (an integer): 123
Image decrypted and saved to decrypted.png
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to create a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Developed by [Hun33er] as part of the Prodigy Info Tech Internship.

---

Feel free to customize the README with your personal information, repository URL, and any additional details you find relevant.
