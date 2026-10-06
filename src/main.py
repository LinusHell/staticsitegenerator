from textnode import TextNode, TextType
from htmlnode import HTMLNode
from mark2text import text_to_textnodes
from markdown2htmlnode import markdown_to_html_node
from copydir import copy_dir
from generatepage import generate_pages_recursive
import sys

def main(): #only use from root of the project
    if len(sys.argv) == 1:
        basepath = "/"
    else:
        basepath = sys.argv[1]
     
    copy_dir("static", "docs",)
    generate_pages_recursive("content", "template.html", "docs", basepath)


   
main()