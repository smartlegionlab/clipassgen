# CLIPassGen (Console Smart Password Generator) <sup>v2.1.3</sup>

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

---

## **🔐 Core Principles:**

- 🔐 **Deterministic Generation**: Same secret + same length = same password, every time
- 🔑 **Zero Storage**: Passwords exist only when generated, never stored
- 🧠 **Memory-Based Security**: Your brain is the only password database
- 💻 **Terminal-First**: Optimized for CLI workflows and scripting
- ⚡ **Multi-Mode Generation**: Smart passwords, strong random, base passwords, and auth codes

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
- ✅ **Deterministic Security**: Identical input → identical output, always
- ✅ **Four Generation Modes**: Smart, Strong, Base, and Code
- ✅ **Public Key Verification**: Generate keys to prove secret knowledge
- ✅ **Interactive & CLI Modes**: Both menu-driven and command-line interfaces
- ✅ **Hidden Input**: Secret phrase entry via getpass (hidden typing)
- ✅ **SmartPrinter Output**: Beautiful centered and framed terminal text
- ✅ **Length Flexibility**: 4-1000 characters depending on mode
- ✅ **No Internet Required**: All cryptographic operations local

**Security Model:**
- **Proof of Knowledge**: Public keys verify secrets without exposing them
- **Deterministic Certainty**: Mathematical certainty in password regeneration
- **Ephemeral Passwords**: Passwords exist only in memory during generation
- **Local Computation**: No data leaves your terminal
- **No Recovery Backdoors**: Lost secret = permanently lost passwords (by design)

---

## ⚠️ Critical Notice

**BEFORE USING THIS SOFTWARE, READ THE COMPLETE LEGAL DISCLAIMER BELOW**

