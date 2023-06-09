﻿# A plugin to convert [Outline](https://synfig.readthedocs.io/en/latest/layers/outline.html#outline-layer) to [Advanced Outline](https://synfig.readthedocs.io/en/latest/layers/advanced_outline.html)

This plugin converts outline within a Synfig File to Advanced Outline while mainting variours properties of Outline layer. Synfig has a built in functionality through which you can convert the outline to advanced outline (right click on Outline layer), but it reset's the properties to default values. This plugin maintains all the properties of Outline such as color, width, etc from Outline to Advaned Outline.

## Features:
- Preservs various properties of Outline
- Convert multiple Outline to Advanced Outlines at once
- Useful if you prefer Advanced Outline over Outline

## Installation:

Download the zip file, extract it's content to the plugins folders ([more](https://synfig.readthedocs.io/en/latest/plugins.html#how-to-install-plugins))

## How to use:

To use the plugin, follow the steps below

1. Open your Synfig file
2. Rename your layer/group with a prefix
   1. toAdvOutline / @: If you want all children at any level to be converted to advanced outline
   2. toAdvOutline* / @* (note the asterik symbol) : If you want only the direct children to be converted to advanced outline.
3. Run the plugin
4. As per specified it will convert those outline layers to advanced outline

# FAQ

### Do I really need this plugin ?

It's just a plugin for convenience, based on your personal need you can use this plugin for simplicity. 

### I have a problem/question/issue what should I do ?

Please open a new issue. If you also have any suggestions, improvements, reviews, ideas, discussions, please open a new issue so that I can discuss the problems.

### Can I use this for commercial purpose ?

This plugin and the code is in Public Domain meaning you can do anything you want, without any permission from the creators.

### I am unable to see the Plugin in Plugins Option, what should I do ?

Please check whether you have installed the plugin properly more information is available on the [Synfig Docs](https://synfig.readthedocs.io/en/latest/plugins.html#how-to-install-plugins).
Common mistakes include having an extra directory on top of the actual Plugin directory or not putting the folder in the right location.
If you are sure you have done everything correctly and yet not able to see the plugin, please open a new issue.

### Does this plugin offer other functionality rather than just doing that ?

No, this plugin's only purpose is to convert Outline to Advanced Outline.

