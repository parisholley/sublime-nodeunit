import sublime, sublime_plugin

class NodeUnitCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		win = self.view.window();

		print win.folders()
		print 'wee'

		root = win.folders()[0]
		relative = self.view.file_name().replace(root,"")[1:]

		sels = self.view.sel()

		test = None

		for sel in sels:
			test = self.view.substr(sel)

		if test == None:
			win.run_command("exec", {
				"cmd": ["nodeunit", relative],
				"working_dir": root
			})
		else:
			win.run_command("exec", {
				"cmd": ["nodeunit", "-t", test, relative],
				"working_dir": root
			})
