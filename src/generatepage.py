from markdown2htmlnode import markdown_to_html_node
from htmlnode import HTMLNode
from extracttitle import extract_title
import os


def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str) -> None:
    files_and_subdir = os.listdir(dir_path_content)
    for object in files_and_subdir:
        object_path = os.path.join(dir_path_content,object)
        if os.path.isfile(object_path):
            if not object.endswith(".md"):
                raise Exception(f"File {object} is not a Markdown file.")
            dest_html = os.path.join(dest_dir_path,object)[:-2] + "html"
            generate_page(object_path, template_path, dest_html)
        elif os.path.isdir(object_path):
            os.makedirs(os.path.join(dest_dir_path,object))
            generate_pages_recursive(object_path, template_path, os.path.join(dest_dir_path,object))
        else:
            raise Exception(f"Object in directory {dir_path_content} is neither a file nor a directory.")
    
    




def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_object = open(from_path, "r")
    markdown = from_object.read()
    from_object.close()
    template_object = open(template_path, "r")
    template = template_object.read()
    template_object.close()
    markdown_as_html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    full_html = template.replace("{{ Content }}",markdown_as_html, 1)
    full_html = full_html.replace("{{ Title }}",title,1)
    os.makedirs(os.path.dirname(dest_path),exist_ok = True)
    dest_object = open(dest_path, "w")
    dest_object.write(full_html)
    dest_object.close()
