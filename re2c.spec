Summary:	re2c - a tool for writing very fast and very flexible scanners
Summary(pl.UTF-8):	re2c - narzędzie do pisania bardzo szybkich i elastycznych skanerów
Name:		re2c
Version:	1.1.1
Release:	1
License:	Public Domain
Group:		Applications/Text
#Source0Download: https://github.com/skvadrik/re2c/releases
Source0:	https://github.com/skvadrik/re2c/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7355fde733bd76cbc480cda10ef49e46
URL:		http://re2c.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.11
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
re2c is a tool for writing very fast and very flexible scanners.
Unlike any other such tool, re2c focuses on generating high efficient
code for regular expression matching. As a result this allows a much
broader range of use than any traditional lexer offers. And last but
not least re2c generates warning free code that is equal to
hand-written code in terms of size, speed and quality.

%description -l pl.UTF-8
re2c to narzędzie do pisania bardzo szybkich i bardzo elastycznych
skanerów. W przeciwieństwie do innych podobnych narzędzi re2c skupia
się na bardzo wydajnym kodzie do dopasowywania wyrażeń regularnych. W
efekcie pozwala to na dużo szerszy zakres zastosowań niż oferują
tradycyjne leksery. I wreszcie re2c generuje kod wolny od ostrzeżeń,
równoważny kodowi pisanemu ręcznie pod kątem rozmiaru, szybkości i
jakości.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README doc/* examples
%attr(755,root,root) %{_bindir}/re2c
%{_mandir}/man1/re2c.1*
