import csv

# The below code is just an example. you can change or add methods or vaiables 
athletes = []

class Athlete:
    
    def __init__(self, id, name, sex, age, height, weight, team, noc, games, year, season, city, sport, event, medal):
        self.id = id
        self.name = name
        self.sex = sex
        self.age = age
        self.height = height
        self.weight = weight
        self.team = team
        self.noc = noc
        self.games = games
        self.year = year
        self.season = season
        self.city = city
        self.sport = sport
        self.event = event
        self.medal = medal
        
    def print_athlete_details(self):
        print(f"Athlete ID: {self.id}, Name: {self.name}, Sport: {self.sport}, Event: {self.event}, Medal: {self.medal}")
        
    # read CSV file and create instances
    def read_athletes_csv(file_path):
        
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                athelete = Athlete(
                    id=row[0],
                    name=row[1],
                    sex=row[2],
                    age=row[3] if row[3] else None,
                    height=row[4] if row[4] else None,
                    weight=row[5] if row[5] else None,
                    team=row[6],
                    noc=row[7],
                    games=row[8],
                    year=row[9],
                    season=row[10],
                    city=row[11],
                    sport=row[12],
                    event=row[13],
                    medal=row[14]
                )
                
                athletes.append(athelete)
        return athletes
    
    
