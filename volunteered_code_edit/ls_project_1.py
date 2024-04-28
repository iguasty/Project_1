# This is my edited version attempting to add fileio
# Editted by Isaac Guastaferro 
# Last edit 4/27/2024

""" Luke Scovel

This program will generate a computer class.
The computer class will have a motherboard, cpu, gpu, ram, and storage.
The motherboard will have a cpu socket, ram slots, BIOS version, and connected components.
The cpu will have a socket, cores, threads, and clock speed.
The gpu will have a present status, cores, clock speed, and vram.
The ram will have a clock speed, capacity, type, and number.
The storage will have a capacity, type, speed, and operating system version.

The check compatibility method will check if the components are compatible with the motherboard.
The provide power method will give power to all components.
The BIOS method will access the BIOS of the motherboard.
The overclock method will increase the clock speed of the component.
The update OS method will update the operating system.


Design (pseudocode): 
computer class
    __init__(self, motherboard, cpu, gpu, ram, storage):]
    
    attributes for motherboard:
        cpu socket (LGA 1151, AM4, etc.)
        ram slots (number of ram slots)
        BIOS version
        connected components (cpu, gpu, ram, storage)
    behavior for motherboard:
        check compatibility
        provide power
        BIOS

    attributes for cpu:
        socket (LGA 1151, AM4, etc.)
        cores (number of cores)
        threads (number of threads)
        clock speed (GHz)
    behavior for cpu:
        overclock

    attributes for gpu:
        present (T/F)
        cores (CUDA cores)
        clock speed (MHz)
        vram (GB)
    behavior for gpu:
        overclock

    attributes for ram:
        clock speed
        capacity
        type (DDR3, DDR4, etc.)
        number
    behavior for ram:
        overclock

    attributes for storage:
        capacity
        type (SSD or HDD)
        speed
        operating system version
    behavior for storage:
        update OS

    relationships:
        mother board is connected to cpu, gpu, ram, and storage (nervous system)
        cpu is the brain of the computer
        gpu is sometimes optional (cpu may have integrated graphics)
        ram is short term memory
        storage is long term memory

        overclock is a method that increases the clock speed of the component
        BIOS is a method that accesses the BIOS of the motherboard
        check compatibility is a method that checks if the components are compatible with the motherboard
        provide power gives power to all components
        update OS is a method that updates the operating system

    Testing:
    A few tests that I would run would be to check if i get the expected output
    when I call the methods. For example:
    >>> motherboard = Motherboard("am4", 4, 1.3, CPU("am4"", 6, 12, 4.4))
    >>> motherboard.check_compatibility()
    True
    >>> motherboard.bios()
    
    BIOS Version: 1.3

    Motherboard Info:
    CPU Socket: am4
    RAM Slots: 4
    
    CPU Info:
    CPU Socket: am4
    Cores: 6
    Threads: 12
    Clock Speed: 4.4 GHz

"""

class Motherboard:
    """ This class will generate a motherboard/computer """

    def __init__(self, cpu_socket, ram_slots, bios_version, cpu):
        """ This method will initialize the class """
        
        self.power = False
        self.cpu_socket = cpu_socket
        self.ram_slots = ram_slots
        self.bios_version = bios_version
        self.cpu = cpu

    def check_compatibility(self):
        """ This method will check if the components are compatible with the motherboard
         (will eventually check more than just cpu probably) """
        if self.cpu_socket == self.cpu.socket:
            return True
        else:
            return False

    def toggle_power(self):
        """ This method will toggle power to all components """
        if self.power is False:
            self.power = True
            self.cpu.power = True
        else:
            self.power = False
            self.cpu.power = False

    def bios(self):
        """ This method will access the BIOS of the motherboard """
    
        print(f"\nBIOS Version: {self.bios_version}\n")
        print("Motherboard Info:")
        print(f"CPU Socket: {self.cpu_socket}")
        print(f"RAM Slots: {self.ram_slots}")
        print("\nCPU Info:")
        print(f"CPU Socket: {self.cpu.socket}")
        print(f"Cores: {self.cpu.cores}")
        print(f"Threads: {self.cpu.threads}")
        print(f"Clock Speed: {self.cpu.clock_speed} GHz")
        print(f"Power: {self.cpu.power}")
    
    # [IG] added write() method 
    def write(self) -> None:
        output_file = open("motherboard", "w")
        output_file.write(str(self.power) + "\n")
        output_file.write(str(self.cpu_socket) + "\n")
        output_file.write(str(self.ram_slots) + "\n")
        output_file.write(str(self.bios_version) + "\n")
        output_file.write(str(self.cpu) + "\n")
        output_file.close()

