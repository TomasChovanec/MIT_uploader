from intelhex import IntelHex
import serial
import time
from serial.tools.list_ports_windows import comports
import sys


def flash(com, path):
    ih = IntelHex(path)
    with serial.Serial(com, 115200, timeout=1) as ser:
        ser.write(b'A')
        if ser.read(1) != b'B':
            return -1

        ser.write(b'I')
        if ser.read(3) != b'\x1e\x98\x01':
            return -2

        ser.write(b'F')
        if ser.read(1) != b'H':
            return -3

        num_bytes = len(ih)
        num_pages = num_bytes // 256 + 1
        pagesize = 256

        for i in range(num_pages):
            ser.write(((i >> 8) & 255).to_bytes(1, "big"))
            ser.write((i & 255).to_bytes(1, "big"))

            for j in range(pagesize):
                ser.write(ih[i * pagesize + j].to_bytes(1, "big"))
                if j % 20 == 0:
                    time.sleep(0.001)

            if ser.read(1) != b'Z':
                return -4

        ser.write(0xFF.to_bytes(1, "big"))
        ser.write(0xFF.to_bytes(1, "big"))
        ser.write(b'Q')
        ser.write(b'Q')
        return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Find COM port with education board
    comport = None
    for portDescription in serial.tools.list_ports_windows.comports():
        if portDescription.vid == 1027 and portDescription.pid == 24597:
            comport = portDescription[0]
            print(f"Education board found on {comport}")
            break

    if comport is None:
        raise Exception("Education board not found. Please check USB and power supply connection")
    else:
        try:
            # path = r"c:\Users\Lenovo L450\Desktop\FrenGP\MIT\cvičení\7seg_display\sedmseg\sedmseg\Debug\sedmseg.hex"
            hex_path = sys.argv[1]
            print(f"File to flash: {hex_path}")
            if flash(comport, hex_path) == 0:
                print("Flashing OK")
                sys.exit(0)
            else:
                raise Exception("Flashing failed, please check if board is in bootloader mode.")
        except IndexError:
            raise Exception("No hex file path specified. Please specify path to hex file as argument.")
