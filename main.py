import os
from calculator.carbon_calculator import CarbonCalculator
from data_reader.excel_reader import ExcelReader

if (__name__ == "__main__"):
    selected_method = 0
    while(selected_method != 1 and selected_method != 2):
        selected_method = int( input("Enter 1 to process Excel file or 2 to enter data manualy: "))
    
    if(selected_method == 1):
        selected_file = input("Enter file name or enter 1 for default file (Emission-Usage): ")
        if(selected_file == "1"):
            file_path = 'inputs/Emission-Usage.xlsx'
        else: 
             file_path = f'inputs/{selected_file}.xlsx'    

        if (os.path.exists(file_path)):
                reader = ExcelReader(file_path)
                answers = reader.read_input_data()
                if len(answers) >= 7:
                     calculator = CarbonCalculator()
                     total_co2_emissions = calculator.total_emissions(
                     electricity_consumption_gj=answers[0],
                     gas_consumption_gj=answers[1],
                     fuel_consumption_gj=answers[2],
                     total_waste_tons=answers[3],
                     recycling_rate=answers[4],
                     total_km_traveled=answers[5],
                     fuel_per_100=answers[6] 
            )
        
                     print(f"Total CO2 Emissions: {total_co2_emissions} kgCO2")
                else:
                     print("Not enough data provided in Excel file for calculation.")
        else:
              print("File doesn't exist in the 'input' folder ")
    else:
        electricity_consumption_gj =""
        gas_consumption_gj =""
        fuel_consumption_gj =""
        total_waste_tons =""
        recycling_rate =""
        total_km_traveled =""

        while(electricity_consumption_gj =="" or gas_consumption_gj =="" or fuel_consumption_gj ==""
              or total_waste_tons =="" or recycling_rate =="" or total_km_traveled ==""
                or fuel_per_100 ==""):
                     electricity_consumption_gj = float(input("Enter Total Electricity Consumption/ Giga jul: "))
                     gas_consumption_gj = float(input("Enter Total Gas Consumption/ Giga jul: "))
                     fuel_consumption_gj = float(input("Enter Total Fuel Consumption/ Giga jul: "))
                     total_waste_tons = float(input("Enter Total Waste Produced/ Tons: "))
                     recycling_rate = float(input("Enter Waste Recycle Rate: "))
                     total_km_traveled = float(input("Enter Total Distance Traveled/ KM: "))
                     fuel_per_100 = float(input("Enter Average Fuel Consumption For 100km Travel By Car/ Liter: "))
        
        calculator = CarbonCalculator()
        total_co2_emissions = calculator.total_emissions(
                electricity_consumption_gj,
                gas_consumption_gj,
                fuel_consumption_gj,
                total_waste_tons,
                recycling_rate,
                total_km_traveled,
                fuel_per_100 
            )
        print(f"Total CO2 Emissions: {total_co2_emissions} kgCO2")