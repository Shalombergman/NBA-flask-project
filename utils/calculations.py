def calculate_atr(assists, turnovers):
    return assists / turnovers if turnovers else float('inf')

def calculate_ppg_ratio(points, games):
    return points / games if games else 0