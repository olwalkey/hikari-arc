from .base import CallableCommandBase, CallableCommandProto, CommandBase, CommandProto
from .message import MessageCommand, message_command
from .option import (
    AttachmentOption,
    AttachmentParams,
    ChannelOption,
    ChannelParams,
    CommandOptionBase,
    FloatOption,
    FloatParams,
    IntOption,
    IntParams,
    MentionableOption,
    MentionableParams,
    Option,
    OptionParams,
    OptionWithChoices,
    OptionWithChoicesParams,
    RoleOption,
    RoleParams,
    StrOption,
    StrParams,
    UserOption,
    UserParams,
)
from .slash import (
    SlashCommand,
    SlashCommandLike,
    SlashGroup,
    SlashSubCommand,
    SlashSubGroup,
    slash_command,
    slash_subcommand,
)
from .user import UserCommand, user_command

__all__ = (
    "CommandBase",
    "CommandProto",
    "CallableCommandBase",
    "CallableCommandProto",
    "SlashCommand",
    "SlashCommandLike",
    "SlashGroup",
    "SlashSubCommand",
    "SlashSubGroup",
    "slash_command",
    "slash_subcommand",
    "CommandOptionBase",
    "Option",
    "IntOption",
    "StrOption",
    "OptionParams",
    "OptionWithChoices",
    "OptionWithChoicesParams",
    "IntParams",
    "StrParams",
    "FloatOption",
    "FloatParams",
    "UserOption",
    "UserParams",
    "ChannelOption",
    "ChannelParams",
    "RoleOption",
    "RoleParams",
    "MentionableOption",
    "MentionableParams",
    "AttachmentOption",
    "AttachmentParams",
    "UserCommand",
    "user_command",
    "MessageCommand",
    "message_command",
)

# MIT License
#
# Copyright (c) 2023-present hypergonial
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
