# Makefile pro Python projekt s testy, dokumentací a profilingem

# Hlavní skripty a složky
MAIN=mockup.py
TEST=test_calc_lib.py
DIST=projekt.zip
PROF=stddev.py

.PHONY: all clean pack test doc run stddev

## Spustí celý build – simulace "překladu" v Pythonu (např. instalace závislostí + profiling skriptu)
all:
	pip install -r requirements.txt || true

## Spustí testy pomocí unittest
test:
	python -m unittest $(TEST)

## Spustí dokumentaci pomocí Doxygenu
doc:
	doxygen Doxyfile

## Spustí hlavní skript
run:
	python $(MAIN)

## Vyčistí dočasné nebo generované soubory
clean:
	del /Q *.zip *.out *.log *.aux *.toc 2>nul || exit 0
	rmdir /S /Q __pycache__ 2>nul || exit 0
	rmdir /S /Q build 2>nul || exit 0


## Zabalí projekt do zipu – včetně zdrojáků, dokumentace a Makefile
pack:
	PowerShell Compress-Archive -Path ../ -DestinationPath ../$(DIST)



## Profilovaný výpočet směrodatné odchylky – příkladový skript
stddev:
	python $(PROF)

# Pokud není uveden žádný cíl, běží defaultně all
.DEFAULT_GOAL := all
