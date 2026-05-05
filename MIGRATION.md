# Migration Guide: v2.x.x / v3.x.x to v4.0.0

> **📌 Version Note:** CliPassGen v4.0.0 uses smartpasslib v4.0.0, which introduces breaking changes from all previous versions. All smartpasslib implementations (Python, C#, JS, Go, Kotlin) now share the same algorithm.

## ⚠️ Breaking Change Notice

**CliPassGen v4.0.0 is NOT backward compatible with previous versions**

Passwords generated with older versions cannot be regenerated using v4.0.0 due to fundamental changes in the deterministic generation algorithm.

---

## Why the change?

**CliPassGen v4.0.0 (smartpasslib v4.0.0) introduces fundamental improvements:**

- **Dynamic iteration counts** — deterministic steps vary per secret (15-30 for private, 45-60 for public)
- **Expanded character set** — Google-compatible symbols (26 special chars + A-Z + a-z + 0-9)
- **Enhanced key derivation** — salt separation for public/private keys ("private"/"public")
- **Unified length validation** — password length must be 12-100 characters (was 12-1000)
- **Input validation** — secret phrases must be at least 12 characters (enforced)
- **Code length extended** — authentication codes now 4-100 characters (was 4-20)
- **Maximum security** — no secret exposure in logs or iterations

---

## What changed:

| Aspect                 | Previous versions     | v4.0.0                                |
|------------------------|-----------------------|---------------------------------------|
| Private key iterations | Fixed 30              | Dynamic 15-30                         |
| Public key iterations  | Fixed 60              | Dynamic 45-60                         |
| Key derivation salt    | None                  | "private"/"public"                    |
| Character set          | `abc...!@#$&*-_`      | `!@#$%^&*()_+-=[]{};:,.<>?/A-Za-z0-9` |
| Password max length    | 1000                  | 100                                   |
| Secret validation      | Min 4 chars           | Min 12 chars (enforced)               |
| Code max length        | 20                    | 100                                   |
| Secret in iterations   | Yes (exposed)         | No (secure)                           |

---

## Migration Steps

The migration process is the SAME for all previous versions (v2.x.x, v3.x.x):

### Step 1: Keep your secret phrases

Your secret phrases remain the same.

### Step 2: Retrieve existing passwords using old version

Before upgrading, generate all passwords you need using the old version:

```bash
# Using your current version
clipassgen --smart -s "your_secret_phrase" -l 16
```

**Save all retrieved passwords** in a safe place.

### Step 3: Upgrade to v4.0.0

```bash
pip install --upgrade clipassgen
```

### Step 4: Generate new passwords

Using the **SAME secret phrases and lengths**, generate new passwords:

```bash
clipassgen --smart -s "your_secret_phrase" -l 16
```

### Step 5: Generate new public keys

Public keys from previous versions are NOT compatible:

```bash
clipassgen --public -s "your_secret_phrase"
```

### Step 6: Update your services

Replace old passwords (from Step 2) with newly generated ones (from Step 4) on each website/service.

### Step 7: Update stored public keys

Replace old public keys in your records/backups with new ones.

### Step 8: Verify

- Log in using new passwords
- Confirm regeneration works (same secret → same password)

---

## What about random passwords?

**Random generation modes are NOT affected:**

- `--strong` — cryptographically secure random passwords (same as before)
- `--base` — simple random passwords (same as before)

Only `--smart` (deterministic) mode changed.

---

## Important Notes

- **No automatic migration** — manual password regeneration required
- **Your secret phrases remain the same**
- **Secret phrases shorter than 12 characters will now be rejected**
- **Password lengths between 101 and 1000 will now be rejected**
- **Code lengths between 21 and 100 are now allowed (was max 20)**
- **Public keys from previous versions are NOT compatible**
- **Old metadata files are NOT compatible**
- Test with non-essential accounts first

---

## Rollback

If you need to rollback to previous version:

```bash
pip install clipassgen==3.0.3
```

---

## Need Help?

- **Issues**: [GitHub Issues](https://github.com/smartlegionlab/clipassgen/issues)
- **Core Library Issues**: [smartpasslib Issues](https://github.com/smartlegionlab/smartpasslib/issues)

---

