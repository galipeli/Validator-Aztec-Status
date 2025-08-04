import requests
import json
import sys
from rich.console import Console
from rich.table import Table
from rich.text import Text

# Initialize rich console, forcing compatibility with limited color terminals
# This ensures the output works on most VPS environments.
console = Console(force_terminal=True, color_system="truecolor", force_jupyter=False)

# Read addresses from file
try:
    with open("address.txt", "r", encoding="utf-8") as f:
        addresses = [line.strip().lower() for line in f if line.strip()]
except FileNotFoundError:
    console.print("[bold red]Error:[/bold red] The file 'address.txt' was not found.")
    sys.exit(1)

if not addresses:
    console.print("[bold yellow]Warning:[/bold yellow] 'address.txt' is empty. Please add validator addresses.")
    sys.exit(0)

# Fetch validator data
try:
    validators_url = "https://dashtec.xyz/api/validators"
    validators_resp = requests.get(validators_url)
    validators_resp.raise_for_status()  # Raise an exception for bad status codes
    validators_data = validators_resp.json()
    validators = validators_data.get("validators", [])
except requests.exceptions.RequestException as e:
    console.print(f"[bold red]Error:[/bold red] Failed to fetch validator data from {validators_url}. Details: {e}")
    sys.exit(1)

# Create a dictionary mapping address -> validator info
validator_map = {v["address"].lower(): v for v in validators}

# Fetch queue data
try:
    queue_url = "https://dashtec.xyz/api/validators/queue"
    queue_resp = requests.get(queue_url)
    queue_resp.raise_for_status()
    queue_data = queue_resp.json()
    queue_list = queue_data.get("validatorsInQueue", [])
except requests.exceptions.RequestException as e:
    console.print(f"[bold red]Error:[/bold red] Failed to fetch queue data from {queue_url}. Details: {e}")
    sys.exit(1)

# Create a dictionary mapping address -> queue position
queue_positions = {}
for item in queue_list:
    addr = item.get("address", "").lower()
    index_str = item.get("index", "")
    if index_str.startswith("#") and index_str[1:].isdigit():
        queue_positions[addr] = int(index_str[1:])

# Create a rich table for output
table = Table(title="[bold underline blue]Validator Aztec Status[/bold underline blue]", show_header=True, header_style="bold magenta")
table.add_column("No.", style="dim", width=5)
table.add_column("Address", style="dim", no_wrap=True)
table.add_column("Status", justify="left")
table.add_column("Details", justify="left")

# Process and add data to the table
for i, addr in enumerate(addresses, 1):
    addr_short = f"{addr[:10]}...{addr[-10:]}"
    v = validator_map.get(addr)
    
    if v and v.get("status") == "Validating":
        attestation = v.get("attestationSuccess", "N/A")
        status_text = Text("Validating", style="bold green")
        details_text = Text(f"Attestation Success: {attestation}", style="green")
        table.add_row(str(i), addr_short, status_text, details_text)
    elif addr in queue_positions:
        position = queue_positions[addr]
        status_text = Text("Queued", style="bold yellow")
        details_text = Text(f"Position: #{position}", style="yellow")
        table.add_row(str(i), addr_short, status_text, details_text)
    else:
        status_text = Text("Not Found", style="bold red")
        details_text = Text("Status unknown or not in queue", style="red")
        table.add_row(str(i), addr_short, status_text, details_text)

# Print the final table
console.print(table)
