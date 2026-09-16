from pathlib import Path
import sqlite3
import pandas as pd
ROOT=Path(__file__).resolve().parent
with sqlite3.connect((ROOT/'data'/'warehouse.db').as_uri()+'?mode=ro',uri=True) as con:
    df=pd.read_sql_query('SELECT * FROM sales',con)
print(df.head())

# TODO P1: province x month, sum(amount), fill_value=0, margins=True

pivot_p1 = pd.pivot_table(
    df,
    index="province",
    columns="month",
    values="amount",
    aggfunc="sum",
    fill_value=0,
    margins=True
)

print("\n=== P1: Province x Month ===")
print(pivot_p1)


# TODO P2: filter September, then category x province

df_sep = df[df["month"] == "2026-09"]

pivot_p2 = pd.pivot_table(
    df_sep,
    index="category",
    columns="province",
    values="amount",
    aggfunc="sum",
    fill_value=0
)

print("\n=== P2: September Category x Province ===")
print(pivot_p2)

# TODO P3: assert that the pivot grand total equals df['amount'].sum()

assert pivot_p1.loc["All", "All"] == df["amount"].sum()

print("\n=== P3: Grand Total Check ===")
print("Pivot Grand Total:", pivot_p1.loc["All", "All"])
print("DataFrame Total:", df["amount"].sum())
print("PASS")
# TODO P4: export each result to CSV in your submission folder

pivot_p1.to_csv("pivot_p1_province_month.csv", encoding="utf-8-sig")
pivot_p2.to_csv("pivot_p2_september_category_province.csv", encoding="utf-8-sig")

print("\n=== P4: Export CSV ===")
print("Exported P1 and P2 CSV successfully")
