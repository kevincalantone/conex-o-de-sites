# save as expenses_tracker.py
import csv
from datetime import datetime
from collections import defaultdict
import argparse
import os

FILE = os.path.expanduser("~/.expenses.csv")

def ensure_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["date","amount","category","description"])

def add_entry(amount, category, description, date=None):
    ensure_file()
    date = date or datetime.now().strftime("%Y-%m-%d")
    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([date, f"{amount:.2f}", category, description])
    print("Entrada adicionada.")

def summary(month=None):
    ensure_file()
    totals = defaultdict(float)
    with open(FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            if not r["amount"]: continue
            row_month = r["date"][:7]
            if month and row_month != month: continue
            totals[r["category"]] += float(r["amount"])
    print(f"Resumo para {month or 'todas os meses'}:")
    for cat, val in sorted(totals.items(), key=lambda x: -x[1]):
        print(f"  {cat:20} R$ {val:,.2f}")
    print(f"Total: R$ {sum(totals.values()):,.2f}")

def main():
    parser = argparse.ArgumentParser(description="Tracker de despesas simples")
    sub = parser.add_subparsers(dest="cmd")
    a = sub.add_parser("add")
    a.add_argument("amount", type=float)
    a.add_argument("category", type=str)
    a.add_argument("description", nargs="?", default="")
    a.add_argument("--date", default=None)
    s = sub.add_parser("summary")
    s.add_argument("--month", help="YYYY-MM (ex: 2025-09)")
    args = parser.parse_args()
    if args.cmd == "add":
        add_entry(args.amount, args.category, args.description, args.date)
    elif args.cmd == "summary":
        summary(args.month)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
