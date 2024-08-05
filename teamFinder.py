# Create a list of schools
schools = [
    "Abilene Christian", "Air Force", "Akron", "Alabama", "Alabama A&M", "Alabama State", "Albany (NY)", "Alcorn State", 
    "American", "Appalachian State", "Arizona", "Arizona State", "Arkansas", "Arkansas State", "Arkansas-Pine Bluff", 
    "Army", "Auburn", "Austin Peay", "Ball State", "Baylor", "Bellarmine", "Belmont", "Bethune-Cookman", "Binghamton", 
    "Boise State", "Boston College", "Boston University", "Bowling Green State", "Bradley", "Brigham Young", "Brown", 
    "Bryant", "Bucknell", "Buffalo", "Butler", "Cal Poly", "Cal State Bakersfield", "Cal State Fullerton", 
    "Cal State Northridge", "California", "California Baptist", "Campbell", "Canisius", "Central Arkansas", 
    "Central Connecticut State", "Central Michigan", "Charleston Southern", "Charlotte", "Chattanooga", 
    "Chicago State", "Cincinnati", "Clemson", "Cleveland State", "Coastal Carolina", "Colgate", "College of Charleston", 
    "Colorado", "Colorado State", "Columbia", "Connecticut", "Coppin State", "Cornell", "Creighton", "Dartmouth", 
    "Davidson", "Dayton", "Delaware", "Delaware State", "Denver", "DePaul", "Detroit Mercy", "Drake", "Drexel", 
    "Duke", "Duquesne", "East Carolina", "East Tennessee State", "Eastern Illinois", "Eastern Kentucky", 
    "Eastern Michigan", "Eastern Washington", "Elon", "Evansville", "Fairfield", "FDU", "Florida", "Florida A&M", 
    "Florida Atlantic", "Florida Gulf Coast", "Florida International", "Florida State", "Fordham", "Fresno State", 
    "Furman", "Gardner-Webb", "George Mason", "George Washington", "Georgetown", "Georgia", "Georgia Southern", 
    "Georgia State", "Georgia Tech", "Gonzaga", "Grambling", "Grand Canyon", "Green Bay", "Hampton", "Harvard", 
    "Hawaii", "High Point", "Hofstra", "Holy Cross", "Houston", "Houston Christian", "Howard", "Idaho", "Idaho State", 
    "Illinois", "Illinois State", "Illinois-Chicago", "Incarnate Word", "Indiana", "Indiana State", "Iona", "Iowa", 
    "Iowa State", "IUPUI", "Jackson State", "Jacksonville", "Jacksonville State", "James Madison", "Kansas", 
    "Kansas City", "Kansas State", "Kennesaw State", "Kent State", "Kentucky", "La Salle", "Lafayette", "Lamar", 
    "Le Moyne", "Lehigh", "Liberty", "Lindenwood", "Lipscomb", "Little Rock", "Long Beach State", 
    "Long Island University", "Longwood", "Louisiana", "Louisiana State", "Louisiana Tech", "Louisiana-Monroe", 
    "Louisville", "Loyola (IL)", "Loyola (MD)", "Loyola Marymount", "Maine", "Manhattan", "Marist", "Marquette", 
    "Marshall", "Maryland", "Maryland-Baltimore County", "Maryland-Eastern Shore", "Massachusetts", 
    "Massachusetts-Lowell", "McNeese State", "Memphis", "Mercer", "Merrimack", "Miami (FL)", "Miami (OH)", 
    "Michigan", "Michigan State", "Middle Tennessee", "Milwaukee", "Minnesota", "Mississippi", 
    "Mississippi State", "Mississippi Valley State", "Missouri", "Missouri State", "Monmouth", "Montana", 
    "Montana State", "Morehead State", "Morgan State", "Mount St. Mary's", "Murray State", "Navy", "NC State", 
    "Nebraska", "Nevada", "Nevada-Las Vegas", "New Hampshire", "New Mexico", "New Mexico State", "New Orleans", 
    "Niagara", "Nicholls State", "NJIT", "Norfolk State", "North Alabama", "North Carolina", "North Carolina A&T", 
    "North Carolina Central", "North Dakota", "North Dakota State", "North Florida", "North Texas", "Northeastern", 
    "Northern Arizona", "Northern Colorado", "Northern Illinois", "Northern Iowa", "Northern Kentucky", 
    "Northwestern", "Northwestern State", "Notre Dame", "Oakland", "Ohio", "Ohio State", "Oklahoma", 
    "Oklahoma State", "Old Dominion", "Omaha", "Oral Roberts", "Oregon", "Oregon State", "Pacific", "Penn State", 
    "Pennsylvania", "Pepperdine", "Pittsburgh", "Portland", "Portland State", "Prairie View", "Presbyterian", 
    "Princeton", "Providence", "Purdue", "Purdue Fort Wayne", "Queens (NC)", "Quinnipiac", "Radford", "Rhode Island", 
    "Rice", "Richmond", "Rider", "Robert Morris", "Rutgers", "Sacramento State", "Sacred Heart", "Saint Francis (PA)", 
    "Saint Joseph's", "Saint Louis", "Saint Mary's (CA)", "Saint Peter's", "Sam Houston", "Samford", "San Diego", 
    "San Diego State", "San Francisco", "San Jose State", "Santa Clara", "Seattle", "Seton Hall", "Siena", 
    "South Alabama", "South Carolina", "South Carolina State", "South Carolina Upstate", "South Dakota", 
    "South Dakota State", "South Florida", "Southeast Missouri State", "Southeastern Louisiana", "Southern", 
    "Southern California", "Southern Illinois", "SIU Edwardsville", "Southern Indiana", "Southern Methodist", 
    "Southern Mississippi", "Southern Utah", "St. Bonaventure", "St. John's (NY)", "St. Thomas", "Stanford", 
    "Stephen F. Austin", "Stetson", "Stonehill", "Stony Brook", "Syracuse", "Tarleton State", "TCU", "Temple", 
    "Tennessee", "Tennessee State", "Tennessee Tech", "Tennessee-Martin", "Texas", "Texas A&M", "Texas A&M-Commerce", 
    "Texas A&M-Corpus Christi", "Texas Southern", "Texas State", "Texas Tech", "Texas-Rio Grande Valley", 
    "The Citadel", "Toledo", "Towson", "Troy", "Tulane", "Tulsa", "UAB", "UC Davis", "UC Irvine", "UC Riverside", 
    "UC San Diego", "UC Santa Barbara", "UCF", "UCLA", "UNC Asheville", "UNC Greensboro", "UNC Wilmington", 
    "UT Arlington", "Utah", "Utah State", "Utah Tech", "Utah Valley", "UTEP", "UTSA", "Valparaiso", "Vanderbilt", 
    "Vermont", "Villanova", "Virginia", "Virginia Commonwealth", "VMI", "Virginia Tech", "Wagner", "Wake Forest", 
    "Washington", "Washington State", "Weber State", "West Virginia", "Western Carolina", "Western Illinois", 
    "Western Kentucky", "Western Michigan", "Wichita State", "William & Mary", "Winthrop", "Wisconsin", "Wofford", 
    "Wright State", "Wyoming", "Xavier", "Yale", "Youngstown State"
]

# Sort the schools alphabetically
schools.sort()

# Create a dictionary with school names as keys and their ranks as values
school_ranks = {school: rank for rank, school in enumerate(schools, 1)}

# Function to get the rank of a school
def get_rank(school):
    return school_ranks.get(school, "School not found")

# Main program
if __name__ == "__main__":
    while True:
        school = input("Enter a school name (or type 'exit' to quit): ")
        if school.lower() == "exit":
            break
        else:
            rank = get_rank(school)
            print(f"The rank of {school} is {rank}")
