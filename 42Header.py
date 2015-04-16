# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    42Header.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaguillo <jaguillo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2015/02/24 01:03:39 by jaguillo          #+#    #+#              #
#    Updated: 2015/04/16 19:49:16 by jaguillo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# import sublime, sublime_plugin, re

# header_config = ([
# 	"        :::      ::::::::",
# 	"      :+:      :+:    :+:",
# 	"    +:+ +:+         +:+  ",
# 	"  +#+  +:+       +#+     ",
# 	"+#+#+#+#+#+   +#+        ",
# 	"     #+#    #+#          ",
# 	"    ###   ########.fr    "], # logo
# 	2, # top offset
# 	2, # bottom offset
# 	4, # max offset
# 	[ # values (offset, regex, initial, format)
# 		(3, '^[^ ]+ +([^ ]+)',								"%(file)s",				"%(file)s")
# 		(5, '^[^ ]+ +By: ([^ ]+) <([^>]+)>',				"%(user)s <%(mail)s>",	"%(1)s <%(2)s>")
# 		(7, '^[^ ]+ +Created: ([^ ]+ [^ ]+) by ([^ ]+)',	"%(date)s by %(user)s",	"%(1)s by %(2)s")
# 		(8, '^[^ ]+ +Updated: ([^ ]+ [^ ]+) by ([^ ]+)',	"%(date)s by %(user)s",	"%(date)s by %(user)s")
# 	]
# ]

# headers = [ # headers for language or file extension
# 	(["C++", "Java", "JavaScript", "ActionScript", "CSS", "JSON"], [], 0, """/* ************************************************************************** */
# /*                                                                            */
# /*                                                        :::      ::::::::   */
# /*   %-50s :+:      :+:    :+:   */
# /*                                                    +:+ +:+         +:+     */
# /*   By: %-42s +#+  +:+       +#+        */
# /*                                                +#+#+#+#+#+   +#+           */
# /*   Created: %-40s #+#    #+#             */
# /*   Updated: %-39s ###   ########.fr       */
# /*                                                                            */
# /* ************************************************************************** */
# """),
# 	(["HTML", "XML"], [], 0, """<!-- *********************************************************************** -->
# <!--                                                                         -->
# <!--                                                      :::      ::::::::  -->
# <!-- %-50s :+:      :+:    :+:  -->
# <!--                                                  +:+ +:+         +:+    -->
# <!-- By: %-42s +#+  +:+       +#+       -->
# <!--                                              +#+#+#+#+#+   +#+          -->
# <!-- Created: %-40s #+#    #+#            -->
# <!-- Updated: %-39s ###   ########.fr      -->
# <!--                                                                         -->
# <!-- *********************************************************************** -->
# """),
# 	([], ["s", "asm", "i", "inc"], 0, """;; ************************************************************************** ;;
# ;;                                                                            ;;
# ;;                                                        :::      ::::::::   ;;
# ;;   %-50s :+:      :+:    :+:   ;;
# ;;                                                    +:+ +:+         +:+     ;;
# ;;   By: %-42s +#+  +:+       +#+        ;;
# ;;                                                +#+#+#+#+#+   +#+           ;;
# ;;   Created: %-40s #+#    #+#             ;;
# ;;   Updated: %-39s ###   ########.fr       ;;
# ;;                                                                            ;;
# ;; ************************************************************************** ;;
# """),
# 	(["Shell"], [], 1, """#!/bin/bash
# # **************************************************************************** #
# #                                                                              #
# #                                                         :::      ::::::::    #
# #    %-50s :+:      :+:    :+:    #
# #                                                     +:+ +:+         +:+      #
# #    By: %-42s +#+  +:+       +#+         #
# #                                                 +#+#+#+#+#+   +#+            #
# #    Created: %-40s #+#    #+#              #
# #    Updated: %-39s ###   ########.fr        #
# #                                                                              #
# # **************************************************************************** #
# """),
# 	(["Language"], [], 0, """# **************************************************************************** #
# #                                                                              #
# #                                                         :::      ::::::::    #
# #    %-50s :+:      :+:    :+:    #
# #                                                     +:+ +:+         +:+      #
# #    By: %-42s +#+  +:+       +#+         #
# #                                                 +#+#+#+#+#+   +#+            #
# #    Created: %-40s #+#    #+#              #
# #    Updated: %-39s ###   ########.fr        #
# #                                                                              #
# # **************************************************************************** #
# """)
# ]

# class Header():

# 	view = None
# 	pattern = None
# 	offset = 0
# 	values = {}

# 	def __init__(self, view):
# 		self.view = view

# 	def update(self):
# 		pass

# 	def overwrite(self):
# 		pass

# 	def search(self):
# 		i = 0
# 		while i < header_config[3]:
# 			j = 0
# 			while j < len(header_config[0]):
# 				linept = view.text_point(0, i + j)
# 				line = view.substr(line(linept))
# 				if not header_config[0][j] in line:
# 					return False
# 				j += 1
# 			i += 1
# 		self.offset = i
# 		return True

# 	def load_values(self):
# 		self.values['file'] = view.file_name().split('/')[-1]
# 		self.values['user'] = self.view.settings().get("header_pseudo", "Unknown")
# 		self.values['mail'] = self.values['user'] + "@student.42.fr"
# 		self.values['date'] = strftime("%Y/%m/%d %H:%M:%S", localtime())

# 	def load_pattern(self):
# 		syntax = self.view.settings().get("syntax")
# 		for pattern in headers:
# 			for l in pattern[0]:
# 				if l in syntax:
# 					self.pattern = pattern
# 					return True
# 			ext = self.view.file_name().lower().split('.')
# 			for l in pattern[1]:
# 				if l == ext[-1]:
# 					self.pattern = pattern
# 					return True
# 		return False


