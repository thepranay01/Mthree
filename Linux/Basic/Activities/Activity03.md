# 🧪 Activity: Fix Log Analysis

## Completion Requirements
In this activity, you will use Linux to analyze and update existing log files.

---

## 📌 Getting Started
1. **Clean Up Home Directory**
   - Remove unnecessary files to maintain a clean workspace.

2. **Download & Run the `fixGenerator.sh` Script**
   ```bash
   wget https://github.com/TheAcademy/pss-orderbook-deploy/blob/main/src/linux_activities/fixGenerator.sh
   chmod +x fixGenerator.sh
   ./fixGenerator.sh &
   ```

---

## 🛠️ Instructions

### 1️⃣ Create a Logs Directory
```bash
mkdir logs
```

### 2️⃣ Move the Log Output
Once the `fixGenerator.sh` script completes, move the log files to the `logs` directory:
```bash
mv fixlog.log logs/
```

### 3️⃣ Replace "WILEYEDGE" with "EDGE"
```bash
sed 's/WILEYEDGE/EDGE/g' logs/fixlog.log > logs/fixlog2.log
```

### 4️⃣ Extract Fill Messages into `fills.log`
```bash
grep 'fill' logs/fixlog2.log > logs/fills.log
```

### 5️⃣ Extract Cancel Acknowledgments (39=4) into `cancels.log`
```bash
grep '39=4' logs/fixlog2.log > logs/cancels.log
```

### 6️⃣ Extract Partial Fills into `partialFills.log`
```bash
grep 'partial fill' logs/fills.log > logs/partialFills.log
```

### 7️⃣ Extract Specific Tags Using `awk`
```bash
awk -F '|' '{print $55, $11, $54, $31, $32, $17}' logs/partialFills.log > logs/parsedPartialFills.log
```

### 8️⃣ Format `parsedPartialFills.log` into CSV (`.module10.csv`)
- Remove tag numbers and format as comma-separated values:
```bash
sed 's/55=//g; s/11=//g; s/54=//g; s/31=//g; s/32=//g; s/17=//g' logs/parsedPartialFills.log | tr ' ' ',' > ~/module10.csv
```
- Add a header row:
```bash
echo 'Symbol,OrderID,Side,Price,Qty,ExecID' | cat - ~/module10.csv > temp && mv temp ~/module10.csv
```

### 9️⃣ Modify `cancels.log` and Compare Differences
- Create a copy of `cancels.log`:
```bash
cp logs/cancels.log logs/cancels2.log
```
- Edit `cancels2.log`:
  - Open in an editor and modify the first symbol (tag 55) by prepending "A" (e.g., `55=GOOG` → `55=AGOOG`).
- Compare the original and modified files:
```bash
diff logs/cancels.log logs/cancels2.log
```

### 🔟 Save History to a File
```bash
history > ~/$(whoami).$(date +%y%m%d).module10
```

---

## 📸 Screenshots

![Fix Log Analysis Output](https://drive.google.com/uc?export=view&id=YOUR_FILE_ID)

