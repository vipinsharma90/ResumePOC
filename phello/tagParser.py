import ConfigParser
Config = ConfigParser.ConfigParser()
def allsections(fullFileName):
	Config.read(fullFileName+'.ini')
	sections = Config.sections()
	return sections


def options(section):
	options= Config.options(section)
	return options

def alloptions(fullFileName):
	dictionary = {}
	sections = allsections(fullFileName)
	for section in sections:
		opt = options(section)
		for option in opt:
			dictionary[(option.upper()[0] + option[1:])] = Config.get(section,option)
	return dictionary

def readOptionValue(fullFileName,option):
	dictionary = alloptions(fullFileName)
	value = dictionary[option]
	return value


def call():
	value=readOptionValue('Date')
	print value


if __name__ == '__main__':
	call()
