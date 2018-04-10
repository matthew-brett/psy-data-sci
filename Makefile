default: psy_data_sci_slides.pdf
reveal: psy_data_sci_slides.html

%.pdf : %.md
	pandoc --filter pandoc-citeproc -t beamer -s $< -o $@

%.html : %.md
	# May need git submodule add https://github.com/hakimel/reveal.js to make
	# this one work.
	pandoc -t revealjs -s -o $@ $< -V revealjs-url=./reveal.js

clean:
	rm *.pdf *.html
