# clipassgen <sup>v1.1.1</sup>

[![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/clipassgen)](https://github.com/smartlegionlab/clipassgen)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/clipassgen?label=pypi%20downloads)](https://pypi.org/project/clipassgen/)
[![GitHub release](https://img.shields.io/github/v/release/smartlegionlab/clipassgen)](https://github.com/smartlegionlab/clipassgen/)
[![GitHub license](https://img.shields.io/github/license/smartlegionlab/clipassgen)](https://github.com/smartlegionlab/clipassgen/blob/master/LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/clipassgen)](https://pypi.org/project/clipassgen)
[![PyPI format](https://img.shields.io/pypi/format/clipassgen)](https://pypi.org/project/clipassgen)

[![PyPI Downloads](https://static.pepy.tech/badge/clipassgen)](https://pepy.tech/projects/clipassgen)
[![PyPI Monthly Downloads](https://static.pepy.tech/badge/clipassgen/month)](https://pepy.tech/projects/clipassgen)
[![PyPI Weekly Downloads](https://static.pepy.tech/badge/clipassgen/week)](https://pepy.tech/projects/clipassgen)

## 🖥️ Console Smart Password Generator

A cross-platform command-line utility for generating cryptographically strong, recoverable smart passwords using deterministic cryptography. Part of the smart password ecosystem built on revolutionary password management principles.

> **Powered by** [smartpasslib](https://github.com/smartlegionlab/smartpasslib) - The core deterministic password generation library

## 🌟 Key Features

- 🔒 **Zero Storage** - Passwords generated on-demand, never stored
- 🔄 **Deterministic Generation** - Same inputs always produce identical passwords
- 📱 **Cross-Platform** - Works on Linux, Windows, macOS, and Android (Termux)
- ⚡ **Instant Generation** - Generate passwords directly from command line
- 🔐 **Multiple Modes** - Support for different generation strategies
- 🎯 **Cryptographically Secure** - Uses SHA3-512 and system entropy

## 🌌 The Paradox at the Core

This tool embodies a beautiful cryptographic paradox: **perfect reproducibility meets complete unpredictability**. 

The system is both:
- **Perfectly reproducible** - Identical inputs (login + secret phrase) will always generate the exact same password, every time, on any device
- **Completely unpredictable** - Without the exact inputs, the output is computationally impossible to guess or reverse-engineer

This paradox is powered by deterministic cryptography - the same revolutionary concept explored in our foundational articles:
- [**The Password That Never Was**](https://dev.to/smartlegionlab/the-password-that-never-was-how-to-access-secrets-that-were-always-there-smart-password-library-4h16) - How passwords emerge from mathematical space rather than being created
- [**Chrono-Library Messenger**](https://dev.to/smartlegionlab/i-created-a-messenger-that-doesnt-send-any-data-heres-how-it-works-4ecp) - The cryptographic framework enabling this paradigm
- [**Messages That Have Always Been With Us**](https://dev.to/smartlegionlab/the-magic-of-messages-that-have-always-been-with-us-48gp) - Philosophical foundation of pre-existing information

Your passwords don't need to be stored because they were never created - they already exist as mathematical certainties, waiting to be discovered through the correct combination of login and secret phrase.

## 📦 Installation

```bash
pip install clipassgen
```

For systems with package conflicts:
```bash
pip install clipassgen --break-system-packages
```

## 🚀 Quick Start

### Interactive Mode
```bash
clipassgen
```

### Command-Line Options
```bash
# Generate smart password with login and secret phrase
clipassgen -l "your_login" -s "your_secret_phrase" -n 16

# Generate using only secret phrase
clipassgen -s "your_secret_phrase" -n 14

# Generate base password (random)
clipassgen -n 12
```

## 🎯 Generation Modes

### 1. Smart Password (Login + Secret Phrase)
```bash
clipassgen -l "alice@example.com" -s "mySecret123" -n 16
# Output: 'xT8$kL9!pQ2sM3c@n'
```

### 2. Smart Password (Secret Phrase Only)
```bash
clipassgen -s "myUniversalSecret" -n 14
# Output: 'M3c@n1cL4mp$h4d'
```

### 3. Base Password (Random)
```bash
clipassgen -n 12
# Output: 'r4nD0m!P@ssw' (different each time)
```

## 🔧 Advanced Usage

### Batch Generation
```bash
# Generate multiple passwords for different services
clipassgen -l "github" -s "main_secret" -n 20
clipassgen -l "email" -s "main_secret" -n 18
clipassgen -l "banking" -s "main_secret" -n 22
```

### Integration with Scripts
```bash
#!/bin/bash
# Automate password generation in scripts
PASSWORD=$(clipassgen -l "$1" -s "$2" -n 16)
echo "Generated password: $PASSWORD"
```

## 🏗️ Technical Foundation

### How It Works
- **Deterministic Algorithm**: Same inputs (login + secret) always produce identical output
- **Cryptographic Hashing**: Uses SHA3-512 for secure one-way generation
- **System Entropy**: Incorporates system randomness for additional security
- **Zero Storage**: No passwords are stored - everything is generated on-demand

### Recovery Process
Your passwords can always be regenerated using the same:
- Login/identifier
- Secret phrase
- Password length

## 🔄 Ecosystem Integration

### Complementary Tools
- [**CLI PassMan**](https://github.com/smartlegionlab/clipassman/) - Console password manager for smart passwords
- [**SmartPassLib**](https://github.com/smartlegionlab/smartpasslib/) - Core Python library for password generation
- [**Desktop Manager**](https://github.com/smartlegionlab/smart-password-manager-desktop) - Graphical interface
- [**Web Manager**](https://github.com/smartlegionlab/smart-password-manager) - Web-based interface

### Consistency Guarantee
Passwords generated with clipassgen are identical to those generated by other ecosystem tools when using the same inputs.

## 📖 Learn More

Understand the revolutionary concept behind this technology:

1. [**The Password That Never Was**](https://dev.to/smartlegionlab/the-password-that-never-was-how-to-access-secrets-that-were-always-there-smart-password-library-4h16) - Deterministic password generation principles
2. [**Chrono-Library Messenger**](https://dev.to/smartlegionlab/i-created-a-messenger-that-doesnt-send-any-data-heres-how-it-works-4ecp) - Underlying cryptographic framework
3. [**Technical Implementation**](https://dev.to/smartlegionlab/the-magic-of-messages-that-have-always-been-with-us-48gp) - Architecture details

## 🛡️ Security Features

- **No Password Storage** - Eliminates risk of password database breaches
- **Local Generation** - All processing happens on your local machine
- **Cryptographic Security** - Industry-standard SHA3-512 hashing
- **Deterministic Yet Secure** - Reproducible without being predictable

## 🤝 Supported Platforms

- **Linux** - All major distributions
- **Windows** - 7, 8, 10, 11
- **macOS** - Fully supported
- **Android** - Via Termux

## 🐛 Troubleshooting

### Common Issues
```bash
# If 'clipassgen' command not found:
python -m clipassgen

# Alternative direct execution:
python -m clipassgen.app
```

### Manual Installation
```bash
# Clone and run manually
git clone https://github.com/smartlegionlab/clipassgen.git
cd clipassgen
python app.py
python app.py -n 10 -s "secret" -l "login"
```

## 📜 License

BSD 3-Clause License

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

## 🌟 Professional Password Generation

Experience the future of password management with deterministic security. Generate strong, recoverable passwords without the risks of traditional storage.

**Ready to enhance your security workflow?** [Install clipassgen](https://pypi.org/project/clipassgen/) today and join developers worldwide using smart password technology.

---

*Explore more professional tools at [Smart Legion Lab](https://github.com/smartlegionlab)*

![CLI Interface](https://github.com/smartlegionlab/clipassgen/raw/master/data/images/clipassgen.png)
