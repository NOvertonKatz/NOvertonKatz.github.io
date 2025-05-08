---
tags: sphinx
date: "2025-05-08"
category: "Blog"
---
# Setting up a Sphinx based blog

First ever post! What better way to start with then how the heck I actually got this site running.

I wanted to setup a personal site for a number of reasons, and I really don't need anything complicated, just some static pages. I'm not a web-dev, don't really want to pay to host it somewhere or somehow host in on my own computer. Lucky me, [github](https://pages.github.com/) pages will host static site for free! 

So having a place to host it, how do I, a high-performance-computing guy with minimal web-dev knowledge, build a website quickly? To no surprise, python has an answer with [Sphinx](https://www.sphinx-doc.org/en/master/). Lots of organizations, and some projects I have worked with, use it for providing documentation. There is even the [ABlog](https://ablog.readthedocs.io/en/stable/) package for making blogs with Sphinx!

I'm not much a fan of the default theme, so use [pydata](https://pydata.org/) instead. Also, while RST is great, I do a lot more work in Markdown, and find it much more readable in a code editor. Sphinx supports using this instead with the [MyST](https://myst-parser.readthedocs.io/en/latest/index.html) package.
