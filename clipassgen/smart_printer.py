# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab//
# --------------------------------------------------------
import shutil


class CenteredTextDecorator:

    @classmethod
    def decorate(cls, text='', char=''):
        columns = cls._get_term_width()
        symbol = ' ' if not char else char
        msg = (f' {text} ' if text else '').center(columns, symbol[0])
        return msg

    @classmethod
    def _get_term_width(cls):
        return shutil.get_terminal_size()[0]


class FramedTextDecorator:

    @classmethod
    def decorate(cls, text='', top_char='-', bottom_char='-'):
        text_len = len(text)
        top_text = top_char * text_len
        bottom_text = bottom_char * text_len
        return f'{top_text}\n{text}\n{bottom_text}'


class SmartPrinter:

    _centered_text_decorator = CenteredTextDecorator()
    _framed_text_decorator = FramedTextDecorator()

    @classmethod
    def print_center(cls, text='', char='-'):
        print(cls._centered_text_decorator.decorate(text, char))

    @classmethod
    def print_framed(cls, text='', char='-'):
        print(cls._framed_text_decorator.decorate(text, char))

    @classmethod
    def show_head(cls, text='', top_char='*', main_char='-'):
        print(cls._centered_text_decorator.decorate(char=top_char))
        print(cls._centered_text_decorator.decorate(text=text, char=main_char))

    @classmethod
    def show_footer(cls, url='', copyright_='', top_char='-', main_char='*'):
        print(cls._centered_text_decorator.decorate(text=url, char=top_char))
        print(cls._centered_text_decorator.decorate(text=copyright_, char=top_char))
        print(cls._centered_text_decorator.decorate(char=main_char))
