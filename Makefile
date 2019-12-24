PYTHON_FILES := $(wildcard *.py)
DOCTEST_FILES := $(patsubst %.py,%.test,$(PYTHON_FILES))
LINT_FILES := $(patsubst %.py,%.lint,$(PYTHON_FILES))

.SILENT:

%.test : %.py
	python -mdoctest $< | tee $@
	if [[ -s $@ ]]; then exit 1; else rm -f $@; fi

%.lint : %.py
	pylint -rn $< | grep $< | sort -t: -k2 -n -r | tee $@
	if [[ -s $@ ]]; then exit 1; else rm -f $@; fi

checks: format doctest

format: isort black lint lama

black: $(PYTHON_FILES)
	black -q $?

clean:
	git clean -dfx

test: $(DOCTEST_FILES)

isort:
	isort $(PYTHON_FILES)

lama : $(PYTHON_FILES)
	pylama $? --ignore E203		# conflicts with black formatting

lint: $(LINT_FILES)

.PHONY: black checks clean doctest isort lama lint
