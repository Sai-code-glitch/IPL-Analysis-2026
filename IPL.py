import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# --- 2026-2050 TRANSITION ARCHITECTURE ---
years = np.arange(2026, 2051)

def ipl_2050_model(start_val, ai_impact_coeff=1.45):
    """
    Simulates exponential growth with an AI-driven multiplier.
    ai_impact_coeff: Efficiency factor for personalized monetization.
    """
    # Base growth (7.5%) + AI-driven exponential kicker
    # Added a small stochastic noise for realism
    noise = np.random.normal(0, 0.05, len(years))
    base_growth = start_val * ((1.075 + noise) ** (years - 2026))
    ai_kicker = (years - 2026) * ai_impact_coeff * 1.2
    return base_growth + ai_kicker

# --- CALCULATING VALUATIONS (USD Billions) ---
# League Value starts at 18.5B; CSK Brand starts at 0.235B
ipl_valuation = ipl_2050_model(18.5, ai_impact_coeff=2.5) 
csk_brand_value = ipl_2050_model(0.235, ai_impact_coeff=0.4)

# --- VISUALIZATION ---
plt.style.use('dark_background')
fig, ax1 = plt.subplots(figsize=(15, 8), dpi=100)

# Create smooth splines for the IPL Economy curve
x_smooth = np.linspace(years.min(), years.max(), 300)
spl = make_interp_spline(years, ipl_valuation, k=3)
y_smooth = spl(x_smooth)

# Plotting the IPL Economy
ax1.plot(x_smooth, y_smooth, color='#00E5FF', linewidth=5, alpha=0.9, label='IPL Total Economy (AI Integrated)')
ax1.fill_between(x_smooth, y_smooth, color='#00E5FF', alpha=0.1)

# Secondary Axis for CSK Brand Evolution
ax2 = ax1.twinx()
ax2.plot(years, csk_brand_value, color='#FFD700', linewidth=3, marker='o', 
         markersize=8, markevery=4, label='CSK Brand Legacy Index')

# Annotations (Fixed Syntax)
ax1.annotate('2030: AI Agentic Rights\n(Autonomous Bidding)', 
             xy=(2030, ipl_valuation[4]), 
             xytext=(2027, ipl_valuation[4] + 40),
             arrowprops=dict(arrowstyle='->', color='#00E5FF', lw=1.5),
             fontsize=10, fontweight='bold')

ax1.annotate('2045: Virtual Stadium\nDominance', 
             xy=(2045, ipl_valuation[19]), 
             xytext=(2040, ipl_valuation[19] + 60),
             arrowprops=dict(arrowstyle='->', color='#FFD700', lw=1.5),
             fontsize=10, fontweight='bold')

# Formatting
plt.title('IPL 2050: THE INTELLIGENT LEAGUE ERA\n[AI Multiplier & Attention Capital Simulation]', 
          fontsize=18, fontweight='bold', pad=30)
ax1.set_xlabel('Timeline (2026 - 2050)', fontsize=12, color='#888888')
ax1.set_ylabel('IPL Valuation (USD Billion)', color='#00E5FF', fontsize=13, fontweight='bold')
ax2.set_ylabel('CSK Brand Value (USD Billion)', color='#FFD700', fontsize=13, fontweight='bold')

ax1.grid(True, linestyle=':', alpha=0.2)
ax1.legend(loc='upper left', frameon=False)
ax2.legend(loc='upper center', frameon=False)

plt.tight_layout()
plt.show()