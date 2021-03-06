# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Misc.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaguillo <jaguillo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2015/02/24 01:04:00 by jaguillo          #+#    #+#              #
#    Updated: 2015/05/29 00:18:13 by juloo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sublime, sublime_plugin, webbrowser

#
# Util command
# Write to the file
#
# {"erase": {"begin": a, "end": b}} // erase region
# {"region": {"begin": a, "end": b}, "data": "text"} // erase region and insert text
# {"point": a, "data": "text"} // insert text
# {"data": "text"} // insert text at cursors positions
#
class JulooWriteCommand(sublime_plugin.TextCommand):

	def run(self, edit, **args):
		if "erase" in args:
			r = sublime.Region(int(args["erase"]["begin"]), int(args["erase"]["end"]))
			self.view.erase(edit, r)
		if not "data" in args or args["data"] == None:
			return
		if "region" in args:
			self.view.replace(edit, sublime.Region(int(args["region"]["begin"]), int(args["region"]["end"])), args["data"])
		elif "point" in args:
			self.view.insert(edit, int(args["point"]), args["data"])
		else:
			for s in self.view.sel():
				self.view.replace(edit, s, args["data"])

#
# Show the current scope in the status bar
#
class JulooScopeHelper(sublime_plugin.EventListener):

	def on_selection_modified(self, view):
		if view.settings().get("juloo_show_scope", False) and len(view.sel()) == 1 and view.sel()[0].size() == 0:
			view.set_status("scope_juloo", "[ "+ view.scope_name(view.sel()[0].a) +"]")
		else:
			view.erase_status("scope_juloo");

#
# Show the font size for 3 secs when you change it using CTRL+mouse
#
class JulooFontSizeHelper(sublime_plugin.EventListener):

	def on_load(self, view):
		def changeCallback():
			size = view.settings().get("font_size")
			sublime.status_message("[ Font Size: "+ str(size) +" ]")
		view.settings().add_on_change("font_size", changeCallback)

	def on_close(self, view):
		view.settings().clear_on_change("font_size")

#
# Open borwser command
#
class JulooOpenBrowser(sublime_plugin.TextCommand):

	def run(self, edit):
		f = self.view.file_name()
		if f != None:
			webbrowser.open(f)
