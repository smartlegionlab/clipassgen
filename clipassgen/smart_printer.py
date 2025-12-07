# Copyright © 2025, Alexander Suvorov
import shutil


class CenteredTextDecorator:

    @classmethod
    def decorate(cls, text='', symbol=''):
        columns = cls._get_term_width()
        symbol = ' ' if not symbol else symbol
        msg = (f' {text} ' if text else '').center(columns, symbol[0])
        return msg

    @classmethod
    def _get_term_width(cls):
        return shutil.get_terminal_size()[0]


class FramedTextDecorator:

    @classmethod
    def decorate(cls, text='', top_symbol='-', bottom_symbol='-'):
        text_len = len(text)
        top_text = top_symbol * text_len
        bottom_text = bottom_symbol * text_len
        return f'{top_text}\n{text}\n{bottom_text}'


class SmartPrinter:
    centred_text_decorator = CenteredTextDecorator()
    framed_text_decorator = FramedTextDecorator()

    @classmethod
    def print_center(cls, text='', symbol='-'):
        print(cls.centred_text_decorator.decorate(text, symbol))

    @classmethod
    def print_framed(cls, text='', symbol='-'):
        print(cls.framed_text_decorator.decorate(text, symbol))

    @classmethod
    def show_head(cls, text='', top_symbol='*', main_symbol='-'):
        print(cls.centred_text_decorator.decorate(symbol=top_symbol))
        print(cls.centred_text_decorator.decorate(text=text, symbol=main_symbol))

    @classmethod
    def show_footer(cls, url='', copyright_='', top_symbol='-', main_symbol='*'):
        print(cls.centred_text_decorator.decorate(text=url, symbol=top_symbol))
        print(cls.centred_text_decorator.decorate(text=copyright_, symbol=top_symbol))
        print(cls.centred_text_decorator.decorate(symbol=main_symbol))
