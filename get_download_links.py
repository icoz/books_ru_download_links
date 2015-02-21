#!/usr/bin/env python3

import lxml.html
import sys

def get_links(fname):
	with open(fname,'rt') as f:
		data = f.read()
		doc = lxml.html.document_fromstring(data)
	links = doc.xpath('//a[@class="pdf"]')
	out = []
	for l in links:
		h = l.attrib['href']
		h = h.replace('/member/download_agreement.php?back_url=/','http://www.books.ru/')
		# print(h)
		if h not in out:
			out.append(h)
	out.sort()
	return out

def parse_files(names):
	links = []
	for name in names:
		print('Parsing {}'.format(name), file=sys.stderr)
		links += get_links(name)
	out = list(set(links))
	out.sort()
	print('<html><body>')
	for i in out:
		print('<a href="{0}">{0}</a><br>\n'.format(i))
	print('</body></html>')


def main():
	# parse_file('2184545')
	names = sys.argv[1:]
	# print(names)
	parse_files(names)

if __name__ == '__main__':
	main()
