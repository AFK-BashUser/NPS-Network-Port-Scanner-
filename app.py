import tkinter as tk
from scanner.threaded_scanner import threaded_scan

# launching the GUI -->

def launch_gui():

    # function will run when [ Start Scan ] button is clicked -->

    def start_scan():
        host = host_entry.get() # Get host/IP from the input
        start_port = int(start_entry.get()) # Get starting port
        end_port = int(end_entry.get()) # Get ending port

        result_text.delete(1.0, tk.END) # Clearing previous results in the text box

        ports = threaded_scan(host, start_port, end_port) # Run the threaded port scan and store the list of open ports
        result_text.insert(tk.END, f"Open ports: {ports}") # Displaying the open ports in the text box

    window = tk.Tk() # Creating the main application window
    window.title("Network Port Scanner (Threaded Only)") # Setting  the window title

    # Creating label and input fields for host/IP -->

    tk.Label(window, text="Host/IP:").grid(row=0, column=0)
    host_entry = tk.Entry(window)
    host_entry.grid(row=0, column=1)

    tk.Label(window, text="Start Port:").grid(row=1, column=0)
    start_entry = tk.Entry(window)
    start_entry.grid(row=1, column=1)

    tk.Label(window, text="End Port:").grid(row=2, column=0)
    end_entry = tk.Entry(window)
    end_entry.grid(row=2, column=1)

    tk.Button(window, text="Start Scan", command=start_scan).grid(row=3, column=0, columnspan=2)

    # Text box to display the scan results -->

    result_text = tk.Text(window, height=15, width=50)
    result_text.grid(row=4, column=0, columnspan=2)

    window.mainloop() # Starting the tkinter event loop to show the window