# def update_header(view):
# 	header = Header(view)
# 	if not header.load_pattern():
# 		print("Header not available for this language")
# 	elif not header.search():
# 		print("Header not found")
# 	else:
# 		header.load_values()
# 		header.update()
# 		header.overwrite()


# class Juloo42Header(sublime_plugin.EventListener):

# 	def on_pre_save(self, view):
# 		if view.settings().get("juloo_42_header", True):
# 			update_header(view)

import sublime, sublime_plugin, re
from time import localtime, strftime

#
# Insert and update the 42 header
#
headers = [
	(["C++", "Java", "JavaScript", "ActionScript", "CSS", "JSON"], [], 0, """/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   %-50s :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: %-42s +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: %-40s #+#    #+#             */
/*   Updated: %-39s ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
"""),
	(["HTML", "XML"], [], 0, """<!-- *********************************************************************** -->
<!--                                                                         -->
<!--                                                      :::      ::::::::  -->
<!-- %-50s :+:      :+:    :+:  -->
<!--                                                  +:+ +:+         +:+    -->
<!-- By: %-42s +#+  +:+       +#+       -->
<!--                                              +#+#+#+#+#+   +#+          -->
<!-- Created: %-40s #+#    #+#            -->
<!-- Updated: %-39s ###   ########.fr      -->
<!--                                                                         -->
<!-- *********************************************************************** -->
"""),
	([], ["s", "asm", "i", "inc"], 0, """;; ************************************************************************** ;;
;;                                                                            ;;
;;                                                        :::      ::::::::   ;;
;;   %-50s :+:      :+:    :+:   ;;
;;                                                    +:+ +:+         +:+     ;;
;;   By: %-42s +#+  +:+       +#+        ;;
;;                                                +#+#+#+#+#+   +#+           ;;
;;   Created: %-40s #+#    #+#             ;;
;;   Updated: %-39s ###   ########.fr       ;;
;;                                                                            ;;
;; ************************************************************************** ;;
"""),
	(["Shell"], [], 1, """#!/bin/bash
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    %-50s :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: %-42s +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: %-40s #+#    #+#              #
#    Updated: %-39s ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
"""),
	(["Language"], [], 0, """# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    %-50s :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: %-42s +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: %-40s #+#    #+#              #
#    Updated: %-39s ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
""")
]

reg_file = re.compile('^[^ ]+ +([^ ]+)')
reg_by = re.compile('^[^ ]+ +By: ([^ ]+) <([^>]+)>')
reg_created = re.compile('^[^ ]+ +Created: ([^ ]+ [^ ]+) by ([^ ]+)')
reg_updated = re.compile('^[^ ]+ +Updated: ([^ ]+ [^ ]+) by ([^ ]+)')

class Header42():

	pattern = None

	lines = []
	name = ""
	by = ("", "")
	creator = ("", "")
	updater = ("", "")
	valid = False

	def __init__(self, pattern):
		self.pattern = pattern

	def set(self, user):
		self.by = (user, user + "@student.42.fr")
		self.creator = (get_42_time(), user)
		self.updater = (get_42_time(), user)

	def parse(self, lines):
		self.lines = lines
		name = re.search(reg_file, lines[3])
		if name != None:
			self.name = name.group(1)
		by = re.search(reg_by, lines[5])
		if by != None:
			self.by = (by.group(1), by.group(2))
		creator = re.search(reg_created, lines[7])
		if creator != None:
			self.creator = (creator.group(1), creator.group(2))
		updater = re.search(reg_updated, lines[8])
		if updater != None:
			self.updater = (updater.group(1), updater.group(2))
		if name == None or by == None or creator == None or updater == None:
			self.valid = False
		else:
			self.valid = True

	def get(self):
		by = "%s <%s>" % self.by
		creator = "%s by %s" % self.creator
		updater = "%s by %s" % self.updater
		return self.pattern[3] % (self.name, by, creator, updater)

	def update(self, view):
		self.name = view.file_name().split('/')[-1]
		self.updater = (get_42_time(), view.settings().get("header_pseudo", self.updater[1]))

class Juloo42Header(sublime_plugin.EventListener):

	def on_pre_save(self, view):
		if view.settings().get("juloo_42_header", True):
			update_header(view)

class JulooHeaderCommand(sublime_plugin.TextCommand):

	def run(self, edit, **args):
		if args["action"] == "update":
			update_header(self.view)
		else:
			header = Header42(get_header_pattern(self.view))
			user = self.view.settings().get("header_pseudo", "Unknown")
			if user == "Unknown":
				print("Please configure your name")
			header.set(user)
			header.update(self.view)
			self.view.run_command("juloo_write", {"point": 0, "data": header.get()})

def get_42_time():
	return strftime("%Y/%m/%d %H:%M:%S", localtime())

def get_header_pattern(view):
	for pattern in headers:
		syntax = view.settings().get("syntax")
		for l in pattern[0]:
			if l in syntax:
				return pattern
		ext = view.file_name().lower().split('.')
		for l in pattern[1]:
			if l == ext[-1]:
				return pattern
	return None

def update_header(view):
	pattern = get_header_pattern(view)
	if pattern == None:
		return
	region = sublime.Region(0, view.text_point(11 + pattern[2], 0))
	substr = view.substr(region)
	if substr.startswith(pattern[3][:247]) and substr.endswith(pattern[3][590:]):
		header = Header42(pattern)
		header.parse(substr.split('\n')[pattern[2]:])
		if header.valid:
			header.update(view)
			view.run_command("juloo_write", {"action": "replace", "region": (region.a, region.b), "data": header.get()})
			print("Header updated")
		else:
			print("Error: Bad header.")
	else:
		print("No header detected.")
