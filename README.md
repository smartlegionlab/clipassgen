# clipassgen <sup>v0.7.7</sup>

***

## Short Description:
___clipassgen___ - Console Smart Passwords Generator. Cross-platform console utility for generating cryptographically strong, recoverable, smart passwords.

***

![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/clipassgen)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/clipassgen?label=pypi%20downloads)](https://pypi.org/project/clipassgen/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/clipassgen)](https://github.com/smartlegionlab/clipassgen/)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/clipassgen)](https://github.com/smartlegionlab/clipassgen/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/clipassgen)](https://pypi.org/project/clipassgen)
[![PyPI - Format](https://img.shields.io/pypi/format/clipassgen)](https://pypi.org/project/clipassgen)
[![GitHub Repo stars](https://img.shields.io/github/stars/smartlegionlab/clipassgen?style=social)](https://github.com/smartlegionlab/clipassgen/)
[![GitHub watchers](https://img.shields.io/github/watchers/smartlegionlab/clipassgen?style=social)](https://github.com/smartlegionlab/clipassgen/)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/clipassgen?style=social)](https://github.com/smartlegionlab/clipassgen/)

[![PyPI Downloads](https://static.pepy.tech/badge/clipassgen)](https://pepy.tech/projects/clipassgen)
[![PyPI Downloads](https://static.pepy.tech/badge/clipassgen/month)](https://pepy.tech/projects/clipassgen)
[![PyPI Downloads](https://static.pepy.tech/badge/clipassgen/week)](https://pepy.tech/projects/clipassgen)

***

Author and developer: ___A.A. Suvorov___

***

## Supported:

- Linux: All.
- Windows: 7/8/10.
- Termux (Android).

***

## Images:

![logo](https://github.com/smartlegionlab/clipassgen/raw/master/data/images/clipassgen.png)

***

## Description:

___clipassgen___ - Console Smart Passwords Generator.

> Smart passwords are not stored anywhere - they are generated on the fly. For a combination - login + secret phrase, or only using a secret phrase, 
> you will always receive the same password from 10 to 1000 characters.
> This is as safe as possible. Your passwords are not stored anywhere, they are generated on the fly when requested.

Possibilities:

- Generate smart passwords using the combination: login + secret phrase.
- Generate smart passwords using a secret phrase.
- Generate common complex passwords.

Smart Password generator (login + secret phrase):

Generates a recoverable smart password
linked to login or name and secret phrase.
To generate and restore, you need to remember
login and secret phrase.

Smart Password Generator (secret phrase):

Recoverable password generator.
The password will be linked to a secret phrase.
The password is not stored anywhere and is generated on the fly.
To generate or recover a password, you only 
need to remember the secret phrase.

Base Password Generator:

A common password generator.
When generated, the password will always be different.
It will be impossible to restore it.

***

> Console manager of smart passwords that are not stored anywhere and are generated on the fly. 
> Only the public key, login and password length are stored. 
> You store the smart password under the desired login or just a name, and when received, 
> enter the secret phrase and receive a generated smart password: [clipassman](https://github.com/smartlegionlab/clipassman/).

> Passwords generated and saved in clipassman will be identical to passwords generated in clipassgen.


To create your own smart password generator apps, you can use the library: [smartpasslib](https://github.com/smartlegionlab/smartpasslib/).

***

## Help:

### Install and use:

`pip install clipassgen`

`clipassgen`

On some systems, when running the command `pip install clipassgen` an error occurs, you can solve 
it like this 

`pip install clipassgen --break-system-packages`

`clipassgen`

or:

- Download.
- Unzip.
- `python app.py`
- `python app.py -n 10`
- `python app.py -n 10 -s "secret phrase"`
- `python app.py -n 10 -s "secret phrase" -l "login or name"`

***

## 📜 License & Disclaimer

This project is licensed under the **GNU Affero General Public License v3.0 (AGPLv3)**.

- You are free to use, modify, and distribute this software.
- **However, if you modify this software and run it as a hosted service (e.g., a web app), you MUST make the full source code of your modified version available to your users under the same license.**
- The full license text can be found in the [LICENSE](https://github.com/smartlegionlab/clipassgen/blob/master/LICENSE) file.

### ⚠️ Important Disclaimer

> **THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.**
>
> *(This is a summary of the full disclaimer, which is legally binding and located in sections 15 and 16 of the AGPLv3 license).*

For commercial use that is not compatible with the AGPLv3 terms (e.g., including this software in a proprietary product without disclosing the source code), a **commercial license** is required. Please contact me at [smartlegiondev@gmail.com](mailto:smartlegiondev@gmail.com) to discuss terms.