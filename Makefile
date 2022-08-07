.PHONY: test

dirs: $(wildcard ch*)
test: 
	poetry run pytest $(dirs)
