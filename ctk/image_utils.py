#!/usr/bin/env python
# coding: utf-8

# Copyright 2011 Álvaro Justen [alvarojusten at gmail dot com]
# License: GPL <http://www.gnu.org/copyleft/gpl.html>

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class ImageText(object):
    def __init__(self, draw:ImageDraw.ImageDraw, sz:tuple[int, int], font:ImageFont.FreeTypeFont):
        self.draw = draw
        self.box_width = sz[0]
        self.box_height = sz[1]
        self.encoding = 'uff-8'
        self.font = font

    def simple_write_text_box(self, pos:tuple[int, int], text:str, ident:str='', color=(0, 0, 0)):
        x, y = pos

        lines = []
        line = []

        place = 'left'
        justify_last_line = False

        words = text.split()
        for word in words:
            if len(lines) == 0:
                new_line = ' '.join(line + [word])
            elif len(ident) > 0:
                new_line = ident + ' '.join(line + [word])
            else:
                new_line = ' '.join(line + [word])
            size = self.get_text_size(self.font, new_line)
            text_height = size[1]
            if size[0] <= self.box_width:
                line.append(word)
            else:
                lines.append(line)
                line = [ident, word]
        if line:
            lines.append(line)
        lines = [' '.join(line) for line in lines if line]
        height = y
        for index, line in enumerate(lines):
            height += text_height
            if place == 'left':
                self.write_text((x, height), line, self.font, color)
            elif place == 'right':
                total_size = self.get_text_size(self.font, line)
                x_left = x + self.box_width - total_size[0]
                self.write_text((x_left, height), line, self.font, color)
            elif place == 'center':
                total_size = self.get_text_size(self.font, line)
                x_left = int(x + ((self.box_width - total_size[0]) / 2))
                self.write_text((x_left, height), line, self.font, color)
            elif place == 'justify':
                words = line.split()
                if (index == len(lines) - 1 and not justify_last_line) or \
                    len(words) == 1:
                    self.write_text((x, height), line, self.font,
                                    color)
                    continue
                line_without_spaces = ''.join(words)
                total_size = self.get_text_size(self.font,
                                                line_without_spaces)
                space_width = (self.box_width - total_size[0]) / (len(words) - 1.0)
                start_x = x
                for word in words[:-1]:
                    self.write_text((start_x, height), word, self.font, color)
                    word_size = self.get_text_size(self.font,
                                                    word)
                    start_x += word_size[0] + space_width
                last_word_size = self.get_text_size(self.font,
                                                    words[-1])
                last_word_x = x + self.box_width - last_word_size[0]
                self.write_text((last_word_x, height), words[-1], self.font, color)
        return (self.box_width, height - y)

    def get_text_size(self, font:ImageFont.FreeTypeFont, text:str):
        ascent, descent = font.getmetrics()
        return (font.getlength(text), (ascent + descent))

    def write_text(self, pos:tuple[float, float], text, font, color=(0, 0, 0)):
        text_size = self.get_text_size(self.font, text)

        x, y = pos
        self.draw.text((x, y), text, font=font, fill=color)
        return text_size

"""
    def get_font_size(self, text, font, max_width=None, max_height=None):
        if max_width is None and max_height is None:
            raise ValueError('You need to pass max_width or max_height')
        font_size = 1
        text_size = self.get_text_size(font, font_size, text)
        if (max_width is not None and text_size[0] > max_width) or \
           (max_height is not None and text_size[1] > max_height):
            raise ValueError("Text can't be filled in only (%dpx, %dpx)" % \
                    text_size)
        while True:
            if (max_width is not None and text_size[0] >= max_width) or \
               (max_height is not None and text_size[1] >= max_height):
                return font_size - 1
            font_size += 1
            text_size = self.get_text_size(font, font_size, text)

    def write_text(self, (x, y), text, font, color=(0, 0, 0), max_width=None, max_height=None):
        if isinstance(text, str):
            #text = text.decode(self.encoding)
            text = text
        if font_size == 'fill' and \
           (max_width is not None or max_height is not None):
            font_size = self.get_font_size(text, font_filename, max_width,
                                           max_height)
        text_size = self.get_text_size(self.font, text)
        font = ImageFont.truetype(self.font)
        if x == 'center':
            x = (self.size[0] - text_size[0]) / 2
        if y == 'center':
            y = (self.size[1] - text_size[1]) / 2
        self.draw.text((x, y), text, font=font, fill=color)
        return text_size

    
    def write_text_box(self, (x, y), text, box_width, font_filename,
                       font_size=11, color=(0, 0, 0), place='left',
                       justify_last_line=False):
        lines = []
        line = []
        words = text.split()
        for word in words:
            new_line = ' '.join(line + [word])
            size = self.get_text_size(self.font, new_line)
            text_height = size[1]
            if size[0] <= box_width:
                line.append(word)
            else:
                lines.append(line)
                line = [word]
        if line:
            lines.append(line)
        lines = [' '.join(line) for line in lines if line]
        height = y
        for index, line in enumerate(lines):
            height += text_height
            if place == 'left':
                self.write_text((x, height), line, self.font,
                                color)
            elif place == 'right':
                total_size = self.get_text_size(self.font, line)
                x_left = x + box_width - total_size[0]
                self.write_text((x_left, height), line, font_filename,
                                font_size, color)
            elif place == 'center':
                total_size = self.get_text_size(self.font, line)
                x_left = int(x + ((box_width - total_size[0]) / 2))
                self.write_text((x_left, height), line, font_filename,
                                font_size, color)
            elif place == 'justify':
                words = line.split()
                if (index == len(lines) - 1 and not justify_last_line) or \
                   len(words) == 1:
                    self.write_text((x, height), line, self.font,
                                    color)
                    continue
                line_without_spaces = ''.join(words)
                total_size = self.get_text_size(self.font,
                                                line_without_spaces)
                space_width = (box_width - total_size[0]) / (len(words) - 1.0)
                start_x = x
                for word in words[:-1]:
                    self.write_text((start_x, height), word, font_filename,
                                    font_size, color)
                    word_size = self.get_text_size(self.font,
                                                    word)
                    start_x += word_size[0] + space_width
                last_word_size = self.get_text_size(self.font,
                                                    words[-1])
                last_word_x = x + box_width - last_word_size[0]
                self.write_text((last_word_x, height), words[-1], font_filename,
                                font_size, color)
        return (box_width, height - y)
"""        