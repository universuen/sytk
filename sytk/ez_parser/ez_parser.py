from abc import ABC
from html.parser import HTMLParser

from sytk.logger import Logger
from .tag_node import TagNode


class _SupParser(HTMLParser, ABC):
    def __init__(self, node: TagNode, convert_charrefs=True):
        super().__init__(convert_charrefs=convert_charrefs)
        self.node = node
        self._logger = Logger(self.__class__.__name__)

    def handle_starttag(self, tag, attrs):
        # generate child node
        child_node = TagNode(tag, attrs, self.node)
        self._logger.debug(f"created new node: {child_node}")
        # bond the child node with current node
        self.node.children.append(child_node)
        # explore child node
        self.node = child_node
        self._logger.debug(f"entered {self.node}\n")

    def handle_data(self, data):
        self.node.data = ''.join([self.node.data, data])
        self.node.text = ''.join([self.node.text, data])
        node = self.node.copy()
        while node.parent is not None:
            node = node.parent
            node.text = ''.join([node.text, data])
        self._logger.debug(f"added data {repr(data)} to {self.node}\n")

    def handle_endtag(self, tag):
        # return to parent node
        self.node = self.node.parent
        self._logger.debug(f"returned to {self.node}\n")


# An EzParser is actually a TagNode with a 'root' tag
class EzParser(TagNode):

    def __init__(self, html: str):
        super().__init__('root')
        _SupParser(self).feed(html)
