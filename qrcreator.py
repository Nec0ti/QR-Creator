import tkinter as tk
from tkinter import filedialog
import qrcode

def generate_qr_code():
    data = entry_data.get()
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if data and filename:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        lbl_status.config(text=f"QR Code saved to '{filename}' Succesfully.")

# Create UI
root = tk.Tk()
root.title("Create QR Code")

# Input
entry_data = tk.Entry(root, width=50)
entry_data.pack(pady=10)

# Create QR code button
btn_generate = tk.Button(root, text="Create QR Code", command=generate_qr_code)
btn_generate.pack(pady=5)

# Status Tag
lbl_status = tk.Label(root, text="")
lbl_status.pack(pady=5)

root.mainloop()
