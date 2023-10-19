from Stack import Stack
import re
import typing

def TagMatch(string):
	tag_stack = Stack()

	tag_re = re.compile(r"<(/?\w+)>")
	
	all_tags = tag_re.findall(string)

	for tag in all_tags:
		if tag[0] != "/":
			tag_stack.push(tag)

		else:
			if (tag[1::] == tag_stack.top()):
				tag_stack.pop()
			else:
				return False

	return tag_stack.isEmpty()

if __name__ == "__main__":
	text = """<body>
<center>
<h1> The Little Boat </h1>
</center>
<p> The storm tossed the little
boat like a cheap sneaker in an
old washing machine. The three
drunken fishermen were used to
such treatment, of course, but
not the tree salesman, who even as
a stowaway now felt that he
had overpaid for the voyage. </p>
<ol>
<li> Will the salesman die? </li>
<li> What color is the boat? </li>
<li> And what about Naomi? </li>
</ol>
</body>"""
	print(TagMatch(text))