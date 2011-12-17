#!/usr/bin/env python
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__   = 'GPL v3'
__copyright__ = '2011, Fanficdownloader team'
__docformat__ = 'restructuredtext en'

from PyQt4.Qt import QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit 

from calibre.utils.config import JSONConfig

# This is where all preferences for this plugin will be stored
# Remember that this name (i.e. plugins/fanfictiondownloader_plugin) is also
# in a global namespace, so make it as unique as possible.
# You should always prefix your config file name with plugins/,
# so as to ensure you dont accidentally clobber a calibre config file
prefs = JSONConfig('plugins/fanfictiondownloader_plugin')

# Set defaults
prefs.defaults['personal.ini'] = get_resources('example.ini')

class ConfigWidget(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.l = QVBoxLayout()
        self.setLayout(self.l)

        self.label = QLabel('personal.ini:')
        self.l.addWidget(self.label)

        self.ini = QTextEdit(self)
        self.ini.setLineWrapMode(QTextEdit.NoWrap)
        self.ini.setText(prefs['personal.ini'])
        self.l.addWidget(self.ini)
        
    def save_settings(self):
        ini = unicode(self.ini.toPlainText())
        if ini:
            prefs['personal.ini'] = ini
        else:
            # if they've removed everything, clear it so they get the
            # default next time.
            del prefs['personal.ini']
