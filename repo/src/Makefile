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
	$(MAKE) build

buildw: 
	python -m PyInstaller --distpath ../../install/exe --noconsole $(MAIN)
	python -m PyInstaller --distpath ../../install/exe $(PROF)
	$(MAKE) clean
## spustí build jen s exe souborem jako výstup
build:
	python -m PyInstaller --distpath ../../install/exe --onefile --noconsole $(MAIN)
	python -m PyInstaller --distpath ../../install/exe --onefile $(PROF)
	$(MAKE) clean
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
	del /Q *.zip *.out *.log *.aux *.toc *.spec 2>nul || exit 0
	rmdir /S /Q __pycache__ 2>nul || exit 0
	rmdir /S /Q build 2>nul || exit 0


## Zabalí projekt do zipu – včetně zdrojáků, dokumentace a Makefile
pack: clean
	PowerShell Compress-Archive -Path ../../ -DestinationPath ../../$(DIST) -Force



## Profilovaný výpočet směrodatné odchylky – příkladový skript
stddev:
	pip install -r requirements.txt || true
	python -m PyInstaller --onefile $(PROF)
	$(MAKE) clean

# Pokud není uveden žádný cíl, běží defaultně all
.DEFAULT_GOAL := all
