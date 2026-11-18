# 1. Roll a die
import random
print(random.randint(1, 6))

# 2. Shuffle a list
import random
cards = ["A", "K", "Q", "J", "10"]
random.shuffle(cards)
print(cards)

# 3. Today's date, formatted
from datetime import date
print(date.today().isoformat())   # 2025-01-15

# 4. Countdown timer
import time
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("🚀 liftoff")

# 5. Average of a list
import statistics
print(statistics.mean([10, 20, 30, 40]))   # 25