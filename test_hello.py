from hello import printinfo

def test_printinfo():
	assert printinfo(-1)
	print "...Negative Number..."

def test_printinfo_a():
	assert printinfo(1)
	print "...Positive Number.."



