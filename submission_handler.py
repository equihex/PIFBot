#!/usr/bin/env python
# coding: utf-8
#
#   File = submission_handler.py
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

def handle_submission(submission):
    # Decide what kind of post this is and proceed appropriately.  Maybe check
    # the flair to see if it's "PIF - Open" and then kick it over to a PIF
    # handler?
    if submission.link_flair_text == "PIF - Open":
        handle_pif(submission)

def handle_pif(submission):
    lines = submission.selftext.lower().split("\n")
    for line in lines:
        if line.startswith("pifbot"):
            parts = line.split()
            if parts[1] == "lottery":
                handle_lottery(submission, parts[2:])
            elif parts[1] == "range":
                handle_range(submission, parts[2:])
            elif parts[1] == "poker":
                handle_poker(submission, parts[2:])

def handle_lottery(submission, args):
    print("Lottery PIF")
    print(args)

def handle_range(submission, args):
    print("Range PIF -- UNSUPPORTED")
    print(args)

def handle_poker(submission, args):
    print("Poker PIF -- UNSUPPORTED") 
    print(args)                
