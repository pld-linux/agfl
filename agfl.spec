Summary:	AGFL - parser generator for natural languages
Summary(pl.UTF-8):	AGFL - generator parserów języków naturalnych
Name:		agfl
Version:	2.3
Release:	0.1
License:	GPL, partialy LGPL
Group:		Development/Languages
Source0:	ftp://ftp.cs.kun.nl/pub/agfl/2.0/unix/sources/%{name}-%{version}.tar.gz
# Source0-md5:	59c7f460ffba3589a06bd881d1162707
Patch0:		%{name}-acam.patch
Patch1:		%{name}-c++.patch
Patch2:		%{name}-flex.patch
URL:		http://www.cs.kun.nl/agfl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cdl3
BuildRequires:	flex
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The AGFL parser generation system for Natural Languages generates
efficient parsers from AGFL grammars. It includes a lexicon system
suitable for the large lexica needed in real life NLP applications.

%description -l pl.UTF-8
System generowania parserów AGFL dla języków naturalnych generuje
wydajne parsery z gramatyk AGFL. Zawiera system leksykalny odpowiedni
dla dużych słowników potrzebnych w prawdziwych aplikacjach NLP.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

rm -f utils/scanner.cc

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-readline=%{_usr}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/userdoc/*.ps README
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*.h
%{_libdir}/lib*.la
%{_libdir}/lib*.a
%{_mandir}/man1/*
