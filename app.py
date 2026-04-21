from time import sleep
from database import create_tables
from services import (
    create_customer,
    get_all_customers,
    delete_customer_by_id,
    update_customer,
    search_customer,
    get_total_revenue
)
from validators import (
    get_valid_name,
    get_valid_text,
    get_valid_number
)
from ui import (
    menu,
    header,
    show_table,
    show_revenue,
    success,
    error
)


def main():
    create_tables()
    while True:
        menu()
        try:
            choice = int(input("Choose: "))
            if choice == 1:
                header("Customers")
                show_table(get_all_customers())
            elif choice == 2:
                header("New Customer")
                name = get_valid_name()
                service = get_valid_text("Service")
                price = get_valid_number("Price: ")
                create_customer(name, service, price)
                success("Customer created!")
            elif choice == 3:
                header("Delete Customer")
                cid = int(input("ID: "))
                if delete_customer_by_id(cid):
                    success("Deleted!")
                else:
                    error("Customer not found!")
            elif choice == 4:
                header("Update Customer")
                cid = int(input("ID: "))
                name = get_valid_name()
                service = get_valid_text("Service")
                price = get_valid_number("Price: ")
                if update_customer(cid, name, service, price):
                    success("Updated!")
                else:
                    error("Customer not found!")
            elif choice == 5:
                header("Search")
                name = input("Name: ")
                show_table(search_customer(name))
            elif choice == 6:
                header("Revenue")
                show_revenue(get_total_revenue())
            elif choice == 7:
                header("Exiting...")
                break
            else:
                error("Invalid option!")
        except ValueError:
            error("Invalid input!")
        except KeyboardInterrupt:
            print()
            header("Exiting...")
            break
        sleep(1)


if __name__ == "__main__":
    main()
