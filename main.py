import os
from calculator.carbon_calculator import CarbonCalculator
from data_reader.excel_reader import ExcelReader
from reporter.pdf_reporter import ReportGenerator

#---------------------------------------------------------------
def collect_manual_input():
    print("Enter the following data manually:")
    electricity_consumption_gj = float(input("Enter Total Electricity Consumption in Giga Joules (GJ): "))
    gas_consumption_gj = float(input("Enter Total Gas Consumption in Giga Joules (GJ): "))
    fuel_consumption_gj = float(input("Enter Total Fuel Consumption in Giga Joules (GJ): "))
    total_waste_tons = float(input("Enter Total Waste Produced in Tons: "))
    recycling_rate = float(input("Enter Waste Recycle Rate (as a decimal, e.g., 0.8 for 80%): "))
    total_km_traveled = float(input("Enter Total Distance Traveled in Kilometers (KM) [If applicable]: ") or 0)
    fuel_per_100 = float(input("Enter Average Fuel Consumption for 100KM Travel by Car in Liters [If applicable]: ") or 0)
    
    return [electricity_consumption_gj, gas_consumption_gj, fuel_consumption_gj,
            total_waste_tons, recycling_rate, total_km_traveled, fuel_per_100]
#---------------------------------------------------------------





if __name__ == "__main__":
    selected_method = 0
    while selected_method not in [1, 2]:
        selected_method = int(input("Enter 1 to process Excel file or 2 to enter data manually: "))

    if selected_method == 1:
        selected_file = input("Enter file name or enter 1 for default file (Emission-Usage): ")
        if selected_file == "1":
            file_path = 'inputs/Emission-Usage.xlsx'
        else:
            file_path = f'inputs/{selected_file}.xlsx'

        if os.path.exists(file_path):
            reader = ExcelReader(file_path)
            answers = reader.read_input_data()
        else:
            print("File doesn't exist in the 'inputs' folder")
            exit()
    elif selected_method == 2:
        answers = collect_manual_input()
    
    if len(answers) >= 7:
        calculator = CarbonCalculator()
        report_data = {
            "Electricity CO2 Emissions": calculator.electricity(answers[0]),
            "Gas CO2 Emissions": calculator.gas(answers[1]),
            "Fuel CO2 Emissions": calculator.fuel(answers[2]),
            "Waste CO2 Reduction": calculator.waste(answers[3], answers[4]),
            "Business Travel CO2 Emissions": calculator.travel(answers[5], answers[6]),
            "Total CO2 Emissions": sum([
                calculator.electricity(answers[0]),
                calculator.gas(answers[1]),
                calculator.fuel(answers[2]),
                calculator.waste(answers[3], answers[4]),
                calculator.travel(answers[5], answers[6])
            ])
        }

        report = ReportGenerator(report_data)
        report.display_console()
        report.generate_pdf()
        print("Report generated successfully. Find related file in report folder")
    else:
        print("Not enough data provided for calculation.")
