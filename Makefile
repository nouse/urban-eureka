.PHONY: test

dirs: $(wildcard ch*)
test: 
	pytest $(dirs)
