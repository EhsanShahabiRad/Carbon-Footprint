class CarbonCalculator:
    
  def __init__(self, GJ_TO_KWH=277.778, Emission_Electricity=0.0005, 
                 Emission_Gas=0.055, Emission_Fuel=2.32):
        self.GJ_TO_KWH = GJ_TO_KWH
        self.Emission_Electricity = Emission_Electricity
        self.Emission_Gas = Emission_Gas
        self.Emission_Fuel = Emission_Fuel
    
  def electricity(self, electricity_consumption_gj):
        electricity_consumption_kwh = electricity_consumption_gj * 1000 * self.GJ_TO_KWH
        co2_electricity = electricity_consumption_kwh * self.Emission_Electricity
        return co2_electricity