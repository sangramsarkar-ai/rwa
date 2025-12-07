# rwa_data.py
"""
Static configuration and reference data for the RWA dashboard.
"""

# Total area
TOTAL_SQFT = 405_770  # total built-up area in sq ft

# Executive Committee
EXEC_MEMBERS = [
    "Harish Siddareddy",
    "Guru Prasad Barik",
    "Sangram Sarkar",
    "Siddharth Maheshwari",
    "M. V. S. R. Raviteja",
    "M. Rupesh Kumar",
    "Jayanthi Venkata Ravisankar",
    "Alok Kumar Sahu",
    "Nilesh Arvind Panchal",
    "Prajesh T O",
    "Nagesh Babu Kattamuri",
    "Pavan Praneshrao Joshi",
]

# Support Staff
SUPPORT_STAFF = [
    {"Role": "Electrician", "Name": "Ishwar"},
    {"Role": "Plumber", "Name": "Sushant"},
    {"Role": "MST Technician", "Name": "Chandra"},
    {"Role": "STP/WTP Operator", "Name": "Nazim"},
    {"Role": "Gardener", "Name": "Subharau"},
    {"Role": "Gardener", "Name": "Nagaraj"},
    {"Role": "Housekeeping Supervisor", "Name": "Parkash"},
    {"Role": "Security Supervisor (Day)", "Name": "Rajesh"},
    {"Role": "Security Supervisor (Night)", "Name": "Atul"},
]

# Manpower data – November
MANPOWER_NOV = {
    "Facility Manager": 1,
    "Security Guards": 5,
    "Security Supervisors": 2,
    "Housekeeping Staff": 8,
    "Housekeeping Supervisor": 1,
    "Electrician": 1,
    "Plumber": 1,
    "Multi Technician (Night)": 1,
    "Gardener": 1,
    "STP/WTP Operator": 1,
}

# Manpower data – December
MANPOWER_DEC = {
    "Facility Manager": 1,
    "Security Guards": 5,
    "Security Supervisors": 2,
    "Housekeeping Staff": 10,
    "Housekeeping Supervisor": 1,
    "Electrician": 1,
    "Plumber": 1,
    "Multi Technician (Night)": 1,
    "Gardener": 2,
    "STP/WTP Operator": 1,
}

# Monthly running cost heads
RUNNING_COST = {
    "Water": 525_000,
    "Idencies FM": 550_000,
    "Diesel": 46_000,
    "Electricity": 170_000,
    "Garbage": 36_400,
    "R&M": 15_000,
    "Drinking Water": 1_200,
}

TOTAL_RUNNING = 1_343_600  # Total monthly running cost

# Provisions / Capex heads
PROVISIONS = {
    "DG panel": 138_178,
    "WTP motors": 60_000,
    "Lift AMC": 1_288_000,
    "DG AMC": 88_000,
    "Fire AMC": 75_000,
    "Audit + renewal": 44_000,
    "Fire license": 90_000,
    "Security cameras": 300_000,
    "OHT cleaning": 39_000,
    "Lift cameras": 140_000,
    "Speed breakers": 10_000,
    "Lights": 13_000,
    "Ladder": 12_000,
}

TOTAL_PROVISIONS = 2_297_178  # Total provisions / capex
