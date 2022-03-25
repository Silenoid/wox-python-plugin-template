#encoding=utf8
import webbrowser
import re,os
import wox
from wox import Wox,WoxAPI

restrictions = [
    "banana",
    "mango",
    "orange",
    "lemon"
]

""" Minimal and generic python template for Wox

In order to have a working plugin, in case __name__ == "__main__", an instance of a
class that inherits Wox must be instantiated.

In that class, the query(self,query) callback will be invoked each time a character
is added in the command palette when triggering the plugin.

In order to return commands, a JSON formatted array with a Title, IcoPAth and
JsonRPCAction have to be specified (read example below).

Keep in mind: optimization is key. The entire script will be run everytime the 
input text in the command palette changes.
"""

class MyPluginClass(Wox):

    def query(self,query):
        suggestions = [restr for restr in restrictions if query in restr]
        res = []
        
        for sugg in suggestions:
            res.append({
                "Title": "{}".format(sugg),
                "IcoPath":"icon.png",
                "JsonRPCAction":{"method": "do_stuff", "parameters": [sugg]}
                })
        return res

    def do_stuff(self,input_query):
        args = [x.strip() for x in input_query.split(' ')]
        if len(args) == 2:
            webbrowser.open_new_tab("https://url.com/buytwofruit?fruit1=" + args[0] + "&fruit2=" + args[1])

if __name__ == "__main__":
    MyPluginClass()