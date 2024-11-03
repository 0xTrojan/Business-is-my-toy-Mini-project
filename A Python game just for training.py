'''

A simple game whose goal is to challenge players who have the ability to manage their business during a certain period by purchasing real estate and calculating the amount of potential income and taxes during a certain period. 
The winner is the one with a business mind that balances income, sustainability and smoothness. 
It seems simple and easy from the outside, but it is not that simple. It requires a lot of planning, strategy and thinking. 

Enjoy


'''


def calcNetSalary(salary):
    return salary * 0.95  # 5%

def calcMonthIncome(properties):
    incomeRates = {
        "mini market": 100,
        "market": 500,
        "super market": 1000,
        "mall": 5000,
        "mini room": 200,
        "hostel": 700,
        "hotel": 2000
    }
    return sum(properties[name] * incomeRates[name] for name in properties)

def calcTax(properties):
    taxRates = {
        "mini market": 0.1,
        "market": 0.15,
        "super market": 0.2,
        "mall": 0.25,
        "mini room": 0.05,
        "hostel": 0.07,
        "hotel": 0.1
    }
    return sum(properties[name] * taxRates[name] * Costs(name) for name in properties)

def Costs(name):
    costs = {
        "mini market": 1000,
        "market": 5000,
        "super market": 10000,
        "mall": 50000,
        "mini room": 12000,
        "hostel": 20000,
        "hotel": 100000
    }
    return costs[name]

def addProperty(properties, name, quantity):
    if name not in properties:
        properties[name] = 0
    properties[name] += quantity

def TotalProperties(properties):
    return sum(properties.values())

def playTurn(name, salary, totalMoney, properties):
    netSalary = calcNetSalary(salary)
    monthlyIncome = calcMonthIncome(properties)
    totalMoney += netSalary + monthlyIncome

    if totalMoney < salary * 2:
        print(f"{name} is exempt from tax this month because they didn't have a lot of money")
        monthlyTax = 0
    else:
        monthlyTax = calcTax(properties)

    totalMoney -= monthlyTax
    print(f"{name}'s total Money: {totalMoney:.2f}$")
    print(f"{name}'s properties: {properties}")
    print("\n==============================================\n")

    print("Choose a number to buy or type 's' or 'c' to skip:")
    
    print("1: Mini Market: (Cost: 1000$) (Tax: 10%) (Monthly Income: 100$)")
    
    print("2: Market: (Cost: 5000$) (Tax: 15%) (Monthly Income: 500$)")
    
    print("3: Super Market: (Cost: 10000$) (Tax: 20%) (Monthly Income: 1000$)")
    
    print("4: Mall: (Cost: 50000$) (Tax: 25%) (Monthly Income: 5000$)")
    
    print("5: Mini Room: (Cost: 12000$) (Tax: 5%) (Monthly Income: 200$)")
    
    print("6: Hostel: (Cost: 20000$) (Tax: 7%) (Monthly Income: 700$)")
    
    print("7: Hotel: (Cost: 100000$) (Tax: 10%) (Monthly Income: 2000$)")
    
    

    propertyMap = {
        "1": "mini market",
        "2": "market",
        "3": "super market",
        "4": "mall",
        "5": "mini room",
        "6": "hostel",
        "7": "hotel"
    }

    while True:
        try:
            choice = input("Enter number or 's' or 'c': ").strip().lower()

            if choice == 's':
                print(f"\n==============================================\n{name} chose to skip this turn.")
                
                break
            
            elif choice == 'c':
                
                print(f"\n==============================================\n{name} ended their turn.")
                
                break
            elif choice in propertyMap:
                propertyName = propertyMap[choice]
                cost = Costs(propertyName)
                if totalMoney >= cost:
                    quantity = int(input(f"How many of {propertyName} would you like to buy? "))
                    if quantity < 0 or totalMoney < cost * quantity:
                        print("Invalid amount so Try again")
                    else:
                        totalMoney -= cost * quantity
                        addProperty(properties, propertyName, quantity)
                        print(f"Bought {quantity} of {propertyName}.")
                else:
                    print("Not enough money to buy this")
            else:
                print("Please enter a valid number")

        except ValueError:
            print("Please enter a valid number")
        except Exception as e:
            print(f"Error: {e}")

    return totalMoney

years = int(input("Enter the number of years from 1 to 5 only: "))
while years < 1 or years > 5:
    print("Please enter a number between 1 and 5")
    years = int(input("Enter the number of years from 1 to 5 only: "))

goalAmount = int(input("Enter the goal amount minimum 1000$: "))
while goalAmount < 1000:
    print("The goal amount should be at least 1000$.")
    goalAmount = int(input("Enter the goal amount (minimum 1000$): "))

player1Salary = float(input("Enter Player 1 salary (minimum 0$): "))
while player1Salary < 0:
    print("Salary cannot be negative")
    player1Salary = float(input("Enter Player 1 salary minimum 0$: "))

player2Salary = float(input("Enter Player 2 salary (minimum 0$): "))
while player2Salary < 0:
    print("Salary cannot be negative")
    player2Salary = float(input("Enter Player 2 salary (minimum 0$): "))

player1Properties = {
    "mini market": 0,
    "market": 0,
    "super market": 0,
    "mall": 0,
    "mini room": 0,
    "hostel": 0,
    "hotel": 0
}
player2Properties = player1Properties.copy()

player1TotalMoney = 0
player2TotalMoney = 0

for month in range(1, years * 12 + 1):
    print(f"\n--- Month {month} ---")
    player1TotalMoney = playTurn("Player 1", player1Salary, player1TotalMoney, player1Properties)
    if player1TotalMoney >= goalAmount:
        print(f"\nGame Over Player 1 reached the goal")
        break
    player2TotalMoney = playTurn("Player 2", player2Salary, player2TotalMoney, player2Properties)
    if player2TotalMoney >= goalAmount:
        print(f"\nGame Over Player 2 reached the goal")
        break

if player1TotalMoney >= goalAmount or player2TotalMoney >= goalAmount:
    winner = "Player 1" if player1TotalMoney >= goalAmount else "Player 2"
else:
    p1PropertiesTotal = TotalProperties(player1Properties)
    p2PropertiesTotal = TotalProperties(player2Properties)
    
    if p1PropertiesTotal > p2PropertiesTotal:
        winner = "Player 1"
    elif p2PropertiesTotal > p1PropertiesTotal:
        winner = "Player 2"
    else:
        winner = "Player 1" if player1Properties["mini market"] < player2Properties["mini market"] else "Player 2"

print(f"\nThe Winner is {winner} with a total amount of {player1TotalMoney if winner == 'Player 1' else player2TotalMoney:.2f}$.")
