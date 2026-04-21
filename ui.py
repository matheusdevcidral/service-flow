from rich import print
from rich.panel import Panel
from rich.table import Table


def header(text):
    print(Panel(text.center(30), width=35, style="cyan"))


def success(msg):
    print(f"[green]{msg}[/]")


def error(msg):
    print(f"[red]{msg}[/]")


def menu():
    header("SERVICE FLOW")
    print("1. Show Customers")
    print("2. Register Customer")
    print("3. Delete Customer")
    print("4. Update Customer")
    print("5. Search Customer")
    print("6. Total Revenue")
    print("7. Exit")
    print("-" * 35)


def show_table(data):
    if not data:
        print("[yellow]No data found.[/]")
        return
    table = Table(title="Customers")
    table.add_column("ID")
    table.add_column("Name", style="cyan")
    table.add_column("Service", style="magenta")
    table.add_column("Price", justify="right", style="green")
    table.add_column("Created")
    for row in data:
        table.add_row(
            str(row[0]),
            row[1],
            row[2],
            f"R$ {row[3]:.2f}",
            row[4]
        )
    print(table)


def show_revenue(total):
    table = Table(title="Revenue")
    table.add_column("Total", justify="center", style="green")
    table.add_row(f"R$ {total:.2f}")
    print(table)
