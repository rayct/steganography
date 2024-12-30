# Steganography Encoder and Decoder

This project provides a simple tool to encode and decode secret messages within image files using steganography. The application features a user-friendly graphical user interface (GUI) built with Tkinter, and uses the Pillow library for image processing.

## Features

1. **Encode Messages**:
   - Hide a secret text message within an image file (supports `.png` and `.bmp` formats).
   - Save the encoded image with the hidden message.

2. **Decode Messages**:
   - Extract the hidden message from an encoded image file.

3. **User-Friendly Interface**:
   - Easy-to-use GUI for encoding and decoding messages.

## Requirements

- Python 3.x
- The following Python libraries:
  - `Pillow` (for image manipulation): Install using `pip install pillow`
  - `Tkinter` (for GUI): Comes pre-installed with most Python distributions.

## Installation

1. Clone the repository or download the source code:

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Install the required dependencies:

   ```bash
   pip install pillow
   ```

3. Run the application:

   ```bash
   python steganography_ui.py
   ```

## Usage

### Encoding a Message

1. Launch the application by running `steganography_ui.py`.
2. Click on the **Encode Message** button.
3. Select an image file (must be `.png` or `.bmp`).
4. Enter the message to encode in the provided text box.
5. Save the encoded image to a desired location.
6. The image will now contain the hidden message.

### Decoding a Message

1. Launch the application by running `steganography_ui.py`.
2. Click on the **Decode Message** button.
3. Select the encoded image file.
4. The hidden message will be displayed in a pop-up window.

## How It Works

### Encoding

The program hides the message by manipulating the least significant bits (LSBs) of the pixel values in the image. Each character in the message is converted to an 8-bit binary representation, and these bits are embedded sequentially into the LSBs of the red, green, and blue color channels of the image pixels.

### Decoding

The program extracts the LSBs from the red, green, and blue color channels of the image pixels. These bits are reassembled to reconstruct the binary representation of the hidden message, which is then converted back into text.

## Supported Formats

- Input Images: `.png`, `.bmp`
- Encoded Images: Saved as `.png` or `.bmp`

## Limitations

- The length of the message is limited by the number of pixels in the image. For example, an image with 100x100 pixels can hide approximately 33,333 characters.
- The program does not support images with transparency or formats like `.jpeg` that use lossy compression.

## Examples

### Encoding Example

1. Original Image:
   ![original](example_images/original.png)

2. Encoded Image:
   ![encoded](example_images/encoded.png)

3. Hidden Message: "This is a secret message."

### Decoding Example

1. Encoded Image:
   ![encoded](example_images/encoded.png)

2. Decoded Message: "This is a secret message."

## Security Note

This tool uses basic steganography techniques and does not provide strong security. If you need to protect the hidden message, consider encrypting it before encoding.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests to improve the project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- The Pillow library for image processing.
- Tkinter for providing an easy-to-use GUI toolkit.


