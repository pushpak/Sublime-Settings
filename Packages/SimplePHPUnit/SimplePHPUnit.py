import os
import re
import sys
import shlex
import subprocess
import sublime
import sublime_plugin

if sys.version_info < (3, 3):
    raise RuntimeError('SimplePHPUnit works with Sublime Text 3 only')

SPU_THEME = 'Packages/SimplePHPUnit/SimplePHPUnit.hidden-tmTheme'
SPU_SYNTAX = 'Packages/SimplePHPUnit/SimplePHPUnit.hidden-tmLanguage'


class NoOpenProjectException(Exception):
    pass

class InvalidFileTypeException(Exception):
    pass


class ShowInPanel:
    def __init__(self, window):
        self.window = window

    def display_results(self):
        self.panel = self.window.get_output_panel("exec")
        self.window.run_command("show_panel", {"panel": "output.exec"})

        self.panel.settings().set("color_scheme", SPU_THEME)
        self.panel.set_syntax_file(SPU_SYNTAX)


class SimplePhpUnitCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(SimplePhpUnitCommand, self).__init__(*args, **kwargs)
        settings = sublime.load_settings('SimplePHPUnit.sublime-settings')
        self.phpunit_executable = settings.get('phpunit_executable')
        self.xml_config_file = settings.get('phpunit_xml_config_file')

    def run(self, *args, **kwargs):
        try:
            self.build_and_run_phpunit_command(args, kwargs)
        except (IOError, NoOpenProjectException, InvalidFileTypeException) as e:
            sublime.status_message(str(e))
            

    def build_and_run_phpunit_command(self, args, kwargs):
            self.ensure_open_project()
            self.reset_command_args()
            self.file_to_test = None

            if kwargs.get('custom_args') is True:
                self.window.show_input_panel('PHPUnit Arguments:', '', self.set_custom_arguments_and_run_phpunit, None, None)
                return

            if kwargs.get('test_current_file'):
                current_filename = self.window.active_view().file_name()
                if current_filename.endswith('.php') is False:
                    raise InvalidFileTypeException('PHPUnit can only be run on PHP files')
                self.file_to_test = current_filename
                
            self.run_phpunit()

    def reset_command_args(self):
        self.args = [self.phpunit_executable, '--stderr']
        if self.xml_config_file and os.path.isfile(self.xml_config_file):
            self.args += ['--config', self.xml_config_file]

    def ensure_open_project(self):
        try:
            self.PROJECT_PATH = self.window.folders()[0]
        except IndexError:
            raise NoOpenProjectException("PHPUnit must be run from an open Sublime project")

    def set_custom_arguments_and_run_phpunit(self, command):
        self.args.extend(shlex.split(str(command)))
        self.run_phpunit()

    def run_phpunit(self):
        if self.file_to_test:
            self.args.append(self.file_to_test)

        if os.name != 'posix':
            self.args = subprocess.list2cmdline(self.args)

        try:
            self.run_shell_command(self.args, self.PROJECT_PATH)
        except IOError:
            raise IOError('IOError - PHPUnit command aborted')

    def run_shell_command(self, command, working_dir):
            self.window.run_command("exec", {
                "cmd": command,
                "shell": os.name == 'nt',
                "working_dir": working_dir
            })
            self.display_results()

    def display_results(self):
        display = ShowInPanel(self.window)
        display.display_results()

    def window(self):
        return self.view.window()
