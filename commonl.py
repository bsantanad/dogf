#!/usr/bin/env python3
'''
common library
'''

import os
import markdown

def get_posts_names(path):
    '''
    return list of md files (the paths in str) in certain directory
    '''
    posts = []
    if not os.path.exists(path):
       raise IOError('posts path not found')
    for filename in os.listdir(path):
        if filename.endswith(".md"):
            post = os.path.join(path, filename)
            posts.append(post)
    return posts

def md_to_html(path):
    '''
    open md, read header and tranform the rest into html,
    build an object with title, date, topic and html and return it
    (by object I mean a dict)
    '''
    obj = {}
    try:
        with open(path, 'r') as file:
            md_text = file.read().splitlines()
            if md_text[0] == '---':
                md_text = md_text[1:]
            lines_to_remove = 0
            for i, line in enumerate(md_text):
                line = line.lstrip().rstrip().lower()
                if line == '---':
                    lines_to_remove = i + 1
                    break
                if line.startswith('title'):
                    _, title = line.split(':', 1)
                    obj['title'] = title.lstrip()
                    continue
                if line.startswith('date'):
                    _, date = line.split(':', 1)
                    obj['date'] = date.lstrip()
                    continue
                if line.startswith('topic'):
                    _, date = line.split(':', 1)
                    obj['topic'] = date.lstrip()
                    continue
            md_text = md_text[lines_to_remove:]
            md_text = '\n'.join(md_text)
            # FIXME maybe add a try and catch here
            html = markdown.markdown(md_text, extensions=['fenced_code'])
    except IOError as e:
        logging.error(f'unable to open {post}')
        raise e
    obj['html'] = html
    return obj
