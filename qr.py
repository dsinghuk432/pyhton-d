import qrcode

# Data to encode
data = "https://www.youtube.com/"

# Create QR code object
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code. Higher number = larger code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Thickness of the border (minimum is 4)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create and save the image
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")

print("QR Code generated and saved as 'qrcode.png'")
