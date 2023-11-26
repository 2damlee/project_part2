import csv

gdp_data = []

class GdpData: 
    # need to check the year
    def __init__(self, nation, noc, idc_name, idc_code, yearly_data): 
        self.nation = nation
        self.noc = noc
        self.idc_name = idc_name
        self.idc_code = idc_code
        self.yearly_data = yearly_data
    
    
    def print_gdp_details(self):
        print(f"Country: {self.nation} ({self.noc})")
        print(f"Indicator: {self.idc_name} ({self.idc_code})")
        print("Yearly Data:")
        for year, value in self.yearly_data.items():
            print(f"{year}: {value}")
    
    def read_gdp_csv(file_path):
        
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for _ in range(4):
                next(csv_reader, None)
            headers = next(csv_reader)
            
            for row in csv_reader:
                yearly_data = {headers[i]: row[i] for i in range(4, len(headers))}
                data = GdpData(
                    nation=row[0],
                    noc=row[1],
                    idc_name=row[2],
                    idc_code=row[3],
                    yearly_data=yearly_data
                )
                gdp_data.append(data)
                