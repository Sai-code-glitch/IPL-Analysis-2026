import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import functools
import logging
import secrets
from datetime import datetime

# --- SYSTEM TELEMETRY ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - [MASTER_NODE] - %(message)s')
logger = logging.getLogger(__name__)

def trace_execution(func):
    """
    Distributed tracing decorator. 
    Uses secrets.token_hex to avoid 32-bit Integer Overflow.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Generates a collision-resistant 64-bit Trace ID
        trace_id = secrets.token_hex(8) 
        start = datetime.now()
        result = func(*args, **kwargs)
        duration = (datetime.now() - start).total_seconds()
        logger.info(f"NODE: {func.__name__} | TRACE: {trace_id} | LATENCY: {duration:.4f}s")
        return result
    return wrapper

# --- ARCHITECTURE: THE 2050 SIMULATOR ---
class IPLFutureNarrative:
    def __init__(self, start_yr=2026, end_yr=2050):
        self.years = np.arange(start_yr, end_yr + 1)
        self.t = len(self.years)
        
    def simulate_narrative_economy(self, start_val, ai_coeff):
        """
        Simulates the convergence of:
        1. AI Multiplier (Efficiency & Monetization)
        2. Bio-Augmentation (Asset Longevity)
        3. Climate Entropy (Logistical Drag)
        """
        # A. Stochastic Baseline (Market Volatility)
        drift = 0.085 
        vol = 0.065
        market_noise = np.random.normal(drift, vol, self.t)
        traj = [start_val]
        for r in market_noise[:-1]:
            traj.append(traj[-1] * (1 + r))
        base_vals = np.array(traj)

        # B. The Intelligence Kicker (Exponential Scaling)
        ai_impact = (self.years - self.years[0]) * ai_coeff * 2.8
        
        # C. Bio-Augmentation ROI (Career extension & Neural Engagement)
        bio_boost = np.linspace(1, 1.40, self.t) 
        
        # D. Climate Resilience Tax (Logistical drag for Smart-Domes)
        climate_drag = np.linspace(1, 0.80, self.t) 
        
        # Converged Result: The Future Economy
        return (base_vals * bio_boost * climate_drag) + ai_impact

    @trace_execution
    def run_suite(self):
        # IPL Economy (Base: $18.5B)
        self.economy = self.simulate_narrative_economy(18.5, ai_coeff=4.2)
        
        # CSK Brand (Base: $0.235B) - Higher Resilience Coefficient
        self.csk_equity = self.simulate_narrative_economy(0.235, ai_coeff=0.72)
        
        # Confidence Intervals
        self.upper = self.economy * 1.15
        self.lower = self.economy * 0.85
        
        return self.economy, self.csk_equity

    def visualize_narrative(self):
        plt.style.use('dark_background')
        fig, ax1 = plt.subplots(figsize=(20, 11), dpi=120)

        # Spline Smoothing for the 'Intelligent' Trendline
        x_smooth = np.linspace(self.years.min(), self.years.max(), 500)
        spline = make_interp_spline(self.years, self.economy, k=3)
        y_smooth = spline(x_smooth)

        # Plot 1: The Global GDP of Attention
        ax1.plot(x_smooth, y_smooth, color='#00E5FF', linewidth=7, alpha=0.9, 
                 label='IPL Total Economy: The Great Convergence')
        ax1.fill_between(self.years, self.lower, self.upper, color='#00E5FF', alpha=0.08)

        # Plot 2: The CSK Brand Legacy
        ax2 = ax1.twinx()
        ax2.plot(self.years, self.csk_equity, color='#FFD700', linewidth=4, marker='H', 
                 markersize=12, markevery=4, label='CSK Brand Equity (USD Billion)')

        # NARRATIVE MILESTONES
        ax1.annotate('2032: NEURAL-LINK MONETIZATION\nDirect-to-Mind Engagement', 
                     xy=(2032, self.economy[6]), xytext=(2027, self.economy[6]+120),
                     arrowprops=dict(arrowstyle='-|>', color='#00E5FF', lw=2), 
                     fontsize=11, fontweight='bold', bbox=dict(facecolor='black', alpha=0.6))

        ax1.annotate('2040: CLIMATE-RESILIENCE PIVOT\nSmart-Dome Stadium Districts', 
                     xy=(2040, self.economy[14]), xytext=(2034, self.economy[14]+160),
                     arrowprops=dict(arrowstyle='-|>', color='#FFD700', lw=2), 
                     fontsize=11, fontweight='bold', bbox=dict(facecolor='black', alpha=0.6))
        
        ax1.annotate('2048: THE AUTONOMOUS LEAGUE\nAI-Android & Human Hybrids', 
                     xy=(2048, self.economy[22]), xytext=(2042, self.economy[22]-100),
                     arrowprops=dict(arrowstyle='-|>', color='#FFFFFF', lw=2), 
                     fontsize=11, fontweight='bold', bbox=dict(facecolor='black', alpha=0.6))

        # DASHBOARD STYLING
        ax1.set_xlabel('TIMELINE OF EVOLUTION (2026 - 2050)', fontsize=14, color='gray', labelpad=15)
        ax1.set_ylabel('TOTAL VALUATION (USD BILLION)', color='#00E5FF', fontsize=16, fontweight='bold')
        ax2.set_ylabel('CSK BRAND EQUITY (USD BILLION)', color='#FFD700', fontsize=16, fontweight='bold')
        
        plt.title('IPL 2050: THE POST-PHYSICAL ECONOMY\n[Convergence of Intelligence, Resilience, and Legacy]', 
                  fontsize=22, fontweight='bold', pad=45)
        
        ax1.grid(True, linestyle='--', alpha=0.1)
        ax1.legend(loc='upper left', frameon=False, fontsize=13)
        ax2.legend(loc='upper center', frameon=False, fontsize=13)
        
        plt.tight_layout()
        plt.show()

# --- EXECUTION ---
if __name__ == "__main__":
    narrative = IPLFutureNarrative()
    narrative.run_suite()
    narrative.visualize_narrative()