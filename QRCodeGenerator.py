import qrcode

for i in range(1, 4):
    input_data = f"http://127.0.0.1:8000/room/{i}"

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(f'qrcode{i}.png')
