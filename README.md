# pkg-marisa
RPM packaging of marisa for Sailfish

This is packaging scripts for "MARISA: Matching Algorithm with
Recursively Implemented StorAge". MARISA homepage is at
http://s-yata.github.io/marisa-trie/docs/readme.en.html . To download
the latest release, URL from osmscout-sailfish
(https://github.com/Karry/osmscout-sailfish).


## Howto build

* Clone this repository

* cd into it and run ./download.sh

* cd into marisa source directory (at time of writing, marisa-0.2.4)

* build by running 
'''
export SFARCH=armv7hl; mb2 -t SailfishOS-$SFARCH -s ../rpm/marisa.spec build
'''
in MER SDK.

* RPMs are under RPMS directory.

Please let me know if there are some errors (missing dependencies, for
example) during building by opening an issue for this repository.
