Summary:	AGFL is the parser generator for natural languages
Summary(pl):	AGFL jest generatorem parserow jezykow naturalnych
Name:		agfl
Version:	2.3
Release:	0.1
License:	GPL, partialy LGPL
Group:		Development/Languages
Source0:	ftp://ftp.cs.kun.nl/pub/agfl/2.0/unix/sources/%{name}-%{version}.tar.gz
# Source0-md5:	e093223c953882a571de9426fa32d984
Patch0:		%{name}-acam.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cdl3
BuildRequires:	libtool
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AGFL

%description -l pl
AGFL

%prep
%setup -q
%patch0

%build
rm -f missing
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

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%doc doc/userdoc/*.ps README
