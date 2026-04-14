# CliPassGen (Console Smart Password Generator) <sup>v3.0.0</sup>

---

**Terminal-based smart password generator with deterministic password generation. 
Generate passwords from secret phrases - same secret always produces the same password, no storage required.**

---

[![PyPI - Downloads](https://img.shields.io/pypi/dm/clipassgen?label=pypi%20downloads)](https://pypi.org/project/clipassgen/)
[![PyPI Downloads](https://static.pepy.tech/badge/clipassgen)](https://pepy.tech/projects/clipassgen)
[![PyPI Weekly Downloads](https://static.pepy.tech/badge/clipassgen/week)](https://pepy.tech/projects/clipassgen)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/clipassgen)
[![GitHub release](https://img.shields.io/github/v/release/smartlegionlab/clipassgen)](https://github.com/smartlegionlab/clipassgen/)
[![PyPI version](https://img.shields.io/pypi/v/clipassgen)](https://pypi.org/project/clipassgen)
[![GitHub license](https://img.shields.io/github/license/smartlegionlab/clipassgen)](https://github.com/smartlegionlab/clipassgen/blob/master/LICENSE)
[![PyPI format](https://img.shields.io/pypi/format/clipassgen)](https://pypi.org/project/clipassgen)
[![GitHub stars](https://img.shields.io/github/stars/smartlegionlab/clipassgen?style=social)](https://github.com/smartlegionlab/clipassgen/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/clipassgen?style=social)](https://github.com/smartlegionlab/clipassgen/network/members)

---

## ⚠️ Disclaimer

**By using this software, you agree to the full disclaimer terms.**

**Summary:** Software provided "AS IS" without warranty. You assume all risks.

**Full legal disclaimer:** See [DISCLAIMER.md](https://github.com/smartlegionlab/clipassgen/blob/master/DISCLAIMER.md)

---

## 🔄 Important: smartpasslib v3.0.0 Breaking Change

> **⚠️ This release (v3.0.0) uses [smartpasslib](https://github.com/smartlegionlab/smartpasslib) v3.0.0, which is NOT backward compatible with v2.x.x**

### Why the change?

**Smartpasslib v3.0.0 introduces fundamental improvements:**
- **Stronger cryptographic algorithm** — enhanced deterministic generation with better entropy distribution
- **Improved performance** — faster password generation, especially for longer passwords
- **Better cross-platform consistency** — identical results guaranteed across all platforms
- **Extended character set support** — wider range of special characters for stronger passwords
- **Future-proof architecture** — easier updates and security patches

### What changed:

- The core password generation algorithm has been completely redesigned
- Smart passwords created with v2.1.6 or earlier **will be different** when generated with v3.0.0
- Same secret phrase + same length = different password between versions

### What you need to do:

1. **If you use smart passwords for existing accounts** — you must regenerate and update them
2. **Use the same secret phrases** — they will produce new passwords in v3.0.0
3. **Update your passwords** on all websites/services after upgrading

**Important**: This only affects **smart passwords** (deterministic from secret phrase). Random generation modes (`--strong`, `--base`, `--code`) are unaffected.

📖 **Full migration instructions** → see [Migration Section](#migration-section)

---

## **Core Principles:**

- **Deterministic Generation**: Same secret + same length = same password, every time
- **Zero Storage**: Passwords exist only when generated, never stored
- **Memory-Based Security**: Your brain is the only password database
- **Terminal-First**: Optimized for CLI workflows and scripting
- **Multi-Mode Generation**: Smart passwords, strong random, base passwords, and auth codes

**What You Can Do:**
1. **Generate Smart Passwords**: Deterministic passwords from secret phrases
2. **Create Public Keys**: Verification keys for secret proof without exposure
3. **Generate Random Passwords**: Cryptographically secure random generation
4. **Create Authentication Codes**: Secure codes with character diversity
5. **Interactive Terminal Mode**: Menu-driven interface for easy use
6. **Command Line Mode**: Scriptable generation for automation
7. **Cross-Platform Operation**: Works on any system with Python
8. **No Dependencies**: Pure Python with smartpasslib core

**Key Features:**
- **Deterministic Security**: Identical input → identical output, always
- **Four Generation Modes**: Smart, Strong, Base, and Code
- **Public Key Verification**: Generate keys to prove secret knowledge
- **Interactive & CLI Modes**: Both menu-driven and command-line interfaces
- **Hidden Input**: Secret phrase entry via getpass (hidden typing)
- **SmartPrinter Output**: Beautiful centered and framed terminal text
- **Length Flexibility**: 4-1000 characters depending on mode
- **No Internet Required**: All cryptographic operations local

**Security Model:**
- **Proof of Knowledge**: Public keys verify secrets without exposing them
- **Deterministic Certainty**: Mathematical certainty in password regeneration
- **Ephemeral Passwords**: Passwords exist only in memory during generation
- **Local Computation**: No data leaves your terminal
- **No Recovery Backdoors**: Lost secret = permanently lost passwords (by design)

---

## Research Paradigms & Publications

- **[Pointer-Based Security Paradigm](https://doi.org/10.5281/zenodo.17204738)** - Architectural Shift from Data Protection to Data Non-Existence
- **[Local Data Regeneration Paradigm](https://doi.org/10.5281/zenodo.17264327)** - Ontological Shift from Data Transmission to Synchronous State Discovery

---

## Technical Foundation

Powered by **[smartpasslib](https://github.com/smartlegionlab/smartpasslib) v3.0.0+** — The core library for deterministic password generation.

> ⚠️ **BREAKING CHANGE NOTICE**  
> **smartpasslib v3.0.0 is NOT backward compatible with v2.x.x**  
> Smart passwords generated with v2.x.x will be different when generated with v3.0.0 due to fundamental changes in the deterministic generation algorithm.

**What this means for you:**
- All smart passwords created with **v2.1.6 or earlier** must be **regenerated and updated** after upgrading
- Random generation modes (`--strong`, `--base`, `--code`) are **unaffected**
- Public keys generated from secrets will also be **different** in v3.0.0

**Key principle** (unchanged): Deterministic generation from secret phrase. Same input = same output **within the same major version**.

**Generation Modes:**
- **Smart Password**: Deterministic from secret phrase (BREAKING CHANGE in v3.0.0)
- **Strong Password**: Cryptographically secure random generation (unchanged)
- **Base Password**: Simple random password generation (unchanged)
- **Authentication Code**: Secure code generation for 2FA/MFA (unchanged)

**Public Key System:**
- Generated from secret phrase via enhanced algorithm
- Can be safely stored/shared to verify secret knowledge
- No way to derive secret from public key
- **Note**: v3.0.0 public keys are different from v2.x.x

---

## Migration Section

### Migrating from v2.x.x to v3.0.0

**⚠️ This only affects users who use smart passwords for existing accounts**

**Step 1: Identify affected passwords**
- Any password generated with `--smart` mode using v2.1.6 or earlier
- Passwords from other modes (`--strong`, `--base`, `--code`) are **not affected**

**Step 2: Document your existing smart passwords**
- Before upgrading, retrieve all smart passwords you actively use
- Save them temporarily in a secure location

**Step 3: Upgrade to v3.0.0**
```bash
# Update via pip
pip install clipassgen==3.0.0

# Or rebuild executable with new version
```

**Step 4: Regenerate your smart passwords**
```bash
# Use the SAME secret phrase as before
clipassgen --smart -s "your_secret_phrase" -l 16

# Password will be DIFFERENT from v2.x.x
```

**Step 5: Update your passwords on all services**
- Replace old passwords with newly generated ones
- Test login before removing old access

**Important**: Random generation modes (`--strong`, `--base`, `--code`) work exactly the same — no action needed.

---

## What's New in v3.0.0

### Breaking Change: smartpasslib v3.0.0

- **New cryptographic algorithm** — stronger and faster smart password generation
- **NOT backward compatible** with v2.x.x — smart passwords will be different
- **Random generation modes unaffected** — `--strong`, `--base`, `--code` work as before
- **See migration section above** for detailed upgrade instructions

### Previous Improvements (from v2.1.6)

**Simplified Architecture:**
- **Login parameter removed** - now uses only secret phrase
- **Single smart password type** - streamlined generation process
- **Cleaner command-line interface** - intuitive argument structure
- **Unified generation API** - consistent across all modes

**Enhanced Terminal Interface:**
- **SmartPrinter class** for beautiful centered and framed text output
- **Interactive menu system** with clear navigation
- **Automatic terminal width detection** for perfect formatting
- **Visual feedback** with clear success/error messages

**Security Improvements:**
- **Updated cryptographic backend** to smartpasslib v3.0.0
- **Stronger public key generation** with enhanced algorithms
- **Hidden secret input** via getpass for interactive mode
- **Input validation** with helpful error messages

**User Experience:**
- **Length parameter flexibility** (4-1000 characters)
- **Public key display** for verification purposes
- **Multiple generation modes** in one tool

---

## Installation & Quick Start

### Prerequisites
- **Python 3.7+** required
- **pip** for package management

### Quick Installation
```bash
# Install from PyPI
pip install clipassgen==3.0.0

# For systems with package conflicts
pip install clipassgen==3.0.0 --break-system-packages

# Verify installation
clipassgen --help
```

### Manual Installation
```bash
# Clone repository
git clone https://github.com/smartlegionlab/clipassgen.git
cd clipassgen
pip install .
```

---

## Quick Usage Guide

### Interactive Mode (Recommended for Beginners)
```bash
# Start interactive menu system
clipassgen
```

**Interactive Menu:**
```
********************************************************************************
------------------- Console Smart Password Generator v3.0.0 --------------------
---------------------------------- Main Menu: ----------------------------------
1. Smart Password (from secret)
2. Strong Random Password
3. Base Random Password
4. Authentication Code
5. Help
0. Exit
Enter your choice: 
```

### Command-Line Mode (For Scripting & Automation)

**Smart Password Generation:**
```bash
# Generate 16-character password from secret
clipassgen --smart -s "MySecureSecretPhrase@2026" -l 16

# Output example: Xk8#pLq2$Rm9@zN5*wT7 (different from v2.x.x)
```

**Random Password Generation (Unchanged):**
```bash
# Generate 20-character strong random password
clipassgen --strong -l 20

# Generate 12-character base random password
clipassgen --base -l 12
```

**Authentication Codes (Unchanged):**
```bash
# Generate 8-character authentication code
clipassgen --code -l 8
```

### Generating Public Keys
```bash
# Public keys are automatically shown in interactive mode
# Note: v3.0.0 public keys are different from v2.x.x
```

---

## Windows Standalone Executable

### Creating a Single-File *.exe

Build a standalone `clipassgen.exe` that runs without Python installation:

#### Step 1: Get the Project Files
1. **Download project ZIP:**
   - Go to: https://github.com/smartlegionlab/clipassgen
   - Click green "Code" button
   - Select "Download ZIP"
   - Extract to: `C:\clipassgen-master\`

#### Step 2: Install Python
1. Download Python installer from: https://python.org/downloads/
2. Run installer
3. **IMPORTANT:** Check "Add Python to PATH"
4. Click "Install Now"

#### Step 3: Open Command Prompt
1. Press `Win + R`
2. Type `cmd`, press Enter
3. Navigate to project folder:
   ```cmd
   cd C:\clipassgen-master
   ```

#### Step 4: Create Virtual Environment
```cmd
# Create virtual environment
python -m venv venv

# Activate it (IMPORTANT!)
.\venv\Scripts\activate

# You should see (venv) in your command prompt
```

#### Step 5: Install Dependencies
```cmd
# Install PyInstaller in virtual environment
pip install pyinstaller
pip install smartpasslib==3.0.0
```

#### Step 6: Build Executable
```cmd
# Build single .exe file
pyinstaller --onefile --console --name "clipassgen.exe" --additional-hooks-dir=. app.py

# Wait for build to complete (1-2 minutes)
```

#### Step 7: Find and Use
**Location:** `C:\clipassgen-master\dist\clipassgen.exe`

**Create desktop shortcut:**
1. Open `C:\clipassgen-master\dist\` folder
2. Right-click `clipassgen.exe`
3. Select "Create shortcut"
4. Drag shortcut to desktop
5. Rename shortcut to "CLIPassGen"
6. Double-click to start

**Run from command line:**
```cmd
C:\clipassgen-master\dist\clipassgen.exe --help
C:\clipassgen-master\dist\clipassgen.exe --smart -s "mysecret" -l 16
```

**What you get:**
- Single file: `clipassgen.exe` (~10MB)
- No Python required to run
- Works on any Windows 10/11 PC
- Can be copied to USB drive

---

## Core Components

### Generation Modes Explained

**1. Smart Password Mode:**
- **Type**: Deterministic
- **Input**: Secret phrase + Length
- **Output**: Same password for same inputs **within same major version**
- **Use Case**: Account passwords, master passwords
- **Security**: Based on secret phrase strength
- **Length Range**: 4-1000 characters
- **⚠️ v3.0.0 change**: Output differs from v2.x.x

**2. Strong Password Mode:**
- **Type**: Cryptographically random
- **Input**: Length only
- **Output**: Unique password each time
- **Use Case**: One-time passwords, temporary access
- **Security**: System cryptographic randomness
- **Length Range**: 4-1000 characters
- **✅ Unaffected by v3.0.0**

**3. Base Password Mode:**
- **Type**: Simple random
- **Input**: Length only
- **Output**: Unique password each time
- **Use Case**: Low-security applications, testing
- **Security**: Basic randomness
- **Length Range**: 4-1000 characters
- **✅ Unaffected by v3.0.0**

**4. Authentication Code Mode:**
- **Type**: Code-optimized random
- **Input**: Length only
- **Output**: Unique code each time
- **Use Case**: 2FA codes, PIN replacements
- **Security**: Character diversity optimized
- **Length Range**: 4-20 characters
- **✅ Unaffected by v3.0.0**

---

## Advanced Usage

### Scripting Integration

**Bash Script Example:**
```bash
#!/bin/bash
# Auto-generate password for service deployment

echo "Generating database password..."
DB_PASSWORD=$(clipassgen --strong -l 24)
echo "Database password: $DB_PASSWORD"

echo "Generating API secret..."
API_SECRET=$(clipassgen --smart -s "ProductionAPISecret@$(date +%Y)" -l 32)
echo "API secret generated"
```

**Python Script Integration:**
```python
import subprocess
from smartpasslib import SmartPasswordMaster

# Method 1: Using subprocess
result = subprocess.run(
    ['clipassgen', '--smart', '-s', 'mysecret', '-l', '16'],
    capture_output=True,
    text=True
)
password = result.stdout.strip()

# Method 2: Direct library usage (no CLI overhead)
password = SmartPasswordMaster.generate_smart_password(
    secret="your_secret_phrase",
    length=16
)

# Generate public key for verification
public_key = SmartPasswordMaster.generate_public_key(
    secret="your_secret_phrase"
)
```

### Workflow Examples

**Account Setup Workflow:**
```bash
# 1. Generate password for new account
clipassgen --smart -s "GitHubPersonal@2026" -l 20

# 2. Save public key for verification
# (Run interactive mode to get public key)
clipassgen
# Choose option 1, enter same secret, note public key

# 3. Use password for account creation
# Copy password from terminal to account setup form
```

### Secret Phrase Strategy

**Best Practices:**
1. **Service-specific secrets**: Different secret for each service type
2. **Pattern-based memorization**: Use consistent patterns you can remember
3. **Length matters**: Longer secrets = stronger cryptographic foundation
4. **Character diversity**: Mix uppercase, lowercase, numbers, symbols
5. **Personalization**: Include personal elements only you would know

**Example Secret Patterns:**
```
# Pattern: Service + Year + Personal Element
"GitHub2026BlueDragon@Boston"
"Email2026PurpleMoon#Seattle"
"Bank2026GoldenSun$Chicago"

# Pattern: Phrase + Service + Special
"MyFavoriteGitHubPassword@2026!"
"SecureEmailAccess#Winter2026"
"BankingPortalSecret$Fall2026"
```

**Avoid:**
- Common phrases ("password123", "letmein")
- Personal information (birthdates, names)
- Short secrets (under 12 characters)
- Dictionary words without modification

---

## Ecosystem Integration

### Part of Smart Password Suite

**Core Technology:**
- **[smartpasslib](https://github.com/smartlegionlab/smartpasslib)** - Core password generation library

**CLI Management:**
- **[CLI Smart Password Manager](https://github.com/smartlegionlab/clipassman/)** - Password metadata management

**Desktop Application:**
- **[Desktop Smart Password Manager](https://github.com/smartlegionlab/smart-password-manager-desktop)** - Graphical interface with editing

**Web Interface:**
- **[Web Smart Password Manager](https://github.com/smartlegionlab/smart-password-manager-web)** - Browser-based access

### Use Case Scenarios

**Individual Users:**
- Generate passwords for personal accounts
- Create verification keys for backup
- Generate temporary access codes

**Developers & DevOps:**
- Generate secrets for application configuration
- Create API keys and tokens
- Generate database passwords for deployments
- Automation scripts requiring secure passwords

**System Administrators:**
- Generate service account passwords
- Create temporary access credentials
- Generate SSH key passphrases
- Bulk password generation for user onboarding

---

## Version History

| Version | smartpasslib | Status | Migration Required |
|---------|--------------|--------|---------------------|
| v2.1.6 and below | v2.x.x | ❌ Deprecated/Unsupported | Must migrate to v3.0.0 |
| v3.0.0+ | v3.0.0 | ✅ Current | N/A |

---

## License

**[BSD 3-Clause License](LICENSE)**

Copyright (©) 2026, Alexander Suvorov

---

## Support

- **Generator Issues**: [GitHub Issues](https://github.com/smartlegionlab/clipassgen/issues)
- **Core Library Issues**: [smartpasslib Issues](https://github.com/smartlegionlab/smartpasslib/issues)
- **Documentation**: Interactive help and this README

**Note**: Always test password generation with non-essential accounts first. Implementation security depends on proper usage.

---

## Security Warnings

### Secret Phrase Security

**Your secret phrase is the cryptographic foundation**

1. **Permanent data loss**: Lost secret phrase = irreversible loss of all derived passwords
2. **No recovery mechanisms**: No password recovery, no secret reset, no administrative override
3. **Deterministic generation**: Identical input (secret + length) = identical output (password) **within same version**
4. **Single point of failure**: Secret phrase is the sole input for smart password generation
5. **Secure memorization required**: Digital storage of secret phrases is prohibited

**Critical**: Test password generation with non-essential accounts before production use

### Version Compatibility Notes

- **v3.0.0 smart passwords are different from v2.x.x**
- Random generation modes are unchanged
- Always verify password compatibility before upgrading critical systems

---

**Version**: 3.0.0 | [**Author**](https://smartlegionlab.ru): [Alexander Suvorov](https://alexander-suvorov.ru)

---

## Terminal Interface Examples

![clipassgen](https://github.com/smartlegionlab/clipassgen/blob/master/data/images/clipassgen.png)

### Smart Password Generation Flow
```
********************************************************************************
------------------- Console Smart Password Generator v3.0.0 --------------------
---------------------------------- Main Menu: ----------------------------------
1. Smart Password (from secret)
2. Strong Random Password
3. Base Random Password
4. Authentication Code
5. Help
0. Exit
Enter your choice: 1
--------------------------- Smart Password Generator ---------------------------

Generates password from your secret phrase.
Same secret + same length = same password every time.

Enter secret phrase (hidden): 
Confirm secret phrase (hidden): 
Enter length [4-1000] (default 16): 16
-------------------
Generated Password:
-------------------
tX3qcpEJyLfIOY!k

Length: 16 characters

Press Enter to continue... 
------------------------------
Public Key (for verification):
------------------------------
a72d11657902c5f1f603898b4a40f7d83c9505955ce3932b287ee6e938312ae5

Store this key to verify your secret later.

Press Enter to continue... 
---------------------------------- Main Menu: ----------------------------------
1. Smart Password (from secret)
2. Strong Random Password
3. Base Random Password
4. Authentication Code
5. Help
0. Exit
Enter your choice: 2
-------------------------- Strong Password Generator ---------------------------
Enter length [4-1000] (default 16): 16
-------------------
Generated Password:
-------------------
*lZ5T2tN95&psd&r

Length: 16 characters

Press Enter to continue... 
---------------------------------- Main Menu: ----------------------------------
1. Smart Password (from secret)
2. Strong Random Password
3. Base Random Password
4. Authentication Code
5. Help
0. Exit
Enter your choice: 3
--------------------------- Base Password Generator ----------------------------
Enter length [4-1000] (default 12): 16
-------------------
Generated Password:
-------------------
H0AVnlpiDWmn&br!

Length: 16 characters

Press Enter to continue... 
---------------------------------- Main Menu: ----------------------------------
1. Smart Password (from secret)
2. Strong Random Password
3. Base Random Password
4. Authentication Code
5. Help
0. Exit
Enter your choice: 4
------------------------ Authentication Code Generator -------------------------
Enter length [4-20] (default 8): 
-------------------
Generated Password:
-------------------
XX0C&fg0

Length: 8 characters

Press Enter to continue... 
---------------------------------- Main Menu: ----------------------------------
1. Smart Password (from secret)
2. Strong Random Password
3. Base Random Password
4. Authentication Code
5. Help
0. Exit
Enter your choice: 5
------------------------------------- Help -------------------------------------
-----------------
CLIPASSGEN v3.0.0
-----------------

For more information, visit the project page on GitHub: https://github.com/smartlegionlab/clipassgen/
============================================================

Press Enter to continue...
---------------------------------- Main Menu: ----------------------------------
1. Smart Password (from secret)
2. Strong Random Password
3. Base Random Password
4. Authentication Code
5. Help
0. Exit
Enter your choice: 0
---------------- https://github.com/smartlegionlab/clipassgen/ -----------------
---------- Copyright © 2026, Alexander Suvorov. All rights reserved. -----------
********************************************************************************
```

### Command Line Examples
```bash
$ clipassgen --smart -s "GitHubSecret@2026" -l 18
TAuedL5DSZUYyJoq

$ clipassgen --strong -l 24
aB3$dE6&gH9*jL1@nO4%qR7^tU0)yX2

$ clipassgen --code -l 8
XX0C&fg0
```

---

