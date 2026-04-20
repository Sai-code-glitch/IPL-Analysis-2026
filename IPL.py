import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Simulate IPL 2026 Data Trends
# Week 1 to Week 8 of the season
weeks = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# TV Revenue Trend (Reflecting the ~31% drop in ad volume)
tv_revenue = np.array([100, 92, 85, 78, 72, 69, 67, 65]) 

# Youth Engagement Trend (Digital/OTT streaming & Social Sentiment)
youth_engagement = np.array([60, 75, 88, 110, 135, 150, 165, 180])

# 2. Create DataFrame
df = pd.DataFrame({
    'Week': weeks,
    'TV_Revenue_Index': tv_revenue,
    'Digital_Youth_Engagement': youth_engagement
})

# 3. Data Visualization for the Dashboard
plt.style.use('dark_background') # Professional "Analyst" Look
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plotting TV Revenue (Left Axis)
color_tv = '#ffcc00' # CSK Yellow!
ax1.set_xlabel('IPL 2026 Season (Weeks)')
ax1.set_ylabel('TV Ad Revenue Index', color=color_tv)
ax1.plot(df['Week'], df['TV_Revenue_Index'], color=color_tv, marker='o', linewidth=3, label='TV Revenue')
ax1.tick_params(axis='y', labelcolor=color_tv)

# Plotting Youth Engagement (Right Axis)
ax2 = ax1.twinx()
color_digital = '#00d4ff' 
ax2.set_ylabel('Digital Youth Engagement (Millions)', color=color_digital)
ax2.plot(df['Week'], df['Digital_Youth_Engagement'], color=color_digital, marker='s', linewidth=3, label='Youth Engagement')
ax2.tick_params(axis='y', labelcolor=color_digital)

plt.title('IPL 2026: The Great Media Pivot\n(TV Revenue Decay vs. Youth Digital Surge)', fontsize=14)
fig.tight_layout()

# Show plot
plt.show()

# 4. Math for the Post: Correlation Calculation
correlation = df['TV_Revenue_Index'].corr(df['Digital_Youth_Engagement'])
print(f"Correlation between TV Revenue and Youth Digital Engagement: {correlation:.2f}")