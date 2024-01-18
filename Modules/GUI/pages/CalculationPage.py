from tkinter import messagebox, ttk

# GUI for Calculation page
class CalculationPage:
    def __init__(self, app):
        self.app = app
        self.driver = "Walter White"
    def show(self):
        self.app.destroy_previous_widgets()
        label_calculation = ttk.Label(self.app.root, text="Calculation:")
        label_calculation.pack(pady=10)

        label_driver = ttk.Label(self.app.root, text=f"Driver: {self.app.selectedDriver.getNameSurname()}")#.getNameSurname()
        label_driver.pack(pady=10)

        label_truck = ttk.Label(self.app.root, text=f"Truck: {self.app.selectedTruck.getBrandModel()}")#.getBrandModel()
        label_truck.pack(pady=10)

        label_payload = ttk.Label(self.app.root, text=f"Payload: {self.app.selectedPayload.getName()}")#.getName()
        label_payload.pack(pady=10)

        label_from = ttk.Label(self.app.root, text=f"From: {self.app.fromDestination.getName()}")
        label_from.pack(pady=10)

        label_to = ttk.Label(self.app.root, text=f"To: {self.app.toDestination.getName()}")
        label_to.pack(pady=10)
    
        prevPage = ttk.Button(self.app.root, text="Previous", command=self.app.selectDestination.show)
        prevPage.pack(pady=10)
    
        calculate_button = ttk.Button(self.app.root, text="Calculate", command=self.app.calculate)
        calculate_button.pack(pady=10)

    def showCalculations(self):
        if (self.app.selectedPayload.type == "PayloadRegular" and self.app.selectedPayload.weight > self.app.selectedTruck.capacity):
            error_label = ttk.Label(self.app.root, text="Error: Payload weighs more than the available capacity of a selected truck.\n"
                                    "Please choose proper truck.")
            error_label.config(foreground="red")
            error_label.pack(pady=10)
        else:
            label_distance = ttk.Label(self.app.root, text=f"Distance: {self.app.distance}")
            label_distance.pack(pady=10)

            label_fuelPrice = ttk.Label(self.app.root, text=f"Fuel Price: {self.app.fuelPrice}")
            label_fuelPrice.pack(pady=10)

            label_driverTime = ttk.Label(self.app.root, text=f"Driver Time: {self.app.driverTime}")
            label_driverTime.pack(pady=10)

            label_driverSalary = ttk.Label(self.app.root, text=f"Driver Salary: {self.app.driverSalary}")
            label_driverSalary.pack(pady=10)
    

  