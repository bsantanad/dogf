# common library

import markdown

with open('./tmp.md', 'r') as f:
    text = f.read()
    html = markdown.markdown(text, extensions=['fenced_code'])

'''
<style>
code {
  font-family: Consolas,"courier new";
  color: crimson;
  background-color: #f1f1f1;
  padding: 2px;
  font-size: 105%;
  display: block;
  white-space: pre-wrap
}
body{
	margin:0;
	background-color: #efefef;
}
header {
	font-size: 20px;
	background-color: black;
	color: #cccccc;
	height: 75px;
}

p {
	margin-top:20px;
	float:left;
}
</style>
'''
