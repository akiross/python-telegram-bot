#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2016
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
"""This module contains a object that represents a Telegram File."""

from os.path import basename

from telegram import TelegramObject


class File(TelegramObject):
    """This object represents a Telegram File.

    Attributes:
        file_id (str):
        file_size (str):
        file_path (str):

    Args:
        file_id (str):
        bot (telegram.Bot):
        **kwargs: Arbitrary keyword arguments.

    Keyword Args:
        file_size (Optional[int]):
        file_path (Optional[str]):

    """

    def __init__(self, file_id, bot, **kwargs):
        # Required
        self.file_id = str(file_id)

        # Optionals
        self.file_size = int(kwargs.get('file_size', 0))
        self.file_path = str(kwargs.get('file_path', ''))

        self.bot = bot

    @staticmethod
    def de_json(data, bot):
        """
        Args:
            data (dict):
            bot (telegram.Bot):

        Returns:
            telegram.File:
        """
        if not data:
            return None

        return File(bot=bot, **data)

    def download(self, custom_path=None):
        """
        Args:
            custom_path (str):

        """
        url = self.file_path

        if custom_path:
            filename = custom_path
        else:
            filename = basename(url)

        self.bot.request.download(url, filename)

    def download_to(self, file_object):
        """
        Args:
            file_object (file-like):

        """
        url = self.file_path
        
        self.bot.request.download_to(url, file_object)
