# CliPassGen (Console Smart Password Generator) <sup>v4.0.0</sup>

---

**Terminal-based smart password generator with deterministic password generation. 
Generate passwords from secret phrases - same secret always produces the same password, no storage required.**

**Decentralized by Design**: Unlike traditional password managers that store encrypted vaults on central servers, 
Smart Password Generator stores nothing. Your secrets never leave your device. Passwords are regenerated on-demand — 
**no cloud, no database, no trust required**.

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

## 🔄 Breaking Change (v4.0.0)

> **⚠️ This release uses [smartpasslib](https://github.com/smartlegionlab/smartpasslib) v4.0.0, which is NOT backward compatible with v2.x.x or v3.x.x**

Smart passwords created with v2.x.x or v3.x.x **will be different** when generated with v4.0.0.

**What changed:**
- Dynamic iterations: private key 15-30 steps (was fixed 30), public key 45-60 steps (was fixed 60)
- Expanded Google-compatible character set (26 special chars + A-Z + a-z + 0-9)
- Code length extended: now 4-100 characters (was 4-20)
- Secret phrases now require minimum 12 characters
- Key derivation with salt separation ("private"/"public")
- No secret exposure in iteration logs

📖 **Full migration instructions** → see [MIGRATION.md](https://github.com/smartlegionlab/clipassgen/blob/master/MIGRATION.md)

---

## Core Principles

- **Zero-Storage Security**: No passwords or secret phrases are ever stored or transmitted
- **Decentralized Architecture**: No central servers, no cloud dependency, no third-party trust required
- **Deterministic Generation**: Same secret + same length = same password, every time
- **Memory-Based Security**: Your brain is the only password database
- **Terminal-First**: Optimized for CLI workflows and scripting
- **Multi-Mode Generation**: Smart passwords, strong random, base passwords, auth codes, public keys, verification

**What You Can Do:**
1. **Generate Smart Passwords**: Deterministic passwords from secret phrases
2. **Create Public Keys**: Verification keys for secret proof without exposure
3. **Verify Secrets**: Check if a secret matches a stored public key
4. **Generate Random Passwords**: Cryptographically secure random generation
5. **Create Authentication Codes**: Secure codes with character diversity
6. **Interactive Terminal Mode**: Menu-driven interface for easy use
7. **Command Line Mode**: Scriptable generation for automation
8. **Cross-Platform Operation**: Works on any system with Python
9. **No Dependencies**: Pure Python with smartpasslib core

## Key Features

- **Decentralized & Serverless**: No central database, no cloud lock-in, complete user sovereignty
- **Deterministic Security**: Identical input → identical output, always
- **Six Generation Modes**: Smart, Strong, Base, Code, Public Key, Verify
- **Public Key Verification**: Generate and verify keys to prove secret knowledge
- **Interactive & CLI Modes**: Both menu-driven and command-line interfaces
- **Hidden Input**: Secret phrase entry via getpass (hidden typing)
- **SmartPrinter Output**: Beautiful centered and framed terminal text
- **Length Flexibility**: 12-100 characters for passwords, 4-100 for codes
- **No Internet Required**: All cryptographic operations local

## Security Model

- **Proof of Knowledge**: Public keys verify secrets without exposing them
- **Decentralized Trust**: No third party needed — you control your secrets completely
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

Powered by **[smartpasslib](https://github.com/smartlegionlab/smartpasslib) v4.0.0+** — The core library for deterministic password generation.

**Key derivation (same as Python/JS/Kotlin/Go/C# versions v4.0.0):**

| Key Type    | Iterations              | Purpose                                               |
|-------------|-------------------------|-------------------------------------------------------|
| Private Key | 15-30 (dynamic)         | Password generation (never stored, never transmitted) |
| Public Key  | 45-60 (dynamic)         | Verification (stored locally)                         |

**Character Set (Google-compatible):**
```
!@#$%^&*()_+-=[]{};:,.<>?/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz
```

**Validation Rules:**
- Secret phrase: minimum 12 characters
- Password length: 12-100 characters
- Code length: 4-100 characters

**Decentralized Architecture**:
- No central authority required
- Metadata can be synced via any channel
- Your security depends only on your secret phrase
- Works offline — no internet connection required

**Generation Modes:**
- **Smart Password**: Deterministic from secret phrase (BREAKING CHANGE in v4.0.0)
- **Strong Password**: Cryptographically secure random generation (unchanged)
- **Base Password**: Simple random password generation (unchanged)
- **Authentication Code**: Secure code generation for 2FA/MFA (max length extended to 100)
- **Public Key**: Generate verification key from secret phrase (NEW)
- **Verify**: Check secret against stored public key (NEW)

---

## Installation

```bash
git clone https://github.com/smartlegionlab/clipassgen
cd clipassgen
python app.py
```

or

```bash
pip install clipassgen==4.0.0
```

---

## Quick Usage

### Interactive Mode
```bash
clipassgen
```

### Command-Line Mode

```bash
# Smart password (deterministic, CROSS-PLATFORM!)
clipassgen --smart -s "MyStrongSecretPhrase2026!" -l 16

# Strong random password
clipassgen --strong -l 20

# Base random password
clipassgen --base -l 16

# Authentication code (2FA) - now up to 100 chars
clipassgen --code -l 8

# Generate public key from secret
clipassgen --public -s "MyStrongSecretPhrase2026!"

# Verify secret against public key
clipassgen --verify -s "MyStrongSecretPhrase2026!" -k "public_key_here"
```

## Security Requirements

### Secret Phrase
- **Minimum 12 characters** (enforced by library)
- Case-sensitive
- Use mix of: uppercase, lowercase, numbers, symbols
- Never store digitally
- **NEVER use your password description as secret phrase**

### Strong Secret Examples
```
✅ "MyStrongSecretPhrase2026!"   — mixed case + numbers + symbols
✅ "P@ssw0rd!LongSecret"         — special chars + numbers + length
✅ "КотБегемот2026НаДиете"       — Cyrillic + numbers
```

### Weak Secret Examples (avoid)
```
❌ "short"                       — too short, rejected by library
❌ "password"                    — dictionary word, too short
❌ "1234567890"                  — only digits, too short
❌ "qwerty123"                   — keyboard pattern
```

### Password Length Requirements
- Smart/Strong/Base passwords: 12-100 characters
- Authentication codes: 4-100 characters (was 4-20)

### Decentralized Nature

**There is no "forgot password" button.** This is by design:

- No central server can reset your passwords
- No support team can recover your access
- Your secret phrase is the ONLY key

**This is the price of true decentralization** — you are completely in control.

## Cross-Platform Compatibility

CliPassGen produces **identical passwords** to:

| Platform           | Application                                                                                                                                        |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Python CLI Manager | [CLI PassMan](https://github.com/smartlegionlab/clipassman)                                                                                        |
| Desktop Python     | [Desktop Manager](https://github.com/smartlegionlab/smart-password-manager-desktop)                                                                |
| Desktop C#         | [Desktop C# Manager](https://github.com/smartlegionlab/SmartPasswordManagerCsharpDesktop)                                                          |
| CLI C# Manager     | [CLI Manager (C#)](https://github.com/smartlegionlab/SmartPasswordManagerCsharpCli)                                                                |
| CLI C# Generator   | [CLI Generator (C#)](https://github.com/smartlegionlab/SmartPasswordGeneratorCsharpCli)                                                            |
| Web                | [Web Manager](https://github.com/smartlegionlab/smart-password-manager-web)                                                                        |
| Android            | [Android Manager](https://github.com/smartlegionlab/smart-password-manager-android)                                                                |
| Core Libraries     | [smartpasslib](https://github.com/smartlegionlab/smartpasslib), [smartpasslib-csharp](https://github.com/smartlegionlab/smartpasslib-csharp), etc. |

## Ecosystem

**Core Libraries:**
- **[smartpasslib](https://github.com/smartlegionlab/smartpasslib)** - Python
- **[smartpasslib-js](https://github.com/smartlegionlab/smartpasslib-js)** - JavaScript
- **[smartpasslib-kotlin](https://github.com/smartlegionlab/smartpasslib-kotlin)** - Kotlin
- **[smartpasslib-go](https://github.com/smartlegionlab/smartpasslib-go)** - Go
- **[smartpasslib-csharp](https://github.com/smartlegionlab/smartpasslib-csharp)** - C#

**CLI Applications:**
- **[CLI Smart Password Manager (Python)](https://github.com/smartlegionlab/clipassman)**
- **[CLI Smart Password Generator (Python)](https://github.com/smartlegionlab/clipassgen)** (this)
- **[CLI Smart Password Manager (C#)](https://github.com/smartlegionlab/SmartPasswordManagerCsharpCli)**
- **[CLI Smart Password Generator (C#)](https://github.com/smartlegionlab/SmartPasswordGeneratorCsharpCli)**

**Desktop Applications:**
- **[Desktop Smart Password Manager (Python)](https://github.com/smartlegionlab/smart-password-manager-desktop)**
- **[Desktop Smart Password Manager (C#)](https://github.com/smartlegionlab/SmartPasswordManagerCsharpDesktop)**

**Other:**
- **[Web Smart Password Manager](https://github.com/smartlegionlab/smart-password-manager-web)**
- **[Android Smart Password Manager](https://github.com/smartlegionlab/smart-password-manager-android)**

## Version History

| Version          | smartpasslib | Status                   | Migration Required     |
|------------------|--------------|--------------------------|------------------------|
| v2.x.x and below | v2.x.x       | ❌ Deprecated/Unsupported | Must migrate to v4.x.x |
| v3.x.x           | v3.x.x       | ❌ Deprecated/Unsupported | Must migrate to v4.x.x |
| **v4.0.0+**      | **v4.0.0+**  | ✅ Current                | N/A                    |

## License

**[BSD 3-Clause License](https://github.com/smartlegionlab/clipassgen/blob/master/LICENSE)**

Copyright (©) 2026, Alexander Suvorov

## Support

- **Generator Issues**: [GitHub Issues](https://github.com/smartlegionlab/clipassgen/issues)
- **Core Library Issues**: [smartpasslib Issues](https://github.com/smartlegionlab/smartpasslib/issues)
- **Documentation**: Interactive help and this README

**Note**: Always test password generation with non-essential accounts first. Implementation security depends on proper usage.

---

### Main Interface

![Main Interface](https://github.com/smartlegionlab/clipassgen/raw/master/data/images/clipassgen.png)

---

