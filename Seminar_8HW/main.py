from os import path

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8"):
        pass


def read_records():
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []


def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data")


def add_new_contact():
    global last_id
    array = ["surname", "name", "patronymic", "phone_number"]
    string = ""
    for i in array:
        string += input(f"Enter {i}: ") + " "
    last_id += 1

    with open(file_base, "a", encoding="utf-8") as f:
        f.write(f"{last_id} {string}\n")


def search_record():
    search_query = input("Enter search query: ")
    found_records = []
    for record in all_data:
        if search_query.lower() in record.lower():
            found_records.append(record)
    if found_records:
        print("Found records:")
        print(*found_records, sep="\n")
    else:
        print("No records found.")


def change_record():
    record_id = input("Enter record ID to change: ")
    for i, record in enumerate(all_data):
        if record.startswith(record_id):
            new_data = input("Enter new data: ")
            all_data[i] = f"{record_id} {new_data}"
            with open(file_base, "w", encoding="utf-8") as f:
                f.write("\n".join(all_data))
            print("Record changed successfully.")
            return
    print("Record not found.")


def delete_record():
    record_id = input("Enter record ID to delete: ")
    for i, record in enumerate(all_data):
        if record.startswith(record_id):
            del all_data[i]
            with open(file_base, "w", encoding="utf-8") as f:
                f.write("\n".join(all_data))
            print("Record deleted successfully.")
            return
    print("Record not found.")


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change a record\n"
                       "5. Delete a record\n"
                       "6. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search_record()
            case "4":
                change_record()
            case "5":
                delete_record()
            case "6":
                play = False
            case _:
                print("Try again!\n")


main_menu()