[View Legal Disclaimer & Liability Waiver](#-legal-disclaimer)

*Usage of this software constitutes acceptance of all terms and conditions.*

---

## 📚 Research Paradigms & Publications

- **[Pointer-Based Security Paradigm](https://doi.org/10.5281/zenodo.17204738)** - Architectural Shift from Data Protection to Data Non-Existence
- **[Local Data Regeneration Paradigm](https://doi.org/10.5281/zenodo.17264327)** - Ontological Shift from Data Transmission to Synchronous State Discovery

---

## 🔬 Technical Foundation

Powered by **[smartpasslib v2.1.0+](https://github.com/smartlegionlab/smartpasslib)** - The core library for deterministic password generation.

**Key principle**: Instead of storing passwords, you store verification metadata. The actual password is regenerated on-demand from your secret phrase.

**Generation Modes:**
- **Smart Password**: Deterministic from secret phrase (main feature)
- **Strong Password**: Cryptographically secure random generation
- **Base Password**: Simple random password generation
- **Authentication Code**: Secure code generation for 2FA/MFA

**Public Key System:**
- Generated from secret phrase via SHA3-512 with iterative derivation
- Can be safely stored/shared to verify secret knowledge
- No way to derive secret from public key
- Same secret always produces same public key

---

## 🆕 What's New in v2.1.3

### ⚠️ **BREAKING CHANGES WARNING**

**CRITICAL**: v2.1.3 is **NOT** backward compatible with v1.x. All passwords generated with v1.x are now **INVALID**. You must generate new passwords using your secret phrases.

### Major Improvements:

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
- **Updated cryptographic backend** to smartpasslib v2.1.0
- **Stronger public key generation** with enhanced algorithms
- **Hidden secret input** via getpass for interactive mode
- **Input validation** with helpful error messages

**User Experience:**
- **Clear migration warnings** with v1.x incompatibility notice
- **Public key display** for verification purposes
- **Length parameter flexibility** (4-1000 characters)
- **Multiple generation modes** in one tool

### Breaking Changes:

**Compatibility:**
- **NOT compatible** with v1.x password generation
- Requires **smartpasslib v2.1.0+**
- **All v1.x passwords are invalid**
- **Login parameter completely removed**

**Migration Required:**
```bash
# Important: v1.x passwords cannot be regenerated with v2.1.3
# Step 1: Recover old passwords using v1.x if needed
# Step 2: Generate new passwords with v2.1.3
# Step 3: Update all service credentials
# Step 4: Securely delete old password records
```

### New Features:

**Command-Line Interface:**
```bash
# Smart password from secret
clipassgen --smart -s "your_secret" -l 16

# Strong random password
clipassgen --strong -l 20

# Base random password
clipassgen --base -l 12

# Authentication code
clipassgen --code -l 8
```

**Interactive Mode Enhancements:**
- Menu-driven interface with four generation options
- Hidden secret input with confirmation
- Public key generation and display
- Length validation with sensible defaults

**Output Formatting:**
- Centered headers and section dividers
- Framed password display for emphasis
- Automatic terminal width adaptation
- Consistent visual styling

### Key Improvements:

1. **Simplified Workflow** - No login parameter needed
2. **Better Terminal UI** - Professional output formatting
3. **Multiple Generation Modes** - One tool for all password types
4. **Clear Migration Path** - Explicit v1.x incompatibility
5. **Enhanced Security** - Updated cryptographic foundation

---

## 📦 Installation & Quick Start

### Prerequisites
- **Python 3.7+** required
- **pip** for package management

### Quick Installation
```bash
# Install from PyPI
pip install clipassgen

# For systems with package conflicts
pip install clipassgen --break-system-packages

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

## 🚀 Quick Usage Guide

### Interactive Mode (Recommended for Beginners)
```bash
# Start interactive menu system
clipassgen

```

**Interactive Menu:**
```
********************************************************************************
------------------- Console Smart Password Generator v2.1.3 --------------------
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
clipassgen --smart -s "MySecureSecretPhrase@2025" -l 16

# Output: Xk8#pLq2$Rm9@zN5*wT7
```

**Random Password Generation:**
```bash
# Generate 20-character strong random password
clipassgen --strong -l 20

# Generate 12-character base random password
clipassgen --base -l 12
```

**Authentication Codes:**
```bash
# Generate 8-character authentication code
clipassgen --code -l 8
```

### Generating Public Keys
```bash
# Public keys are automatically shown in interactive mode
# For CLI mode, generate password first, then use smartpasslib directly
# to generate public key from the same secret
```

---

## 📦 Windows Standalone Executable

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
3. **IMPORTANT:** Check ✅ "Add Python to PATH"
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

## 🏗️ Core Components

### Generation Modes Explained

**1. Smart Password Mode:**
- **Type**: Deterministic
- **Input**: Secret phrase + Length
- **Output**: Same password for same inputs
- **Use Case**: Account passwords, master passwords
- **Security**: Based on secret phrase strength
- **Length Range**: 4-1000 characters

**2. Strong Password Mode:**
- **Type**: Cryptographically random
- **Input**: Length only
- **Output**: Unique password each time
- **Use Case**: One-time passwords, temporary access
- **Security**: System cryptographic randomness
- **Length Range**: 4-1000 characters

**3. Base Password Mode:**
- **Type**: Simple random
- **Input**: Length only
- **Output**: Unique password each time
- **Use Case**: Low-security applications, testing
- **Security**: Basic randomness
- **Length Range**: 4-1000 characters

**4. Authentication Code Mode:**
- **Type**: Code-optimized random
- **Input**: Length only
- **Output**: Unique code each time
- **Use Case**: 2FA codes, PIN replacements
- **Security**: Character diversity optimized
- **Length Range**: 4-20 characters

---

## 💡 Advanced Usage

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
clipassgen --smart -s "GitHubPersonal@2025" -l 20

# 2. Save public key for verification
# (Run interactive mode to get public key)
clipassgen
# Choose option 1, enter same secret, note public key

# 3. Use password for account creation
# Copy password from terminal to account setup form
```

**Batch Password Generation:**
```bash
#!/bin/bash
# Generate passwords for multiple services

services=("github" "email" "banking" "cloud")

for service in "${services[@]}"; do
    echo "Generating password for $service..."
    clipassgen --smart -s "${service}Secret@2025" -l 18
    echo ""
done
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
"GitHub2025BlueDragon@Boston"
"Email2025PurpleMoon#Seattle"
"Bank2025GoldenSun$Chicago"

# Pattern: Phrase + Service + Special
"MyFavoriteGitHubPassword@2025!"
"SecureEmailAccess#Winter2025"
"BankingPortalSecret$Fall2025"
```

**Avoid:**
- Common phrases ("password123", "letmein")
- Personal information (birthdates, names)
- Short secrets (under 12 characters)
- Dictionary words without modification

---

## 🔧 Ecosystem Integration

### Part of Smart Password Suite

**Core Technology:**
- **[smartpasslib](https://github.com/smartlegionlab/smartpasslib)** - Core password generation library

**CLI Management:**
- **[CLI Smart Password Manager](https://github.com/smartlegionlab/clipassman/)** - Password metadata management

**Desktop Application:**
- **[Desktop Smart Password Manager](https://github.com/smartlegionlab/smart-password-manager-desktop)** - Graphical interface with editing

**Web Interface:**
- **[Web Smart Password Manager](https://github.com/smartlegionlab/smart-password-manager)** - Browser-based access

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

### Integration Patterns

**With Configuration Management:**
```yaml
# Ansible playbook example
- name: Generate database password
  command: clipassgen --strong -l 24
  register: db_password

- name: Set database password
  postgresql_user:
    name: app_user
    password: "{{ db_password.stdout }}"
```

**With Docker & Containers:**
```dockerfile
# Dockerfile example
RUN pip install clipassgen

# Generate password during build (not recommended for secrets)
RUN clipassgen --strong -l 16 > /tmp/generated_password.txt
```

**With CI/CD Pipelines:**
```yaml
# GitHub Actions example
- name: Generate deployment secret
  run: |
    DEPLOY_SECRET=$(clipassgen --strong -l 32)
    echo "DEPLOY_SECRET=$DEPLOY_SECRET" >> $GITHUB_ENV
```

---

## 📜 License

**[BSD 3-Clause License](LICENSE)**

Copyright (c) 2025, Alexander Suvorov

```
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

---

## 🆘 Support

- **Generator Issues**: [GitHub Issues](https://github.com/smartlegionlab/clipassgen/issues)
- **Core Library Issues**: [smartpasslib Issues](https://github.com/smartlegionlab/smartpasslib/issues)
- **Documentation**: Interactive help and this README

**Note**: Always test password generation with non-essential accounts first. Implementation security depends on proper usage.

---

## ⚠️ Security Warnings

**Version Incompatibility**: v2.1.3 passwords are incompatible with v1.x.
Never mix secret phrases across different versions.

### Secret Phrase Security

**Your secret phrase is the cryptographic foundation**

1. **Permanent data loss**: Lost secret phrase = irreversible loss of all derived passwords
2. **No recovery mechanisms**: No password recovery, no secret reset, no administrative override
3. **Deterministic generation**: Identical input (secret + length) = identical output (password)
4. **Single point of failure**: Secret phrase is the sole input for smart password generation
5. **Secure memorization required**: Digital storage of secret phrases is prohibited

**Critical**: Test password generation with non-essential accounts before production use

---

## 📄 Legal Disclaimer

**COMPLETE AND ABSOLUTE RELEASE FROM ALL LIABILITY**

**SOFTWARE PROVIDED "AS IS" WITHOUT ANY WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT.**

The copyright holder, contributors, and any associated parties **EXPLICITLY DISCLAIM AND DENY ALL RESPONSIBILITY AND LIABILITY** for:

1. **ANY AND ALL DATA LOSS**: Complete or partial loss of passwords, accounts, credentials, cryptographic keys, or any data whatsoever
2. **ANY AND ALL SECURITY INCIDENTS**: Unauthorized access, data breaches, account compromises, theft, or exposure of sensitive information
3. **ANY AND ALL FINANCIAL LOSSES**: Direct, indirect, incidental, special, consequential, or punitive damages of any kind
4. **ANY AND ALL OPERATIONAL DISRUPTIONS**: Service interruptions, account lockouts, authentication failures, or denial of service
5. **ANY AND ALL IMPLEMENTATION ISSUES**: Bugs, errors, vulnerabilities, misconfigurations, or incorrect usage
6. **ANY AND ALL LEGAL OR REGULATORY CONSEQUENTS**: Violations of laws, regulations, compliance requirements, or terms of service
7. **ANY AND ALL PERSONAL OR BUSINESS DAMAGES**: Reputational harm, business interruption, loss of revenue, or any other damages
8. **ANY AND ALL THIRD-PARTY CLAIMS**: Claims made by any other parties affected by software usage

**USER ACCEPTS FULL AND UNCONDITIONAL RESPONSIBILITY**

By installing, accessing, or using this software in any manner, you irrevocably agree that:

- You assume **ALL** risks associated with software usage
- You bear **SOLE** responsibility for secret phrase management and security
- You accept **COMPLETE** responsibility for all testing and validation
- You are **EXCLUSIVELY** liable for compliance with all applicable laws
- You accept **TOTAL** responsibility for any and all consequences
- You **PERMANENTLY AND IRREVOCABLY** waive, release, and discharge all claims against the copyright holder, contributors, distributors, and any associated entities

**NO WARRANTY OF ANY KIND**

This software comes with **ABSOLUTELY NO GUARANTEES** regarding:
- Security effectiveness or cryptographic strength
- Reliability or availability
- Fitness for any particular purpose
- Accuracy or correctness
- Freedom from defects or vulnerabilities

**NOT A SECURITY PRODUCT OR SERVICE**

This is experimental software. It is not:
- Security consultation or advice
- A certified cryptographic product
- A guaranteed security solution
- Professional security software
- Endorsed by any security authority

**FINAL AND BINDING AGREEMENT**

Usage of this software constitutes your **FULL AND UNCONDITIONAL ACCEPTANCE** of this disclaimer. If you do not accept **ALL** terms and conditions, **DO NOT USE THE SOFTWARE.**

**BY PROCEEDING, YOU ACKNOWLEDGE THAT YOU HAVE READ THIS DISCLAIMER IN ITS ENTIRETY, UNDERSTAND ITS TERMS COMPLETELY, AND ACCEPT THEM WITHOUT RESERVATION OR EXCEPTION.**

---

**Version**: 2.1.3 | [**Author**](https://smartlegionlab.ru): [Alexander Suvorov](https://alexander-suvorov.ru)

---

**Note**: This is v2.1.3. If migrating from v1.x, all passwords must be regenerated with new secret phrases.

---

## Terminal Interface Examples

![clipassgen](https://github.com/smartlegionlab/clipassgen/blob/master/data/images/clipassgen.png)

### Smart Password Generation Flow
```
********************************************************************************
------------------- Console Smart Password Generator v2.1.3 --------------------
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
wcJjBKIhsgV%!6Iq

Length: 16 characters

Press Enter to continue... 
------------------------------
Public Key (for verification):
------------------------------
d8295cdc1a8e3094529e623718e6307da97c3aec7e313de786095de80796a6e0ebf8d356682e58eeb0279eb7cd9d04d75714548dcbe6733ebb4b558bf7d70b4b

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
I^wiCnKbM6P&87Ow

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
Enter length [4-1000] (default 12): 12
-------------------
Generated Password:
-------------------
_exe$bSNA4hn

Length: 12 characters

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
Enter length [4-20] (default 8): 8
-------------------
Generated Password:
-------------------
fGa80P3@

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
CLIPASSGEN v2.1.3
-----------------
WARNING: 
• Login parameter removed
• All v1.x passwords are INVALID
• Only secret phrase needed

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
---------- Copyright © 2025, Alexander Suvorov. All rights reserved. -----------
********************************************************************************
```

### Command Line Examples
```bash
$ clipassgen --smart -s "GitHubSecret@2025" -l 18
&EQAAA_653Lv68%LnQ

$ clipassgen --strong -l 24
aB3$dE6&gH9*jL1@nO4%qR7^tU0)yX2

$ clipassgen --code -l 8
K8P3L9M2
```
