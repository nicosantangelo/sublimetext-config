import sublime, sublime_plugin

# Close all tabs except the active one.
class CloseOthersCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = self.view.window()
        group_index, view_index = window.get_view_index(self.view)
        window.run_command("close_others_by_index", { "group": group_index, "index": view_index})        


# Close tabs to the right of the active tab.
class CloseToRightCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = self.view.window()
        group_index, view_index = window.get_view_index(self.view)
        window.run_command("close_to_right_by_index", { "group": group_index, "index": view_index})


# Show the current path on a panel, if selected, copy it.
class GetCurrentPathCommand(sublime_plugin.TextCommand):
    STRIP = '/Users/nicosantangelo'

    def run(self, edit):
        full_path = self.view.file_name()
        if full_path:
            self.path = self.view.file_name().replace(self.STRIP, '')
            sublime.set_timeout(lambda: self.view.window().show_quick_panel([self.path], self.copy_path, sublime.MONOSPACE_FONT), 0)

    def copy_path(self, index):
        sublime.set_clipboard(self.path)
