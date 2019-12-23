PYTHON_FILES := $(wildcard *.py)
DOCTEST_FILES := $(patsubst %.py,%.doctest,$(PYTHON_FILES))
LINT_FILES := $(patsubst %.py,%.lint,$(PYTHON_FILES))

.SILENT:

%.doctest : %.py
	python -mdoctest $< | tee $@
	if [[ -s $@ ]]; then exit 1; else rm -f $@; fi

%.lint : %.py
	pylint -rn $< | grep $< | sort -t: -k2 -n -r | tee $@
	if [[ -s $@ ]]; then exit 1; else rm -f $@; fi

checks: isort black lint lama doctest

black: $(PYTHON_FILES)
	black -q $?

clean:
	git clean -dfx

doctest: $(DOCTEST_FILES)

isort:
	isort $(PYTHON_FILES)

lama : $(PYTHON_FILES)
	pylama $? --ignore E203		# conflicts with black formatting

lint: $(LINT_FILES)

.PHONY: black checks clean doctest isort lama lint
