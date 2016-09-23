SimplePHPUnit
===============

This plugin allows you the run PHPUnit tests straight from the Sublime Text interface.

### Available commands
**`Run`**
This is the equivalent of running: `phpunit` _`<sublime project root directory>`_

**`Test current file`**
This is the equivalent of running: `phpunit` _`<path to current file>`_

**`Run with custom args`**
Opens a new input window which allows user to enter PHPUnit arguments to be added to the command.  This is the equivalent of running: `phpunit` _`<user-entered arguments>`_

***Please see the settings file after installation to see options that could affect the behavior of these commands***

### Colored output:
![Coloring output](https://raw.github.com/m0nah/SimplePHPUnit-for-Sublime-Text/master/Screen%20Shot.png)

### Installation:
1. Use [Package Control](https://packagecontrol.io/installation) to install `SimplePHPUnit`
2. Download and unzip the plugin files to `<Your ST2-ST3 Packages Directory>\SimplePHPUnit\`

### Usage:
1. Press Cmd + Shift + P to open the control palette
2. Search for `PHPUnit: ` and pick your command

Also you can use the `Tools --> PHPUnit...` menu item, or set up custom keybindings

### Keybinding:
You can use command `simple_php_unit` for your keybinding.

**Examples**:
```json
{
	"keys": ["ctrl+alt+t"],
	"command": "simple_php_unit"
},
{
	"keys": ["super+ctrl+alt+t"],
	"command": "simple_php_unit",
	"args": {
        "test_current_file": true
    }
}
```

### Notes:
- Latest version of the plugin built and tested using [PHPUnit 4.4](https://phpunit.de/).
- If your projects use XML configuration files for PHPUnit, be sure to specify them in your user settings.
- Enable automatic output panel display by adding `"show_panel_on_build": true` to your user settings or use the `Tools --> Build Results --> Show Build Results` menu item to view results.

### Donate:
If you liked this plugin, you can donate to support it!

[![Paypal donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=SZ6YWJUGFM9J8)

Give some feedback.

Thanks.
