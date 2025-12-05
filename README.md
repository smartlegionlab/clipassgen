# clipassgen (Console Smart Password Generator CLI) <sup>v2.0.0</sup>

---

> **Command-line smart password generator** for deterministic password generation - same secret always produces the same password.

---

[![PyPI - Downloads](https://img.shields.io/pypi/dm/clipassgen?label=pypi%20downloads)](https://pypi.org/project/clipassgen/)
[![PyPI Downloads](https://static.pepy.tech/badge/clipassgen)](https://pepy.tech/projects/clipassgen)
[![PyPI Weekly Downloads](https://static.pepy.tech/badge/clipassgen/week)](https://pepy.tech/projects/clipassgen)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/clipassgen)
[![GitHub release](https://img.shields.io/github/v/release/smartlegionlab/clipassgen)](https://github.com/smartlegionlab/clipassgen/)
[![PyPI version](https://img.shields.io/pypi/v/clipassgen)](https://pypi.org/project/clipassgen)
[![GitHub license](https://img.shields.io/github/license/smartlegionlab/clipassgen)](https://github.com/smartlegionlab/clipassgen/blob/master/LICENSE)
[![PyPI format](https://img.shields.io/pypi/format/clipassgen)](https://pypi.org/project/clipassgen)

## 🖥️ Console Smart Password Generator

Cross-platform command-line utility for generating deterministic passwords and verification keys.

> **Powered by** [smartpasslib v2.0.0](https://github.com/smartlegionlab/smartpasslib) - The core library for deterministic password generation

### ⚠️ **BREAKING CHANGES in v2.0.0**

**WARNING:** This version introduces breaking changes:
- **Login parameter removed** - now uses only secret phrase
- All passwords generated with v1.x are now **INVALID**
- **Simplified API** - single type of smart password generation
- **New cryptographic algorithm** - different from v1.x

---

## 📦 Installation

### Standard Installation
```bash
pip install clipassgen
```

### For Systems with Package Conflicts
```bash
pip install clipassgen --break-system-packages
```

### Manual Installation
```bash
# Clone and install from source
git clone https://github.com/smartlegionlab/clipassgen.git
cd clipassgen
pip install -e .
```

---

## 🚀 Quick Start

### Interactive Mode
```bash
clipassgen
```
Launches interactive terminal with menu selection.

### Generate Smart Password (CLI)
```bash
# Generate password from secret phrase
clipassgen --smart -s "your_secret_phrase" -l 16

# Generate strong random password
clipassgen --strong -l 20

# Generate authentication code
clipassgen --code -l 8
```

---

## 🎯 Key Features

### Deterministic Generation
- **Same secret + same length = same password** - every time
- **Mathematical certainty** - passwords are calculated from your secret
- **No storage required** - passwords exist only when generated

### Multiple Generation Types
- **Smart Passwords** - Deterministic from secret phrase
- **Strong Passwords** - Cryptographically secure random
- **Base Passwords** - Simple random passwords
- **Authentication Codes** - Secure codes with character diversity

### Security by Design
- **No password storage** - eliminates breach risk
- **Local processing** - all operations on your machine
- **Public key verification** - verify secrets without revealing them
- **Case-sensitive secrets** - enhanced security

---

## ⚙️ How It Works

### Smart Password Generation
1. **Input**: Secret phrase + Length
2. **Process**: Cryptographic hashing and deterministic seeding
3. **Output**: Identical password for identical inputs

### Public Key Generation
1. **Input**: Secret phrase
2. **Process**: SHA3-512 hashing with iterative key derivation
3. **Output**: Verification key (safe to store/share)

### Verification
- **Public key** can verify secret knowledge without revealing secret
- **Same secret** always produces same public key
- **No way** to derive secret from public key

---

## 💻 Usage Examples

### Basic Generation
```bash
# Generate smart password (14 characters)
clipassgen --smart -s "myStrongSecret123" -l 14

# Generate strong password (16 characters)
clipassgen --strong -l 16

# Generate authentication code (6 characters)
clipassgen --code -l 6
```

### Advanced Usage
```bash
# Generate multiple passwords
clipassgen --smart -s "githubSecret" -l 20
clipassgen --smart -s "emailSecret" -l 18
clipassgen --smart -s "bankSecret" -l 22
```

---

## 🔄 Smart Password Ecosystem

This generator is part of a comprehensive suite of applications built on deterministic password technology:

### 🛠️ Console Applications
- **CLI Smart Password Generator** (this tool) - Password generation
- [**CLI Smart Password Manager**](https://github.com/smartlegionlab/clipassman/) - Smart Password Manager CLI

### 🖥️ Desktop Applications
- [**Desktop Smart Password Manager**](https://github.com/smartlegionlab/smart-password-manager-desktop) - Graphical interface

### 🌐 Web Applications
- [**Web Smart Password Manager**](https://github.com/smartlegionlab/smart-password-manager) - Browser-based interface

### 💡 Core Technology
- [**SmartPassLib v2.0.0**](https://github.com/smartlegionlab/smartpasslib) - Core password generation library

---

## 🛡️ Security Features

### What Makes It Secure:
- **Zero Password Storage** - Passwords exist only in memory
- **Deterministic Generation** - Reproducible without being predictable
- **Cryptographic Foundation** - SHA3-512 with iterative key derivation
- **Local Execution** - No data transmission or cloud dependency

### Protection Against:
- **Database Breaches** - No password database to steal
- **Keyloggers** - Interactive mode hides secret input
- **Shoulder Surfing** - Hidden input for sensitive operations
- **Memory Scraping** - Passwords exist briefly in memory

---

## 📋 Migration from v1.x

### Critical Information:
- **v2.0.0 is NOT compatible** with v1.x passwords
- **All v1.x passwords are invalid** in v2.0.0
- **New passwords required** for all services

### Migration Process:
1. **Identify** services using v1.x passwords
2. **Recover** passwords using v1.x if needed
3. **Generate** new passwords with v2.0.0
4. **Update** service credentials
5. **Securely delete** old password records

### Why These Changes?
- **Simplified API** - Single secret parameter
- **Enhanced Security** - Improved cryptographic algorithms
- **Better UX** - Clearer interface and error messages
- **Future-proof** - Clean architecture for development

---

## 🐛 Troubleshooting

### Common Issues:

**"Module not found" errors:**
```bash
# Reinstall package
pip install --force-reinstall clipassgen

# Verify Python version (requires 3.7+)
python --version
```

**Password generation errors:**
- Verify secret phrase is correct (case-sensitive)
- Check password length (4-1000 characters)
- Ensure proper terminal encoding

**Interactive mode issues:**
```bash
# Clear terminal and retry
clear && clipassgen  # Linux/macOS
```

### Getting Help:
1. Check [GitHub Issues](https://github.com/smartlegionlab/clipassgen/issues)
2. Review [smartpasslib documentation](https://github.com/smartlegionlab/smartpasslib)
3. Submit new issue with detailed error information

---

## 📜 License

**BSD 3-Clause License**

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

## 🔗 Links & Resources

- **GitHub Repository**: [clipassgen](https://github.com/smartlegionlab/clipassgen)
- **Core Library**: [smartpasslib](https://github.com/smartlegionlab/smartpasslib)
- **Issues & Support**: [GitHub Issues](https://github.com/smartlegionlab/clipassgen/issues)
- **PyPI Package**: [clipassgen on PyPI](https://pypi.org/project/clipassgen/)
- **Academic Research**: [Pointer-Based Security Paradigm](https://doi.org/10.5281/zenodo.17204738)
- **Extended Research**: [Local Data Regeneration Paradigm](https://doi.org/10.5281/zenodo.17264327)

---

## ⚠️ Important Notes

**Secret Phrase Security:**
- Your secret phrase is **never stored** by the system
- **Memorize it securely** - it cannot be recovered if lost
- Use **different secrets** for different security levels
- Consider using **passphrase techniques** for better memorability

**Password Management:**
- clipassgen is a **generator**, not a password manager
- For password management, use [clipassman](https://github.com/smartlegionlab/clipassman)
- Always **test passwords** before relying on them
- Keep **backup access methods** for critical accounts

**Legal Disclaimer:**
The security of generated passwords depends on proper usage, including secret phrase strength and operational security practices. The developers assume no liability for password security breaches resulting from improper use.

![CLI Interface](https://github.com/smartlegionlab/clipassgen/raw/master/data/images/clipassgen.png)
