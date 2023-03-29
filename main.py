# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
A quick response (QR) code is a barcode that a digital device can easily scan.
It encodes data as a series of pixels in a square grid.
Tracking information about supply chains using QR codes is very useful in marketing and advertising campaigns.
The International Organization for Standardization certified QR codes as a global standard in 2000.
They are an improvement over the previous uni-dimensional barcodes (ISO).
QR codes were developed in the 1990s to provide more information than a regular barcode.
They were created by Denso Wave, a Toyota affiliate, to monitor the production of vehicles.

In contrast to barcodes, which need a beam of light to bounce off the parallel lines,
QR codes may be scanned digitally by devices like smartphones.

QR codes are used in cryptocurrency systems to enable digital payments,such as when displaying a Bitcoin address.
QR codes are also often used to communicate site URLs to mobile devices.

"""

"""
__author__ = "Rob Knight, Gavin Huttley, and Peter Maxwell"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Rob Knight", "Peter Maxwell", "Gavin Huttley",
                    "Matthew Wakefield"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Rob Knight"
__email__ = "rob@spot.colorado.edu"
__status__ = "Production"
"""


def qr_code():
    import segno
    import tkinter as tk
    from tkinter import ttk
    from tkinter.messagebox import showinfo

    root = tk.Tk()
    root.geometry('400x680')
    root.configure(bg='lightblue')
    root.resizable(False, False)
    root.title('QR_Generator')

    # place a label on the root window
    tk.Label(root, text="Welcome to QR Generator Software").pack()

    def qr_generator(text):
        # Use a breakpoint in the code line below to debug your script.
        print(text)
        qr_tag = segno.make_qr(text)
        qr_tag.save("qr_text.png", scale=10)
        # print(text)

    def qr_generator_url(url):
        print(url)
        video = segno.make(url)
        video.save('qr_url.png',  scale=10)

    def qr_generator_personal_detail(name, email, phone):
        from segno import helpers
        qrcode = helpers.make_mecard(name=name, email=email, phone=phone)
        qrcode.designator
        '3-L'
        # Some params accept multiple values, like email, phone, url
        # qrcode = helpers.make_mecard(name='Shittu Olumide',
        #                             email=('me@example.com', 'email@example.com'),
        #                            url=['http://www.example.com', 'https://example.come/~olu'])
        qrcode.save('qr_personal.png', scale=10)

    def qr_generator_wifi(ssid, password):
        """
        How to Make a QR Code for a WiFi Configuration
        We  can also use the Segmo library to create a QR code for wifi configuration.
        The segno.helpers module offers factory methods to generate standard QR codes for encoding
        geographic coordinates, vCards and MeCards, WIFI setups, and EPC QR Codes.
        The error correction level "L" is utilized in creating QR codes.
        If possible, we will apply the higher error correction level without altering the QR Code version.
        The density of the QR code picture decreases with decreasing error correction level,
        which enhances minimum printing size. The more damage it can withstand before losing its ability to be read, the greater the error correction level.
        The optimal balance between density and toughness for general marketing use is Level L or Level M.
        In industrial settings where maintaining a clean or undamaged QR code may be difficult, Level Q and
        Level H are the best options.
        """
        from segno import helpers

        qrcode = helpers.make_wifi(ssid=ssid, password=password, security='WPA')

        qrcode.designator
        '3-L'

        print(ssid, password)
        qrcode.save('qr_wifi_access.png', scale=10)

    # check button and calling method
    agreement = tk.StringVar()

    def ch_qr_generator_url():
        print("hi im here")
        tk.Label(root, text="Enter URL:").pack(padx=10, pady=10, fill='x',expand=True)
        url = tk.StringVar()
        tk.Entry(root, textvariable=url).pack(padx=10, pady=10, fill='x',expand=True)
        print(url.get())

        ttk.Button(root, text="Submit", command=lambda: qr_generator_url(url.get())).pack(padx=10, pady=10, fill='x',expand=True)

    def ch_qr_generator():
        tk.Label(root, text="Enter Text:").pack(padx=10, pady=10,fill='x',expand=True)
        text = tk.StringVar()
        tk.Entry(root, textvariable=text).pack(padx=10, pady=10,fill='x',expand=True)

        tk.Button(root, text="Submit", command=lambda: qr_generator(text.get())).pack(padx=10, pady=10,fill='x',expand=True)

    def ch_qr_generator_wifi():
        tk.Label(root, text="Enter WiFi SSID:").pack(padx=10, pady=10,fill='x',expand=True)
        ssid = tk.StringVar()
        tk.Entry(root, textvariable=ssid).pack(padx=10, pady=10,fill='x',expand=True)

        tk.Label(root, text="Enter WiFi Password:").pack(padx=10, pady=10,fill='x',expand=True)
        pswd = tk.StringVar()
        tk.Entry(root, textvariable=pswd).pack(padx=10, pady=10,fill='x',expand=True)
        tk.Button(root, text="Submit", command=lambda: qr_generator_wifi(ssid.get(), pswd.get())).pack(padx=10, pady=10,fill='x',expand=True)

    def ch_qr_generator_personal_detail():
        #ttk.Frame(root)
        ttk.Label(root, text="Enter Name:").pack(padx=10, pady=10,fill='x',expand=True)
        name = tk.StringVar()
        ttk.Entry(root, textvariable=name).pack(padx=10, pady=10,fill='x',expand=True)

        ttk.Label(root, text="Enter Email:").pack(padx=10, pady=10,fill='x',expand=True)
        email = tk.StringVar()
        ttk.Entry(root, textvariable=email).pack(padx=10, pady=10,fill='x',expand=True)

        ttk.Label(root, text="Enter Phone:").pack(padx=10, pady=10,fill='x',expand=True)
        phone = tk.StringVar()
        ttk.Entry(root, textvariable=phone).pack(padx=10, pady=10,fill='x',expand=True)
        print("deepak",name, email.get(), phone.get())

        ttk.Button(root, text="Submit", command=lambda: qr_generator_personal_detail(name.get(), email.get(), phone.get())).pack(padx=10, pady=10,fill='x',expand=True)

    def agreement_changed():
        print(agreement.get())
        if int(agreement.get()) == 1:
            ch_qr_generator_url()
            print("hello sir")
        elif int(agreement.get()) == 2:
            ch_qr_generator()
        elif int(agreement.get()) == 3:
            ch_qr_generator_wifi()
        elif int(agreement.get()) == 4:
            ch_qr_generator_personal_detail()

    ttk.Checkbutton(root, text='URL Encoding to QR',variable=agreement, onvalue=1, offvalue=0).pack(padx=10, pady=10,fill='x',expand=True)
    ttk.Checkbutton(root, text='Text Encoding to QR', variable=agreement,onvalue=2, offvalue=0).pack(padx=10, pady=10,fill='x',expand=True)
    ttk.Checkbutton(root, text='WiFi credentials Encoding to QR', variable=agreement, onvalue=3, offvalue=0).pack(padx=10, pady=10, fill='x', expand=True)
    ttk.Checkbutton(root, text='Personal card Encoding to QR', variable=agreement, onvalue=4, offvalue=0).pack(padx=10,pady=10,fill='x',expand=True)

    tk.Button(root, text="Save", command=lambda:agreement_changed()).pack(padx=10, pady=10,fill='x',expand=True)

    root.mainloop()


if __name__ == '__main__':
    print("Hi")
    qr_code()
