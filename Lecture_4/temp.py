
import pandas as pd

data = {
    "Subjects": ["军训", "思修", "史纲", "马原", "毛概"],
    "Grade": [88, 89, 90, 91, 92],
    "year": [2018, 2019, 2019, 2020, 2020],
}
df = pd.DataFrame(data)
df


# 加权平均，计算GPA
df["sum"] = df["credit"] * df["point"]
GPA = df["sum"].sum() / df["credit"].sum()
GPA