class CPU:
    """ This class will generate a CPU """

    def __init__(self, socket, cores, threads, clock_speed):
        """ This method will initialize the class """

        self.power = False
        self.socket = socket
        self.cores = cores
        self.threads = threads
        self.clock_speed = clock_speed

    def overclock(self):
        """ This method will increase the clock speed of the CPU """
        
    # [IG] added write() method
    def write(self) -> None:
        output_file = open(self, "w")
        output_file.write(str(self.power) + "\n")
        output_file.write(str(self.socket) + "\n")
        output_file.write(str(self.cores) + "\n")
        output_file.write(str(self.clock_speed) + "\n")
        output_file.close()
        
def readMotherboard(filename: str) -> Motherboard:
    input_file = open(filename, "r")
    lines = input_file.readlines()
    
    object_Motherboard = Motherboard()
    object_Motherboard.power = lines[0]
    object_Motherboard.cpu_socket = lines[1]
    object_Motherboard.ram_slots = lines[2]
    object_Motherboard.bios_version = lines[3]
    object_Motherboard.cpu = lines[4]
    input_file.close()
    return object_Motherboard

def readCPU(filename: str) -> CPU:
    input_file = open(filename, "r")
    lines = input_file.readlines()
    
    object_CPU = CPU()
    object_CPU.power = lines[0]
    object_CPU.socket = lines[1]
    object_CPU.cores = lines[2]
    object_CPU.clock_speed = lines[3]
    input_file.close()
    return object_CPU

def main():
    """ This function will generate a computer class 
    and show a menu to the user """

    print("Hello! Welcome to the computer setup menu!")
    print("Please enter the following information:")
    print("\nMotherboard Info:")
    cpu_socket = input("Enter the CPU socket of the motherboard (eg. am4): ")
    ram_slots = int(input("Enter the number of RAM slots: "))
    bios_version = input("Enter the BIOS version: ")
    print("\nCPU Info:")
    cpu_socket_cpu = input("Enter the CPU socket of the CPU (eg. am4): ")
    cores = int(input("Enter the number of cores: "))
    threads = int(input("Enter the number of threads: "))
    clock_speed = float(input("Enter the clock speed (GHz): "))

    my_comp = Motherboard(cpu_socket, ram_slots, bios_version, CPU(cpu_socket_cpu, cores, threads, clock_speed))

    print("\nHello! Welcome to the computer application main menu!")
    
    while True:
        print("\nMenu:")
        print("1. Check compatibility")
        print("2. Turn on computer")
        print("3. Access BIOS")
        print("4. Quit")
        print("5. Save Motherboard") # [IG]
        
        choice = input("Select an option (1/2/3/4): ")
        
        if choice == '1':
            if my_comp.check_compatibility():
                print("The components are compatible!")
            else:
                print("The components are not compatible!")
        elif choice == '2':
            my_comp.toggle_power()
        elif choice == '3':
            my_comp.bios()
        elif choice == '4':
            print("Goodbye!")
            break
        elif choice == '5': # [IG]
            my_comp.write()
            print("Saved Motherboard file!")
        elif choice == '6': # [IG]
            readMotherboard("motherboard")
            print("opened Motherboard file!")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
