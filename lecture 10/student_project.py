# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 22:38:46 2026

@author: HP 840 G3
"""


import pandas as pd


aaa = pd.read_excel("student data.xlsx", sheet_name=0)

print("ORIGINAL DATA")
print(aaa)



print("\nSELECT NAME, MONDAY AND FRIDAY")
print(aaa[["Name", "Monday", "Friday"]])



print("\nSELECT ROWS AND COLUMNS USING ILOC")
print(aaa.iloc[1:, 0:4])



bbb = aaa.reindex(columns=[
    "Name", "Monday", "Wednesday", "Friday"
])

print("\nREINDEXED COLUMNS")
print(bbb)



print("\nREINDEXED ROWS AND COLUMNS")
print(aaa.reindex(
    aaa.index[1:],
    columns=["Name", "Monday", "Friday"]
))



bbb = bbb.set_index("Name")

print("\nNAME AS INDEX")
print(bbb)



days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

aaa["Total Hours"] = aaa[days].sum(axis=1)

print("\nTOTAL STUDY HOURS")
print(aaa)



aaa["Average Hours"] = aaa[days].mean(axis=1)

print("\nAVERAGE STUDY HOURS")
print(aaa)



print("\nSELECT IDRIS AND JOHN")
print(aaa.loc[[0, 1], ["Name", "Monday", "Friday"]])



print("\nSELECT EVERY SECOND STUDENT")
print(aaa.loc[aaa.index[::2], ["Name", "Monday", "Friday"]])



aa2 = aaa.copy()

del aa2["Monday"]

print("\nAFTER DELETING MONDAY")
print(aa2)



aa2 = aaa.copy()

aa2 = aa2.drop("Tuesday", axis=1)

print("\nAFTER DELETING TUESDAY")
print(aa2)



aa2 = aaa.copy()

aa2 = aa2.drop(aa2.index[0])

print("\nAFTER DELETING FIRST ROW")
print(aa2)



aa2 = aaa.copy()

aa2.drop("Wednesday", axis=1, inplace=True)

print("\nAFTER DELETING WEDNESDAY")
print(aa2)



aa2 = aaa.copy()

aa2.drop(["Thursday", "Friday"], axis=1, inplace=True)

print("\nAFTER DELETING THURSDAY AND FRIDAY")
print(aa2)



aa2 = aaa.copy()

aa2.drop(
    aa2.columns[[1, 2]],
    axis=1,
    inplace=True
)

print("\nAFTER DELETING COLUMNS BY POSITION")
print(aa2)



aa2 = aaa.copy()

positions = [1, 2, 4, 5, 6]
valid_positions = [i for i in positions if i < len(aa2)]

aa2.drop(
    aa2.index[valid_positions],
    axis=0,
    inplace=True
)

print("\nAFTER DELETING ROWS BY POSITION")
print(aa2)
