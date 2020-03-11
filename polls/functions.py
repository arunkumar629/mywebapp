def handle_uploaded_file(f):
	fr=open(f.name, 'wb')
	for chunk in f.chunks():
		fr.write(chunk)