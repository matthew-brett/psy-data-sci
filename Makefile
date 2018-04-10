default: psy_data_sci_slides.pdf

%.pdf : %.md
	pandoc --filter pandoc-citeproc -t beamer -s $< -o $@
