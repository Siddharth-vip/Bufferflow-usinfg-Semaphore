import threading
import time
from queue import Queue

# Semaphore for controlling access to loading and unloading operations
loading_semaphore = threading.Semaphore(3)
unloading_semaphore = threading.Semaphore(3)

# Queues for import and export operations
import_queue = Queue(maxsize=5)
export_queue = Queue(maxsize=5)

# Lock for synchronizing access to print statements
print_lock = threading.Lock()

def load_goods():
    with loading_semaphore:
        time.sleep(2)  # Simulate time taken to load goods
        import_queue.put('Goods')
        with print_lock:
            print("Goods loaded. Current import queue size:", import_queue.qsize())

def unload_goods():
    with unloading_semaphore:
        time.sleep(2)  # Simulate time taken to unload goods
        if not export_queue.empty():
            export_queue.get()
            with print_lock:
                print("Goods unloaded. Current export queue size:", export_queue.qsize())
        else:
            with print_lock:
                print("Export queue is empty. Nothing to unload.")

def import_goods():
    with loading_semaphore:
        time.sleep(2)  # Simulate time taken to import goods
        import_queue.put('Imported Goods')
        with print_lock:
            print("Goods imported. Current import queue size:", import_queue.qsize())

def export_goods():
    with unloading_semaphore:
        time.sleep(2)  # Simulate time taken to export goods
        export_queue.put('Exported Goods')
        with print_lock:
            print("Goods exported. Current export queue size:", export_queue.qsize())

def quit_system():
    print("Quitting the system...")
    print(f"Final import queue size: {import_queue.qsize()}")
    print(f"Final export queue size: {export_queue.qsize()}")
    exit()

def user_interface():
    while True:
        print("\nLogistics System Menu:")
        print("1. Load Goods")
        print("2. Unload Goods")
        print("3. Import Goods")
        print("4. Export Goods")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            threading.Thread(target=load_goods).start()
        elif choice == '2':
            threading.Thread(target=unload_goods).start()
        elif choice == '3':
            threading.Thread(target=import_goods).start()
        elif choice == '4':
            threading.Thread(target=export_goods).start()
        elif choice == '5':
            quit_system()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    user_interface()
