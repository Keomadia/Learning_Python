import random


MIN_BET = 1
MAX_BET = 200
MAX_LINES = 3

ROWS = 3
COLS = 3

symbol_count = {
   "A": 2,
   "B": 3,
   "C": 2,
   "D": 5
}

symbol_values = {
   "A": 5,
   "B": 4,
   "C": 3,
   "D": 2
}

def check_winnings(columns,lines,bet,values):
   winnings = 0
   winning_lines = []
   for line in range(lines):
      symbol = columns[0][line]
      for column in columns:
          symbol_to_check = column[line]
          if symbol != symbol_to_check:
             break
      else:
         winnings += values[symbol] * bet
         winning_lines.append(line + 1)
   return winnings,winning_lines
   
def get_slot_machine_spin(rows,cols,symbols):
   # inside the function we need to generate what symbol wil be in each column based on the frequency
   all_symbols = []
   for symbol,symbol_count in symbols.items():
      for _ in range(symbol_count):
         all_symbols.append(symbol)
   columns = []
   for col in range(cols):
      column = []
      # Making a copy of the all_symbols list
      current_symbols = all_symbols[:]
      for _ in range(rows):
         value = random.choice(all_symbols)
         current_symbols.remove(value)
         # adding the name of value to our column
         column.append(value)
      columns.append(column)
   return columns
  
def print_slot_machines(columns):
   # we are going to transpose the columns
   for row in range(len(columns[0])):
   # Looping through all columns and printing only th first value in it or whatever the index of the current row is
      for i,column in enumerate(columns):
         if i != len(columns) - 1:
            print(column[row],end=" | ")
         else:
            print(column[row],end="")
      print()

def deposit():
   while True:
      amount = input("Enter amount you wish to deposit?$")
      if amount.isdigit():
         amount = int(amount)
         if amount >= 1:
            break
         else:
            print("Deposit must be greater than 0")
      else:
         print("Please Enter a Valid deposit")
   return amount

def get_number_of_lines():
   while True:
      lines = input(f"Enter number of lines to bet on (1-{MAX_LINES})?#")
      if lines.isdigit():
         lines = int(lines)
         if 1 <= lines <= MAX_LINES:
            break
         else:
            print(f"Lines should be in the given range 1-{MAX_LINES}")
      else:
         print("Please Enter a Number")
   return lines

def get_bet():
   while True:
      bet = input("How much do you want to bet on each line? $")
      if bet.isdigit():
         bet = int(bet)
         if MIN_BET <= bet <= MAX_BET:
            break
         else:
            print(f"Amount must be above {MIN_BET}-{MAX-BET}")
      else:
         print("Please Enter a Number")
   return bet

def game(balance):
   lines = get_number_of_lines()
   while True:
      bet = get_bet()
      total_bet = lines * bet
      if total_bet > balance:
         print(f"Insufficient Balance. Your Current Balance is ${balance}")
      else:
         break
   print(f"you are betting ${bet} on {lines} line(s). Total bet is = ${total_bet}")
   slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
   print_slot_machines(slots)
   winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
   print(f"you won ${winnings}")
   print(f"you won on lines:", *winning_lines)  # * = In this syntax the splat operator to unpack from the collection
   return winnings - total_bet

def check_balance(balance):
   if balance == 0:
      return deposit()

def main():
   balance = deposit()
   while True:
      print(f"Current Balance is ${balance}")
      spin = input("Press Enter to Play(q to quit)").lower()
      if spin == 'q':
         break
      balance += game(balance)
      if balance != 0:
         print(f'You left with {balance}')
      else:
         print(f"Insufficient Balance. Your Current Balance is ${balance}")
         balance += deposit()
main()
input()