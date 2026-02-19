# raspi-thermal-printer

[python-escpos - Python library to manipulate ESC/POS Printers](https://python-escpos.readthedocs.io/en/latest/)

## Initial Setup

```bash
sudo apt update && sudo apt full-upgrade -y
sudo apt install -y libusb-1.0-0 libusb-1.0-0-dev
sudo apt install code
python -m pip install --upgrade pip
echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="0fe6", ATTRS{idProduct}=="811e", GROUP="lp", MODE="0660"' | sudo tee /etc/udev/rules.d/99-thermal-printer.rules > /dev/null
```

## Hardware

- **Camera**: UGREEN 2K Webcam for PC Ultra HD 1080P Computer Webcam with Microphone, PC Camera with Privacy Cover, USB Web Camera for Streaming, Conference, Video Calling, Zoom, Skype, Teams, FaceTime, Grey
- **Compute**: Raspberry Pi 4 Model B 2 GB (BCM2711)
- **Display**: ELECROW 10.1 Inch Portable Monitor - IPS Capacitive Monitor with HD VGA Port，1920x1080P LCD Display Built-in Dual Speakers VESA Mount for Raspberry Pi 5/4/3, PS Xbox, Windows 11/10/8/7
- **Printer**: [Rongta POS Printer RP332](https://www.rongtatech.com/rp332-3inch-thermal-receipt-printer_p15.html)
    - `lsusb -v -d 0fe6:811e`; ID 0fe6:811e ICS Advent Parallel Adapter

## Resources used when learning

- [Mouse Control With Just a Webcam and Python. Here’s How It Works. By Divya Rameshkumar Patel](https://medium.com/@divya330369/built-a-minority-report-style-interface-with-just-a-webcam-and-python-heres-how-it-works-7d2e61d7360d)
- [I Turned AI Into a Tiny Fortune-Telling Machine with Raspberry Pi. By Cassie Serendipity](https://medium.com/@cassie_serendipity/i-turned-ai-into-a-tiny-fortune-telling-machine-with-raspberry-pi-a33255704b3a)
