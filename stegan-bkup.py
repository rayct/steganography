import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

# Core Steganography Functions
def encode_message(image_path, message, output_path):
    image = Image.open(image_path)
    encoded_image = image.copy()
    width, height = image.size

    message += "<EOF>"  # Mark the end of the message
    message_bits = ''.join([format(ord(char), '08b') for char in message])

    pixels = list(encoded_image.getdata())
    new_pixels = []

    bit_index = 0
    for pixel in pixels:
        r, g, b = pixel[:3]
        if bit_index < len(message_bits):
            r = (r & ~1) | int(message_bits[bit_index])
            bit_index += 1
        if bit_index < len(message_bits):
            g = (g & ~1) | int(message_bits[bit_index])
            bit_index += 1
        if bit_index < len(message_bits):
            b = (b & ~1) | int(message_bits[bit_index])
            bit_index += 1
        new_pixels.append((r, g, b) + pixel[3:])

    encoded_image.putdata(new_pixels)
    encoded_image.save(output_path)


def decode_message(image_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())

    bits = ""
    for pixel in pixels:
        r, g, b = pixel[:3]
        bits += str(r & 1)
        bits += str(g & 1)
        bits += str(b & 1)

    message = ""
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        char = chr(int(byte, 2))
        if char == "<EOF>":
            break
        message += char

    return message

# Tkinter UI Functions
def select_image():
    filename = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.bmp")])
    return filename

def save_image():
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("BMP files", "*.bmp")])
    return filename

def encode_ui():
    input_image = select_image()
    if not input_image:
        return

    def encode_and_save():
        message = message_entry.get("1.0", tk.END).strip()
        output_image = save_image()
        if not output_image:
            return

        try:
            encode_message(input_image, message, output_image)
            messagebox.showinfo("Success", "Message encoded and saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to encode: {e}")

    encode_window = tk.Toplevel(root)
    encode_window.title("Encode Message")

    tk.Label(encode_window, text="Enter your message:").pack(pady=5)
    message_entry = tk.Text(encode_window, width=40, height=10)
    message_entry.pack(pady=5)

    tk.Button(encode_window, text="Encode and Save", command=encode_and_save).pack(pady=10)

def decode_ui():
    input_image = select_image()
    if not input_image:
        return

    try:
        message = decode_message(input_image)
        decode_window = tk.Toplevel(root)
        decode_window.title("Decoded Message")

        tk.Label(decode_window, text="Decoded Message:").pack(pady=5)
        message_box = tk.Text(decode_window, width=40, height=10)
        message_box.pack(pady=5)
        message_box.insert(tk.END, message)
        message_box.config(state=tk.DISABLED)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to decode: {e}")

# Tkinter GUI Setup
root = tk.Tk()
root.title("Steganography Tool")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

welcome_label = tk.Label(frame, text="Steganography Encoder and Decoder", font=("Helvetica", 16))
welcome_label.pack(pady=10)

tk.Button(frame, text="Encode Message", command=encode_ui, width=20).pack(pady=5)
tk.Button(frame, text="Decode Message", command=decode_ui, width=20).pack(pady=5)

root.mainloop()

