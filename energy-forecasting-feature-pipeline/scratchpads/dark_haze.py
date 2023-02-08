"""
NOTE: Scratchpad blocks are used only for experimentation and testing out code.
The code written here will not be executed as part of the pipeline.
"""
from mage_ai.data_preparation.variable_manager import get_variable

import matplotlib.pyplot as plt


df = get_variable('energy_consumption', 'remove_extra_data', 'output_0')

df = df[(df["Area"] == "DK1") & (df["Consumer Type"] == "111")]

fig, ax = plt.subplots(figsize=(16, 6))
ax = df.plot(x="UTC Datetime", y="Energy Consumption", ax=ax)
df.plot(x="UTC Datetime", y="Energy Consumption Rolling Average 1", ax=ax)
df.plot(x="UTC Datetime", y="Energy Consumption 31", ax=ax)

df[["Energy Consumption", "Energy Consumption 1", "Energy Consumption 4"]].head(100)
