"""
Autor: Rene Hollander 5BHIT
"""

from ui.ContentTableModel import ContentTableModel


class MainModel():
    def __init__(self, parent):
        self.fileName = None
        self.contentTableModel = ContentTableModel(parent, [])
