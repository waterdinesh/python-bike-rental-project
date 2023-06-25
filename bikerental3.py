import tkinter as tk
from PIL import Image, ImageTk

class Bike:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 50

class BikeRentalShop:
    def __init__(self):
        self.bikes = [
            Bike("Pulsar", 20),
            Bike("Apache", 15),
            Bike("Shine", 10),
            Bike("Spender", 5)
        ]

    def displayBikes(self):
        display_label.config(text="Available bikes for rent:\n" + "\n".join([f"{bike.name}: {bike.quantity} qty" for bike in self.bikes]))

    def rentBike(self, bike_name, quantity):
        bike = next((b for b in self.bikes if b.name == bike_name), None)
        if bike is None:
            display_label.config(text="Invalid bike selection.")
        elif quantity <= 0:
            display_label.config(text="Enter a positive value greater than zero.")
        elif quantity > bike.quantity:
            display_label.config(text="Bike quantity not available.")
        else:
            bike.quantity -= quantity
            total_price = bike.price * quantity
            display_label.config(text="Total price: {} Rs\nBike: {}\nOrder qty: {}\nTotal bikes remaining: {} qty".format(total_price, bike.name, quantity, bike.quantity))

def display_bikes():
    bike_rental_shop.displayBikes()

def rent_bike():
    bike_name = bike_selection.get()
    quantity = quantity_entry.get()
    if not quantity.isdigit():
        display_label.config(text="Enter a positive integer value for quantity.")
        return
    quantity = int(quantity)
    bike_rental_shop.rentBike(bike_name, quantity)
    quantity_entry.delete(0, tk.END)  # Clear the quantity entry after renting a bike

def exit_program():
    root.destroy()

def handle_selection(*args):
    selected_image = bike_selection.get()
    if selected_image == "Pulsar":
        bike_label.config(image=bike_photo)
    elif selected_image == "Apache":
        bike_label.config(image=bike_photo2)
    elif selected_image == "Shine":
        bike_label.config(image=bike_photo3)
    elif selected_image == "Spender":
        bike_label.config(image=bike_photo4)

bike_rental_shop = BikeRentalShop()

root = tk.Tk()
root.title("Bike Rental Shop")
root.geometry("500x400")

root.configure(bg="light blue")

display_button = tk.Button(root, text="Display bikes", command=display_bikes, bg="yellow")
display_button.pack()

bike_selection_label = tk.Label(root, text="Select a bike:", bg="light blue")
bike_selection_label.pack()

# Load and display the bike image
bike_image2 = Image.open("./bike_image.jpg").resize((100, 100))
bike_image = Image.open("./pulsar200rs.jpg").resize((100, 100))
bike_image3 = Image.open("./shine.jpg").resize((100, 100))
bike_image4 = Image.open("./spendar.jpg").resize((100, 100))

#bike_image4 = Image.open("C:/Users/1/OneDrive/Desktop/python/spendar.jpg").resize((100, 100))
# Convert the
# Convert the images to Tkinter PhotoImage objects
bike_photo = ImageTk.PhotoImage(bike_image)
bike_photo2 = ImageTk.PhotoImage(bike_image2)
bike_photo3 = ImageTk.PhotoImage(bike_image3)
bike_photo4 = ImageTk.PhotoImage(bike_image4)

bike_selection = tk.StringVar(root)
bike_selection.set(bike_rental_shop.bikes[0].name)  # Set the default bike selection to the first bike

bike_dropdown = tk.OptionMenu(root, bike_selection, *[bike.name for bike in bike_rental_shop.bikes])
bike_dropdown.pack()

quantity_label = tk.Label(root, text="Enter the required bike quantity:", bg="light blue")
quantity_label.pack()

quantity_entry = tk.Entry(root)
quantity_entry.pack()

rent_button = tk.Button(root, text="Rent a bike", command=rent_bike, bg="yellow")
rent_button.pack()

display_label = tk.Label(root, bg="light blue")
display_label.pack()

exit_button = tk.Button(root, text="Exit", command=exit_program, bg="yellow")
exit_button.pack()

bike_label = tk.Label(root, image=bike_photo)  # Create a label to display the selected bike image
bike_label.pack()

# Bind the handle_selection function to the variable trace
bike_selection.trace("w", handle_selection)

root.mainloop()



