#!/usr/bin/env python
# coding: utf-8
#
#   File = pifbot.py
#
#      Copyright 2019 [name of copyright owner]
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
############################################################################

import config
from comment_handler import handle_comment
from submission_handler import handle_submission
from private_message_handler import handle_private_message

import praw
import threading

# Create the connection to Reddit.
# This assumes a properly formatted praw.ini file exists:
#   https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html
reddit = praw.Reddit(config.bot_name, user_agent=config.user_agent)

# Get a handle on our preferred subreddit
subreddit = reddit.subreddit(config.subreddit)

# Prove we're connected
print(reddit.user.me())


def monitor_submissions():
    for submission in subreddit.stream.submissions():
        handle_submission(submission)


def monitor_comments():
    for comment in subreddit.stream.comments():
        handle_comment(comment)


def monitor_private_messages():
    for inbox_item in reddit.inbox.stream():
        if inbox_item.id.startswith("t4"):
            handle_private_message(inbox_item)
        # TODO in case of a mention, maybe refer to a documentation of this bot's functionality

threading.Thread(target=monitor_submissions).start()
threading.Thread(target=monitor_comments).start()
threading.Thread(target=monitor_private_messages).start()
