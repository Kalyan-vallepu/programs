import tkinter as tk
from openpyxl import load_workbook

class RoomDetails:
    def __init__(self, root, floor, room, go_back):
        self.root = root
        self.floor = floor
        self.room = room
        self.go_back = go_back
        self.show_room_details()

    def show_room_details(self):
        """Display tenant details for a selected room."""
        self.clear_window()

        # Title label
        tk.Label(self.root, text=f"Details for Floor {self.floor} - Room {self.room}", font=("Arial", 14, "bold")).pack(pady=10)

        # Display loading message
        loading_label = tk.Label(self.root, text="Loading details, please wait...", font=("Arial", 12))
        loading_label.pack(pady=10)

        # Load data from Excel
        try:
            wb = load_workbook("kalyan.xlsx")
            sheet = wb.active

            data_found = False
            for row in sheet.iter_rows(values_only=True):
                # Assuming columns: Floor, Room, Name, Age, Place, Advance, Rent
                if row[0] == self.floor and row[1] == self.room:
                    details = f"Name: {row[2]}\nAge: {row[3]}\nPlace: {row[4]}\nAdvance: {row[5]}\nRent: {row[6]}"
                    tk.Label(self.root, text=details, justify="left").pack(pady=10)
                    data_found = True
                    break

            if not data_found:
                tk.Label(self.root, text="No data available for this room.").pack()

        except FileNotFoundError:
            tk.Label(self.root, text="Error: Data file not found. Please ensure the file is present.").pack()
        except Exception as e:
            tk.Label(self.root, text=f"An error occurred: {str(e)}").pack()

        # Hide loading message and show back button
        loading_label.destroy()
        tk.Button(self.root, text="Back", command=self.go_back, width=20, height=2).pack(pady=10)

    def clear_window(self):
        """Clear all widgets from the current window."""
        for widget in self.root.winfo_children():
            widget.destroy()

# Example of how to use this class:
if __name__ == "__main__":
    def go_back():
        print("Going back to the previous screen.")

    root = tk.Tk()
    room_details = RoomDetails(root, floor=2, room=3, go_back=go_back)
    root.geometry("400x400")
    root.mainloop()
