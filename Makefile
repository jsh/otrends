PYTHON_FILES := $(wildcard *.py)
LINT_FILES := $(patsubst %.py,%.lint,$(PYTHON_FILES))

.SILENT:

%.lint : %.py
	pylint -rn $< | grep $< | sort -t: -k2 -n -r | tee $@
	if [[ -s $@ ]]; then exit 1; else rm -f $@; fi

checks: black lint lama doctest

black: $(PYTHON_FILES)
	black -q $?

doctest:
	for i in $(PYTHON_FILES); do python -mdoctest $$i; done

lama : $(PYTHON_FILES)
	pylama $? --ignore E203		# conflicts with black formatting

lint: $(LINT_FILES)

.PHONY: checks black doctest lama lint
