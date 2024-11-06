import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import ImageTk, Image

UPI_ID = "9346798475@fbl"  # Updated to include the correct UPI ID

def generate_qr_code(cost):
    qr_data = f"upi://pay?pa={UPI_ID}&pn=YourName&mc=1234&tid=000000000000&tr=1234567890&tn=Payment%20for%20your%20purchase&am={cost}&cu=INR&url="
    qr = qrcode.make(qr_data)
    qr.save("payment_qr.png")

def show_qr():
    try:
        quantity = int(entry_quantity.get())
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        cost = quantity * 5
        generate_qr_code(cost)
        
        # Show the QR Code
        qr_img = Image.open("payment_qr.png")
        qr_img = qr_img.resize((200, 200), Image.Resampling.LANCZOS)  # Updated here
        qr_img = ImageTk.PhotoImage(qr_img)
        
        qr_label.config(image=qr_img)
        qr_label.image = qr_img
        label_cost.config(text=f"Total Cost: Rs. {cost}")
        payment_button.config(state=tk.NORMAL)
    except ValueError as ve:
        messagebox.showerror("Input Error", "Please enter a valid integer quantity.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def payment_done():
    # In a real application, you'd need to verify payment status using a payment gateway API
    quantity = entry_quantity.get()
    # Simulating payment confirmation
    payment_confirmed = True  # This should be replaced with actual payment verification logic

    if payment_confirmed:
        messagebox.showinfo("Payment Status", "Payment Done Successfully!")
        messagebox.showinfo("Product Dispensed", f"{quantity} Products Dispensed!")
    else:
        messagebox.showerror("Payment Status", "Payment Failed or Not Verified!")

# Create the main window
root = tk.Tk()
root.title("Automatic Vending Machine")

# Set the window size and color scheme
root.geometry("400x500")
root.configure(bg='#FFC0CB')  # Pink background

# Quantity input
label_quantity = tk.Label(root, text="Enter Quantity of Products:", bg='#FFC0CB', fg='#FFFFFF', font=("Arial", 14))
label_quantity.pack(pady=20)

entry_quantity = tk.Entry(root, font=("Arial", 14))
entry_quantity.pack(pady=10)

# Button to generate QR
generate_button = tk.Button(root, text="Generate QR Code", command=show_qr, bg='#FF69B4', fg='#FFFFFF', font=("Arial", 12))
generate_button.pack(pady=10)

# Label to show the cost
label_cost = tk.Label(root, text="", bg='#FFC0CB', fg='#FFFFFF', font=("Arial", 14))
label_cost.pack(pady=10)

# Label to display the QR Code
qr_label = tk.Label(root, bg='#FFC0CB')
qr_label.pack(pady=10)

# Payment Button
payment_button = tk.Button(root, text="Mark Payment as Done", command=payment_done, bg='#FF69B4', fg='#FFFFFF', font=("Arial", 12), state=tk.DISABLED)
payment_button.pack(pady=20)

# Run the application
root.mainloop()
