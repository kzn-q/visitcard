import qrcode
from PIL import Image

# URL of your personal profile webpage
url = "https://yourwebsite.com"  # Replace with your real URL

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("profile_qr.png")

print("✅ QR code generated and saved as profile_qr.png")
