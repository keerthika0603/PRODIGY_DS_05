import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("traffic_accidents.csv")

# ------------------------
# Basic Statistics
# ------------------------
total_accidents = df["Accidents"].sum()

highest = df.loc[df["Accidents"].idxmax()]

print("Total Accidents:", total_accidents)
print("\nHighest Accident Scenario:")
print(highest)

# ------------------------
# Road Condition Analysis
# ------------------------
road_data = df.groupby("Road_Condition")["Accidents"].sum()

plt.figure(figsize=(8,5))
road_data.plot(kind="bar")
plt.title("Accidents by Road Condition")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.savefig("road_condition.png")
plt.close()

# ------------------------
# Weather Analysis
# ------------------------
weather_data = df.groupby("Weather")["Accidents"].sum()

plt.figure(figsize=(8,5))
weather_data.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Accidents by Weather")
plt.savefig("weather_analysis.png")
plt.close()

# ------------------------
# Time Analysis
# ------------------------
time_data = df.groupby("Time_of_Day")["Accidents"].sum()

plt.figure(figsize=(8,5))
sns.barplot(
    x=time_data.index,
    y=time_data.values
)

plt.title("Accidents by Time of Day")
plt.ylabel("Accidents")
plt.tight_layout()
plt.savefig("time_analysis.png")
plt.close()

# ------------------------
# Heatmap
# ------------------------
pivot = df.pivot_table(
    values="Accidents",
    index="Weather",
    columns="Time_of_Day"
)

plt.figure(figsize=(8,5))
sns.heatmap(
    pivot,
    annot=True,
    cmap="YlOrRd"
)

plt.title("Accident Hotspots")
plt.tight_layout()
plt.savefig("accident_hotspots.png")
plt.close()

# ------------------------
# HTML Report
# ------------------------
html = f"""
<html>
<head>
<title>Traffic Accident Analysis</title>

<style>
body {{
font-family: Arial;
background:#f5f7fa;
padding:20px;
}}

.card {{
background:white;
padding:20px;
margin:20px;
border-radius:10px;
box-shadow:0px 2px 10px rgba(0,0,0,0.1);
}}

img {{
width:100%;
}}

h1 {{
text-align:center;
}}
</style>

</head>

<body>

<h1>Traffic Accident Analysis Dashboard</h1>

<div class="card">
<h2>Summary</h2>
<p>Total Accidents: {total_accidents}</p>
<p>Most Risky Condition:</p>
<p>
Road: {highest['Road_Condition']}<br>
Weather: {highest['Weather']}<br>
Time: {highest['Time_of_Day']}<br>
Accidents: {highest['Accidents']}
</p>
</div>

<div class="card">
<h2>Road Condition Analysis</h2>
<img src="road_condition.png">
</div>

<div class="card">
<h2>Weather Analysis</h2>
<img src="weather_analysis.png">
</div>

<div class="card">
<h2>Time of Day Analysis</h2>
<img src="time_analysis.png">
</div>

<div class="card">
<h2>Accident Hotspots</h2>
<img src="accident_hotspots.png">
</div>

</body>
</html>
"""

with open("traffic_report.html", "w") as file:
    file.write(html)

print("\nProject Completed Successfully!")
print("Open traffic_report.html from File Explorer.")