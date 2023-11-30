import csv

medal_data = []

class MedalPayoutData: 
    def __init__(self, place, growth_rate, area, country, noc, rank, g_payout, total_payout, year):
        self.place = place
        self.growth_rate = growth_rate
        self.area = area
        self.country = country
        self.noc = noc
        self.rank = rank
        self.g_payout = g_payout
        self.total_payout = total_payout
        self.year = year
        
        
    def print_medal_details(self):
        print(f"Place: {self.place}")
        print(f"Growth Rate: {self.growth_rate}")
        print(f"Area: {self.area}")
        print(f"Country: {self.country}")
        print(f"rank: {self.rank}")
        print(f"Gold Medal Payout: {self.g_payout}")
        print(f"Total Payout: {self.total_payout}")
        print(f"Gold Medal Payout Data Year: {self.year}")

    
    def read_medalPayout_data_csv(file_path):
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            headers = next(csv_reader)
            
            for row in csv_reader:
                if len(row) < len(headers):
                    continue
                
                data = MedalPayoutData(
                    place=row[0],
                    growth_rate=row[2], 
                    area=row[3],
                    country=row[4],
                    noc=row[5],
                    rank=row[15],
                    g_payout=row[16],
                    total_payout=row[17],
                    year=row[19]
                )
                medal_data.append(data)
            
        return medal_data