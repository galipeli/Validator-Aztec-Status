# Aztec Validator Status Checker

This script allows you to easily check the status of your Aztec validator addresses and display the results in a clean, tabular format directly in your terminal.

## 🔧 How to Use `cek.py`

Follow the steps below to set up and run the script:

### 1. Clone the Repository

```bash
git clone https://github.com/galipeli/Validator-Aztec-Status.git
cd Validator-Aztec-Status
```

### 2. Install Dependencies

Make sure you have Python installed, then install the required libraries:

```bash
pip install -r requirements.txt
```

### 3. Add Your Validator Addresses

Create a file named `address.txt` in the project root directory, and add your validator addresses—**one address per line**.

**Example:**

```
0x1a2b...
0x1122...
0x55aa...
```

### 4. Run the Script

To check your validator statuses, run:

```bash
python cek.py
```

The script will output a neatly formatted table showing the current status of each validator address.

---

## 📷 Example Output

<img width="984" height="894" alt="image" src="https://github.com/user-attachments/assets/b14badcd-b55f-4f42-a6e0-e4e8135f90c5" />

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
