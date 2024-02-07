Image Encryption Using AES and Visual Cryptography

Description:
This project implements a novel image encryption algorithm based on AES (Advanced Encryption Standard) and Visual Cryptography. The implementation follows the IEEE paper titled "A Novel Image Encryption Algorithm using AES and Visual Cryptography". The encryption process involves converting an image into ciphertext using AES encryption combined with Visual Cryptography techniques.

Technology Stack:

- Language: Python 3.11
- Development Environment: Spyder
- Libraries: base64, hashlib, Crypto.Cipher, Crypto.Random, numpy, cv2, sklearn.linear_model

Instructions:

1. Clone or download the repository.
2. Open Spyder and navigate to the folder containing the project files.
3. Run the `Encryption.py` file to convert an image into ciphertext.
4. Use the `mykey.txt` file located in the `keys` folder for encryption.
5. The ciphertext and key split images will be generated in the `ToBeSent for Decryption` folder.
6. Run the `Decryption.py` file to obtain the original image named as `DecryptedImg`.

Additional Notes:

- This implementation encrypts and decrypts images using a combination of AES encryption and Visual Cryptography, providing an added layer of security to image data.
- The code is organized into Python scripts for easy execution and understanding.
- Users are encouraged to explore and modify the code according to their requirements.
