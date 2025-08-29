# WordGenX---Custom-Wordlist-Generator

# 🔑 WordGenX
**Unpredictable Custom Password Generator**
WordGenX is a **cross-platform Python tool** for generating strong, unpredictable, and custom passwords.  
It takes **seed words** (like names, nicknames, org names, etc.) and applies **mangling techniques** to create complex passwords with leetspeak, random casing, inserted special characters, reversals, and duplications.
No boring `password123` here — WordGenX spits out 🔥 `M@HaKaL_77!`, `$cyb3RninJA`, and other unpredictable monsters.

---

## 🚀 Features
- Generate **unpredictable custom passwords** from seed words.
- **Mangling rules**:
  - Leetspeak substitutions (`a → @`, `e → 3`, `o → 0`, etc.)
  - Random case variations
  - Insert special characters **inside words** (not just start/end)
  - Reverse or duplicate words
- **Customizable length** and **count** of passwords.
- Works on **Linux, Windows, macOS, WSL, Termux**.
- **Save results** to a file for later use.
- Beginner-friendly CLI.

---

<img width="1190" height="495" alt="image" src="https://github.com/user-attachments/assets/e94a6df7-6646-458a-b362-46fa141e7cb4" />

## ⚡ Installation
Clone the repository and run directly with Python 3:

```bash
git clone https://github.com/abhinav8377/WordGenX.git
cd WordGenX
chmod +x wordgenx.py
```

🛠 Usage
```bash
python3 wordgenx.py -w <words> [options]
```

# Arguments
*Flag	Description*
<img width="762" height="217" alt="image" src="https://github.com/user-attachments/assets/608ac31b-f002-4974-8f3d-5124b9ca2222" />


# 🎯 Examples
1. Basic password generation
```bash
python3 wordgenx.py -w abhinav mahakal
```
2. With leetspeak mangling
```bash
python3 wordgenx.py -w abhinav hacker -c 10 --leet
```
3. Complex unpredictable passwords
```bash
python3 wordgenx.py -w cyber ninja -l 16 -c 25 --complex --leet
```
4. Custom specials + output to file
```bash
python3 wordgenx.py -w india ggsipu -l 14 -c 50 -s ! _ % ^ -o passwords.txt
```

# ⚠️ Disclaimer
This tool is for educational and security research purposes only.
Do not use it for unauthorized access or illegal activities.
The author is not responsible for misuse.

# 👨‍💻 Author
Developed with ❤️ by Abhinav
🔗 GitHub: abhinav8377
