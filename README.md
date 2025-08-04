# Aztec Validator Status Checker

This script allows you to easily check the status of your Aztec validator addresses and display the results in a clean, tabular format directly in your terminal.

## 🔧 How to Use `cek.py`

Follow the steps below to set up and run the script:

---

### 1. Clone the Repository

```bash
git clone https://github.com/galipeli/Validator-Aztec-Status.git
cd Validator-Aztec-Status
```

---

### 2. Set Up Virtual Environment (Recommended)

To avoid system-level Python issues (like `externally-managed-environment`), create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
```

If you're on Windows, use:
```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

Once the virtual environment is active, install the required Python libraries:

```bash
pip install -r requirements.txt
```

---

### 4. Add Your Validator Addresses

Create a file named `address.txt` in the project root directory, and add your validator addresses — **one per line**.

**Example:**

```
0x1a2b...
0x1122...
0x55aa...
```

---

### 5. Run the Script

```bash
python cek.py
```

The script will display a table showing the current status of each validator address.

---

## 📷 Example Output

> Replace the image below with a screenshot of your actual terminal output.

![Example Output](images/output.png)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

