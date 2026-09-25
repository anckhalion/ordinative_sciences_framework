# Ordinative Sciences Framework — maintenance targets.
# Every target is a thin wrapper around a command documented in docs/handbook/07_MAINTAINERS_GUIDE.md.
PYTHON ?= python3

.PHONY: help test test-lexx test-casework check dist manifest lock package

help:
	@echo "make test      run the LEXX and CASEWORK test suites"
	@echo "make check     manifest, lock, compatibility profiles, derived files, docs, links"
	@echo "make dist      rebuild dist/ and llms.txt from FRAMEWORKS/"
	@echo "make manifest  regenerate FRAMEWORKS/MANIFEST_SHA256.txt (after a change to a canonical file)"
	@echo "make lock      regenerate FRAMEWORKS/te_frameworks.lock.json (then re-pin the compatibility profiles)"
	@echo "make package   build the download archive dist/te-frameworks-<version>.zip (not committed)"

test: test-lexx test-casework

test-lexx:
	cd FRAMEWORKS/LEXX/v0_2_alpha3 && $(PYTHON) -m unittest discover -s tests

test-casework:
	mkdir -p tmp && cd FRAMEWORKS/CASEWORK && TMPDIR=$(CURDIR)/tmp $(PYTHON) -m unittest discover -s tests

check:
	$(PYTHON) tools/check_repo.py

dist:
	$(PYTHON) tools/build_dist.py

manifest:
	$(PYTHON) tools/build_dist.py --write-manifest

lock:
	$(PYTHON) FRAMEWORKS/CASEWORK/runtime/make_lock.py --framework-root FRAMEWORKS --out FRAMEWORKS/te_frameworks.lock.json --force

package: dist
	$(PYTHON) tools/build_dist.py --zip
