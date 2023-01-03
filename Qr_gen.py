import qrcode

# Create the QR code image
img = qrcode.make('This is the data that will be encoded in the QR code')

# Save the QR code image to a file
with open('qr_code.png', 'wb') as f:
    img.save(f)
