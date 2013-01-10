import re

def parseSyncOutput2XML (theInput):
	allTheContent = re.sub(r'c: \[\{', '', theInput) # removing leading "c: [{"
	allTheContent = re.sub(r'\}\]$', '', allTheContent) # removing trailing }]
	allTheContent = re.split(r'\}, \{', allTheContent) # splitting user data tuples by "}, {"
	n = 0
	theOutput = ""
	while True: 		
		# SHOWTIMEEEE - Here comes the REGEX MAGICCCCCCCC
		tempContactDataTuple = re.sub(r'u\'(.+?)\'', r"'\g<1>'", allTheContent[n] ) # u'blablabla' becomes 'blablabla'
		tempContactDataTuple = re.sub(r'u"(.+?)"', r"'\g<1>'", tempContactDataTuple ) # special scaped cases (status that have a single quote become sorrounded by double quotes)
		tempContactDataTuple = re.sub(r"'p': '(.+?)', ", r'<p>\g<1></p>\n', tempContactDataTuple ) # parse phone #
		tempContactDataTuple = re.sub(r"'s': '(.+?)', ", r'<s>\g<1></s>\n', tempContactDataTuple ) # parse status quote
		tempContactDataTuple = re.sub(r"'t': (.+?), ", r'<t>\g<1></t>\n', tempContactDataTuple ) # parse time account signed in (I think)
		tempContactDataTuple = re.sub(r"'w': (.+?), ", r'<w>\g<1></w>\n', tempContactDataTuple ) # parse whatsapp account existence 0/1
		tempContactDataTuple = re.sub(r"'n': '(.+)'", r'<n>\g<1></n>\n', tempContactDataTuple ) # parse number in full format (w/countrycode)
		theOutput = theOutput + "<contact>\n" + tempContactDataTuple + "</contact>"
		if (n == len(allTheContent)-1):
			break
		else:
			theOutput = theOutput + "\n"
			n += 1
			
	return theOutput
