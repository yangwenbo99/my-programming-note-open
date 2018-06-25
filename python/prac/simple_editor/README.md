# Usage 

Commands under normal mode:

	p: print 
		p [num]
		num should be a non-negative integer
		print some line from the current line
		if num not given, it will print the current line
	i: insert line(s) before current line
		i
	a: insert line(s) after current line
		a
	A: go the the end and append line(s) at the end of the file
		A
	s: substitute the current line 
	g: go to
		g [line_number]
		line_number should be a non-negative integer, 
		if line_number not given, it will go the first line
	G: go to, from bottom
		G [num]
		num should be a non-negative integer, 
		if num not given, it will go the line after the last line
	h: move to, from current line
		h offset
		offset should be an integer
	u: undo
	m: mark, so that the cusor can go back to current line
		m register_name
	k: go to mark
		' register_name

	e: edit
		e file_name
		edit file_name
	w: write
		w [file_name]
		if file_name not given, it will write to current file.
		after writing, the current file will be updated to file_name
	q: quit
	

