import ConfigParser
Config = ConfigParser.ConfigParser()
def allsections():
	Config.read("poc/hello.ini")
	sections = Config.sections()
	return sections


def options(section):
	options= Config.options(section)
	return options

def alloptions():
	dictionary = {}
	sections = allsections()
	for section in sections:
		opt = options(section)
		for option in opt:
			dictionary[(option.upper()[0] + option[1:])] = Config.get(section,option)
	return dictionary

def readOptionValue(option):
	dictionary = alloptions()
	value = dictionary[option]
	return value


def call():
	value=readOptionValue('Date')
	print value


if __name__ == '__main__':
	call()
