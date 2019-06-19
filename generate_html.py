from jinja2 import Environment, FileSystemLoader
import yaml

class LoadText():
	def __init__(self):
		self.title = None
		self.list = []
	def open_yaml(self, yml_path):
		with open(yml_path, 'r') as yml:
			config = yaml.load(yml, Loader=yaml.SafeLoader)
		self.title = config["title"]
		for key, value in config["body"].items():
			self.list.append({'title': value["title"], 'body': value["text"]})

class Html():
	def __init__(self):
		self.env = None
		self.tpl = None
	def read_template(self, tpl_path):
		self.env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
		self.tpl = self.env.get_template(tpl_path)
	def write_html(self, text, out_html):
		html = self.tpl.render({'title':text.title, 'list': text.list})
		file = open(out_html, 'wb')
		file.write(html.encode('utf-8'))
		file.close()

def main():
	html = Html()
	html.read_template('templates/tpl.html')
	loadtext = LoadText()
	loadtext.open_yaml('yamlfiles/contents.yaml')
	html.write_html(loadtext, "index.html")

if __name__ == "__main__":
	main()
