"""Monday Morning Punchlines — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The joke: Monday morning — the alarm, the cold coffee, and a meeting about being tired.
TEXT = "Monday morning: my alarm went off, my coffee went cold, and my calendar already scheduled a meeting to discuss why I am tired."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
