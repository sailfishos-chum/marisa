Name: libmarisa

%define keepstatic 1

Summary: MARISA: Matching Algorithm with Recursively Implemented StorAge
Version: 0.2.6
Release: 1%{?dist}
License: LGPL and BSD 2-clause license
Group: Libraries/Databases
URL: https://github.com/s-yata/marisa-trie

#Source: https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/marisa-trie/marisa-0.2.4.tar.gz
Source0: %{name}-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires: gcc-c++
#Requires: pango

%description
Matching Algorithm with Recursively Implemented StorAge (MARISA) is a
space-efficient trie data structure. libmarisa is a C++ library for an
implementation of MARISA. Users can build dictionaries and search keys
from the dictionaries. The package also provides command line tools to
test basic operations of libmarisa, and the tools are useful to test
the performance.

Categories:
  - Library

%package devel
Summary: MARISA development headers and static library
Group: Development/Libraries
#Requires: %%{name} = %%{version}

%description devel
Matching Algorithm with Recursively Implemented StorAge (MARISA) is a
space-efficient trie data structure. This package provides libraries
and headers for development

Categories:
  - Library

%package tools
Summary: MARISA tools
Group: Libraries/Databases
Requires: %{name} = %{version}

%description tools
Matching Algorithm with Recursively Implemented StorAge (MARISA) is a
space-efficient trie data structure. The package provides command line
tools to test basic operations of libmarisa, and the tools that are
useful to test the performance.

Categories:
  - Utility

%prep

%setup -q -n %{name}-%{version}/marisa-trie

%build
%{__make} clean || true

CFLAGS="$CFLAGS -fPIC"
CXXFLAGS="$CXXFLAGS -fPIC"
%reconfigure

%{make_build}

%install
%{make_install}
%{__rm} -rf %{buildroot}%{_libdir}/libmarisa.la || true

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/libmarisa.so.0
%{_libdir}/libmarisa.so.0.0.0

%files devel
%{_libdir}/libmarisa.so
%{_includedir}/marisa
%{_includedir}/marisa.h
%{_libdir}/libmarisa.a
%{_libdir}/pkgconfig/marisa.pc

%files tools
%{_bindir}/marisa-*

%changelog
* Sat Oct 1 2016 rinigus <rinigus.git@gmail.com> - 0.2.4-1
- initial packaging release for SFOS
