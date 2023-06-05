from pathlib import Path

path = Path("C:/Users/USER/Python/great")

for i in path.rglob("**\*"):
    print(i)