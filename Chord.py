def Note2Num(Note):
	if Note == 'A':
		return 0
	if Note == 'A#' or Note == 'Bb':
		return .5
	if Note == 'B' or Note == 'Cb':
		return 1
	if Note == 'C' or Note == 'B#':
		return 1.5
	if Note == 'C#' or Note == 'Db':
		return 2
	if Note == 'D':
		return 2.5
	if Note == 'D#' or Note == 'Eb':
		return 3
	if Note == 'E' or Note == 'Fb':
		return 3.5
	if Note == 'F' or Note == 'E#':
		return 4
	if Note == 'F#' or Note == 'Gb':
		return 4.5
	if Note == 'G':
		return 5
	if Note == 'G#' or Note == 'Ab':
		return 5.5
	return 0

def Num2Note(Num,flat=False):
	if Num > 5.5:
		Num = Num % 6
	if Num == 0:
		return 'A'
	if Num == .5:
		if flat == True:
			return 'Bb'
		else:
			return 'A#'
	if Num == 1:
		return 'B'
	if Num == 1.5:
		return 'C'
	if Num == 2:
 		if flat == True:
			return 'Db'
		else:
			return 'C#'
	if Num == 2.5:
		return 'D'
	if Num == 3:
		if flat == True:
			return 'Eb'
		else:
			return 'D#'
	if Num == 3.5:
		return 'E'
	if Num == 4:
		return 'F'
	if Num == 4.5:
		if flat == True:
			return 'Gb'
		else:
			return 'F#'
	if Num == 5:
		return 'G'
	if Num == 5.5:
		if flat == True:
			return 'Ab'
		else:
			return 'G#'
	return Num

def Scale(root,scaleType,flat=False):
	if scaleType == 'minor':
		return [Num2Note(root,flat),Num2Note(root + 1,flat),Num2Note(root + 1.5,flat),Num2Note(root + 2.5,flat),Num2Note(root + 3.5,flat),Num2Note(root + 4,flat),Num2Note(root + 5,flat),Num2Note(root + 6,flat)]
	if scaleType == 'major':
		return [Num2Note(root,flat),Num2Note(root + 1,flat),Num2Note(root + 2,flat),Num2Note(root + 2.5,flat),Num2Note(root + 3.5,flat),Num2Note(root + 4.5,flat),Num2Note(root + 5.5,flat),Num2Note(root + 6,flat)]
def Chord(root,chordType,flat=False):
	if chordType == 'maj':
		return [Num2Note(root,flat),Num2Note(root + 2,flat),Num2Note(root + 3.5,flat)]
	if chordType == 'min':
		return [Num2Note(root,flat),Num2Note(root + 1.5,flat),Num2Note(root + 3.5,flat)]
def Quiz(flat=False):
	#initilise the variables and import random
	import random
	Ansr = ''

	#determin the chord type
	ChordType = 'min'
      	if random.randrange(1,3) == 1:
      		ChordType = 'maj'

	#determin the root chord
     	Temproot = random.randrange(0,11)/2.0

	#print out the chord for the user to see
     	print(Chord(Temproot,ChordType,flat))

	#quiz the user
     	while Ansr != 'give up':
    		Ansr = raw_input('What is the chords name? ->')
    		if Ansr == Num2Note(Temproot,True) + ChordType or Ansr == Num2Note(Temproot,False) + ChordType:
            		print('Correct!')
              		return 1
		else:
			if Ansr != 'give up':
				print('Try again!')

		if Ansr == 'hint':
			print('No, I dont want to program this get your own hint, you lazy user')
	print('the chord name was: ' + Num2Note(Temproot,flat) + ChordType)
   	print('better luck next time')
	return 0

def Main():
	root = 0
	flat = False
	Ansr = ''
	while Ansr != 'q':
		Ansr = raw_input('->')
		if Ansr.lower() == 'help' or Ansr == '?':

		#this is the start of the help command
			print('List of commands:')
			print('----------------------------------')
			print('root')
			print('major')
			print('minor')
			print('enharm')
			while Ansr != 'enharm' and Ansr != 'major' and Ansr != 'minor' and Ansr != 'root' and Ansr != 'd':
				Ansr = raw_input('Please list what command you would like help with, d for done- >')
			if Ansr == 'root':
				print('syntax:root <NOTE>')
				print('---------------------------')
 				print('the root command changes the global root note that is used by each of the scale commands')
				print('to <NOTE>, notes should be capitalised, with a lowercase b representing flat')
				print('If the specified not is not recognise the program will default to \'A\'')
			if Ansr == 'minor':
				print('syntax:minor')
				print('---------------------------')
				print('the minor command prints off a minor scale of the current global root note')
				print('see the root command to change that global')
			if Ansr == 'major':
				print('syntax:major')
				print('---------------------------')
                                print('the major command prints off a major scale of the current global root note')
                                print('see the root command to change that global')
			if Ansr == 'enharm':
				print('syntax:enharm <#>//<b>')
				print('---------------------------')
				print('The enharm command changes the global preference for flat or sharp enharmonics to your specified argument')
				print('If no argument is specified the command will invert the global preference')
		#this is the end of the help command
		#comments 4 clenlyness (not spelling :p)

		if Ansr.lower() == 'minor':
			print(Scale(root,'minor',flat))
		if Ansr.lower() == 'major':
			print(Scale(root,'major',flat))
		if Ansr.lower() == 'quiz':
			Quiz(flat)
		if len(Ansr.split(' ')) > 1 and Ansr.split(' ')[0] == 'root':
			root = Note2Num(Ansr.split(' ')[1])
			print('Setting root to ' + Num2Note(root))
		if Ansr.split(' ')[0] == 'enharm':
			if len(Ansr.split(' ')) > 1 and Ansr.split(' ')[1] == '#':
				flat = False
			else:
				if len(Ansr.split(' ')) > 1 and Ansr.split(' ')[1] == 'b':
					flat = True
				else:
					if flat == True:
						flat = False
					else:
						flat = True
			if flat == True:
				print('setting global enharm to flat')
			else:
				print('setting global enharm to sharp')

Main()
