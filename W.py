from tkinter import Tk, Canvas, PhotoImage, Spinbox, Label, Button, messagebox, Listbox, Entry, END, Toplevel

import random
import string


cart_items = {}

#1 untuk gambar
window = Tk()
window.geometry("1280x720")
window.configure(bg="#FFFFFF")
window.title("KASIR")

canvas = Canvas(
    window,
    height=720,
    width=1280,
    
)
canvas.place(x=0, y=0)
bg_image = PhotoImage(file="D:/frame1/bg.png")
canvas.create_image(0, 0, 
anchor="nw", image=bg_image)

image_paths = ["coke.png", "tempeh.png", "tempura.png","sate.png","nugget.png","combo.png"]
images = []
for path in image_paths:
    image = PhotoImage(file="D:/frame1/"+ path)
    images.append(image)

image_objects = []
x_positions = [120, 380,640,900,1160,625,625]  
y_position = [280, 280, 280, 280,280,520,500]  
for i, image in enumerate(images):
    
    image_obj = canvas.create_image(
        x_positions[i], 
        y_position[i], 
        image=image
    )
    image_objects.append(image_obj)
#-1 untuk gamabr

def keranjang(item_spinbox_quantities):
    for item, spinbox in item_spinbox_quantities.items():
        quantity = int(spinbox.get())
        if quantity > 0:
            cart_items[item] = quantity
        elif item in cart_items:
            del cart_items[item]  # Remove item from cart_items
    listbox_keranjang()

def listbox_keranjang():
    cart_listbox.delete(0, END)
    for item, quantity in cart_items.items():
        harga_barang = get_price_per_unit(item) * quantity
        WWW = "Rp {:,.0f}".format(harga_barang)
        cart_listbox.insert(END, f" Item: {item}, Quantity: {quantity}, Harga Barang: {WWW}")

def total_harga():
    total_price = 0
    for item, spinbox in item_spinbox_quantities.items():
        harga_makanan = get_price_per_unit(item)
        jumlah_barang = int(spinbox.get())
        total_price += harga_makanan * jumlah_barang

    if total_price == 0:
        messagebox.showerror("Transaksi gagal", "Tidak ada menu yang dipesan")
    else:
        Rupiah = "Rp {:,.0f}".format(total_price)
        hasil_label.config(text=f"Total Harga: {Rupiah}")
        return total_price


def center_window(window):
    window.update_idletasks()  # Ensure that window attributes are updated
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"+{x}+{y}")

def open_new_window():
    price_total = total_harga ()
    if price_total == None:
        return
     # Create a new window
    new_window = Toplevel()
    center_window(new_window)
    new_window.title("New Window")
    new_window.geometry("300x150")  # Set the size of the window
    new_window.configure(bg="#FFFFFF", bd=0, highlightthickness=0, relief="ridge")  # Configure window attributes
    if new_window == True:
        return
    # Create a label for the entry widget
    label = Label(new_window, text="Enter your name:")
    label.pack(pady=10)  # Add padding to the top

    # Create an entry widget
    entry = Entry(new_window)
    entry.pack()
    
    # Create a label for displaying total price
    Rupiah = "Rp {:,.0f}".format(price_total)   
    total_label = Label(new_window, text=f"Total Harga: {Rupiah}")
    total_label.pack(pady=10)  # Add padding to the bottom
  
    def save_entry_value():
        
        value = entry.get()
    
        if any(char.isdigit() for char in value):
            messagebox.showerror("ok","Masukkan nama anda dengan benar")
        elif not value:
            messagebox.showerror("OK","masukkan nama dengan benar")
        else:
            messagebox.showinfo( "OK",f"Terimakasih!  {value}  atas pesananya silahkan melakukan pembayaran di kasir")
        
        update_cart_and_save_receipt(item_spinbox_quantities, value)
        new_window.destroy()  # Close the window after saving the value

    save_button = Button(new_window, text="Lanjutkan", command=save_entry_value)
    save_button.pack()

#2 tempat simpan
def update_cart_and_save_receipt(item_spinbox_quantities, value):
    keranjang(item_spinbox_quantities)
    name = value
    price_total = total_harga()
    idd=generate_unique_random()

    with open('receipt.txt', 'w') as file:
        file.write("Receipt:\n")
        file.write(f"nama pelanggan: {name}\n")
        file.write(f"NO Pesanan: {idd}\n")
        for item, quantity in cart_items.items():
            price_per_unit = get_price_per_unit(item)
            total_item_price = price_per_unit * quantity
            Rupiah1 = "Rp {:,.0f}".format(total_item_price)
            file.write(f"Item: {item}, Quantity: {quantity},  Price: {Rupiah1}\n")
            Rupiah2 = "Rp {:,.0f}".format(price_total)
        file.write(f"Total Price: {Rupiah2}\n")
#-2

def generate_unique_random():
    characters = string.ascii_letters + string.digits
    unique_codes = set()
    code = '#' + ''.join(random.choice(characters) for _ in range(9))
    unique_codes.add(code)
    return code
    
#1bagian spinbox
#3 batasan input
spinboxsoda = Spinbox(window, from_=0, to=10)
spinboxsoda.place(x=55, y=400)

spinboxtempe = Spinbox(window, from_=0, to=10)
spinboxtempe.place(x=315, y=400)

spinboxtempura = Spinbox(window, from_=0, to=10)
spinboxtempura.place(x=575, y=400)

spinboxsate = Spinbox(window, from_=0, to=10)
spinboxsate.place(x=835, y=400)

spinboxnugeet = Spinbox(window, from_=0, to=10)
spinboxnugeet.place(x=1095, y=400)

spinboxcombo = Spinbox(window, from_=0, to=10)
spinboxcombo.place(x=555, y=610)

spinboxayam = Spinbox(window, from_=0, to=10)
spinboxayam.place(x=500, y=500)
#-1
def get_price_per_unit(item):
    prices = {"Soda": 10000, "Tempeh": 12000, "Tempura": 2500, "Sate": 25000, "Nugeet": 15000,"combo" :55000,"ayam":10000}
    return prices.get(item, 0)
item_spinbox_quantities = {"Soda": spinboxsoda, "Tempeh": spinboxtempe,  "Tempura" : spinboxtempura , "Sate" : spinboxsate ,"Nugeet":spinboxnugeet,"combo" :spinboxcombo ,"ayam":spinboxayam}


#1 bagian tombol
button_image_1 = PhotoImage(file="D:/frame1/button_1.png")
button_hitung = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
     command=lambda: [open_new_window(), update_cart_and_save_receipt(item_spinbox_quantities, "")]
    )
button_hitung.place(x=920, y=550)

button_image_2= PhotoImage(file="D:/frame1/cek.png")

button_cart1 = Button(
image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=lambda: [keranjang(item_spinbox_quantities), total_harga()]
)
button_cart1.place(x=920, y=450)
#-1

#1 untuk label
cart_label = Label(text="keranjang Anda:")
cart_label.place(x=10, y=420)

cart_listbox = Listbox(width=50)
cart_listbox.grid(row=2, column=0, columnspan=12)
cart_listbox.place(x=10, y=440)

hasil_label = Label()
hasil_label.place(x=10, y=580)
hasil_label.config(width=43, height=3)
window.mainloop()


