#!/usr/bin/env python3
"""
Real‑World Vedic Pipeline Demo
Fetches live temperature data, compresses, predicts, verifies.
"""
import json
import urllib.request
import vedic

# 1. Fetch live data (Berlin coordinates)
url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&forecast_days=2"
print("Fetching live weather data...")
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())

temps = data["hourly"]["temperature_2m"][:24]
print(f"Received {len(temps)} hourly temperature values: {temps[:6]}...\n")

# 2. Compress
original_text = str(temps)
compressed, dictionary = vedic.compress(original_text)
print(f"Shunyam Compression: {len(original_text)} bytes -> {len(compressed)} bytes")
print(f"Compressed sample: {compressed[:80]}...\n")

# 3. Predict
last_temp = int(temps[-1])
predicted_seq = vedic.predict(last_temp, 3)
predicted = predicted_seq[-1]
print(f"Last temperature: {last_temp}°C")
print(f"Ekadhikena predicted sequence from {last_temp}: {predicted_seq}")
print(f"Next predicted temperature: {predicted}°C\n")

# 4. Verify multiplication
a, b, product = 23, 45, 1035
ver = vedic.verify_multiplication(a, b, product)
print(f"Gunita verification: {a}×{b}={product} ➜ {ver}\n")

# 5. Solve constraint
s = temps[0] + temps[1]
d = temps[1] - temps[0]
x, y = vedic.sankalana_solve(s, d)
print(f"Sankalana: sum={s}, diff={d} → x={x}, y={y} (original: {temps[0]},{temps[1]})\n")

# 6. Build report line by line (no triple‑quote)
lines = []
lines.append("# Real‑World Vedic Pipeline Report\n")
timestamp = data["hourly"]["time"][0] if data["hourly"]["time"] else "N/A"
lines.append(f"**Data source:** Open‑Meteo API (Berlin hourly temperature)  \n")
lines.append(f"**Timestamp:** {timestamp}\n\n")
lines.append("## 1. Shunyam Compression\n")
lines.append(f"- Original size: {len(original_text)} bytes  \n")
lines.append(f"- Compressed size: {len(compressed)} bytes  \n")
compression_ratio = (1 - len(compressed)/len(original_text))*100
lines.append(f"- Compression ratio: {compression_ratio:.2f}%\n\n")
lines.append("## 2. Ekadhikena Prediction\n")
lines.append(f"- Last observed: {last_temp}°C  \n")
lines.append(f"- Predicted sequence: {predicted_seq}  \n")
lines.append(f"- Next value: {predicted}°C\n\n")
lines.append("## 3. Gunita Samuccaya Verification\n")
lines.append(f"- {a} × {b} = {product} ✓\n\n")
lines.append("## 4. Sankalana Constraint\n")
lines.append(f"- From first two temps: sum={s}, diff={d} → x={x}, y={y}\n\n")
lines.append("## 5. Vedic Library Import\n")
lines.append("```\n")
lines.append("import vedic\n")
lines.append("print(vedic.mul(98,97))       # 9506\n")
lines.append("print(vedic.cuberoot(405224)) # 74\n")
lines.append("```\n")

report = "".join(lines)

with open("REAL_WORLD_DEMO.md", "w") as f:
    f.write(report)

print("Real‑world demo report written to REAL_WORLD_DEMO.md")
