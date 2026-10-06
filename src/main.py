from textnode import TextNode, TextType
from htmlnode import HTMLNode
from mark2text import text_to_textnodes
from markdown2htmlnode import markdown_to_html_node
from copydir import copy_dir
from generatepage import generate_pages_recursive
def main(): #only use from root of the project
    copy_dir("static", "public",)
    generate_pages_recursive("content", "template.html", "public")


   
main()