#!/usr/bin/python -tt
#
# main.py
# Copyright (C) Viswanath S 2010 <viswanathgs@gmail.com>
# 
# HelloWorld is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# HelloWorld is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import gtk

class HelloWorldEditor:
	
	def on_mainwindow_destroy(self, widget, data=None):
		gtk.main_quit()
	
	def __init__(self):
		builder = gtk.Builder()
		builder.add_from_file("homedialog.xml")
		
		self.window = builder.get_object("mainwindow")
		builder.connect_signals(self)


if __name__ == '__main__':
	editor = HelloWorldEditor()
	editor.window.show()
	gtk.main()
	
