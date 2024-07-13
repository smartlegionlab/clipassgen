# clipassgen <sup>v0.6.2</sup>

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

## What's new:

- Added the ability to launch an application with additional parameters.

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
linked to login and secret phrase.
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
> enter the secret phrase and receive a generated smart password: [clipassman](https://github.com/smartlegionlab/clipassman/)

> Passwords generated and saved in clipassman will be identical to passwords generated in clipassgen.

***

## Help:

### Install and use:

`pip install clipassgen`
- `clipassgen`

> On some systems, when running the command `pip install clipassgen` an error occurs, you can solve it like this `pip install clipassgen --break-system-packages`

or:

- Download.
- Unzip.
- `python app.py`
- `python app.py -l 10`
- `python app.py -l 10 -s "secret phrase"`
- `python app.py -l 10 -s "secret phrase" -l "login or name"`

***

## Disclaimer of liability:

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

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2024, A.A. Suvorov
    All rights reserved.
    --------------------------------------------------------
