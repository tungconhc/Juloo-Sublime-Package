import sublime, sublime_plugin, webbrowser

class JulooFontSizeHelper(sublime_plugin.EventListener):

	def on_load(self, view):
		def changeCallback():
			size = view.settings().get("font_size")
			sublime.status_message("[ Font Size: "+ str(size) +" ]")
		view.settings().add_on_change("font_size", changeCallback)

	def on_close(self, view):
		view.settings().clear_on_change("font_size")


class JulooOpenBrowserCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		f = self.view.file_name()
		if f != None:
			webbrowser.open(f)
