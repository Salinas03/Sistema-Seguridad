import wmi

def obtener_numero_serie():
    # Connect to the WMI service
    c = wmi.WMI()

    # Query for the serial number
    numero_serie = None
    for bios in c.Win32_BIOS():
        numero_serie = bios.SerialNumber.strip()
        break
    return numero_serie
