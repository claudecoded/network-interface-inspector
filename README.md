# Network Interface Inspector 🌐🔍

A simple Python tool that automatically scans your computer to find all active network interfaces (like Wi-Fi, Ethernet, or Virtual adapters) and displays their current IPv4 addresses.

---

## How to Use This Project

Follow these steps to download and run the application on your computer:

### 1. Download the Files
First, you need to get the files onto your computer:
* Click the green **"Code"** button at the top of this GitHub page.
* Select **"Download ZIP"**.
* Extract the downloaded ZIP file into a folder of your choice.

<img width="670" height="435" alt="image" src="https://github.com/user-attachments/assets/5218efbf-ded2-48c1-9a62-8d9d1d5c6dc2" />

### 2. Open Your Terminal
Open the command line terminal inside the extracted folder:
* **Windows:** Hold `Shift`, right-click inside the folder, and select **"Open PowerShell window here"** or **"Open in Terminal"**.
* **Mac / Linux:** Open your Terminal app and navigate to the folder using the `cd` command (e.g., `cd Downloads/network-interface-inspector`).

### 3. Install Requirements & Run the Tool
Choose the commands below based on your Operating System. These commands use advanced Python flags to ensure the system recognizes Python even if your standard `pip` command fails.

#### 🪟 On Windows
```bash
python -m pip install -r requirements.txt
python main.py
```

#### 🍏 On macOS / 🐧 On Linux
```bash
python3 -m pip install -r requirements.txt
python3 main.py
```

Once executed, the program will clear your screen and present a clean list of all identified network interfaces along with their respective IP addresses.

---

## Troubleshooting
If you receive a **"Python not found"** error, make sure Python is installed on your machine and that you checked the box **"Add Python to PATH"** during its installation process.
