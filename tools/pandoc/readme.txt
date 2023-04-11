https://pandoc.org/epub.html #bookmark #pandoc #kindle #epub

Pandoc can convert simple text file written in markup format to epub format that is compatible for kindle.
---------------------------
A toy example
Use your text editor to create a file mybook.txt, with the following contents:
--------
% My Book
% Sam Smith

This is my book!

# Chapter One

Chapter one is over.

# Chapter Two

Chapter two has just begun.
To make this into an ebook takes only one command:

pandoc mybook.txt -o mybook.epub
You can upload mybook.epub to your ebook reader and try it out.

Note that if your markdown file contains links to local images, for example

![Juliet](images/sun.jpg)
pandoc will automatically include the images in the generated epub.
---------------------------

Example command,
$ pandoc -o mybook.epub mybook.txt 



