# Conditional build:
%bcond_without	tests	# unit tests

Summary:	re2c - a tool for writing very fast and very flexible scanners
Summary(pl.UTF-8):	re2c - narzędzie do pisania bardzo szybkich i elastycznych skanerów
Name:		re2c
Version:	4.6
Release:	1
License:	Public Domain
Group:		Applications/Text
#Source0Download: https://github.com/skvadrik/re2c/releases
Source0:	https://github.com/skvadrik/re2c/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	4bee1f1531980bd06cc325c174577210
URL:		http://re2c.org/
BuildRequires:	libstdc++-devel
%{?with_tests:BuildRequires:	python3}
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
%configure
%{__make}

%if %{with tests}
%{__make} check
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG NO_WARRANTY README.md examples
%attr(755,root,root) %{_bindir}/re2c
%attr(755,root,root) %{_bindir}/re2d
%attr(755,root,root) %{_bindir}/re2go
%attr(755,root,root) %{_bindir}/re2hs
%attr(755,root,root) %{_bindir}/re2java
%attr(755,root,root) %{_bindir}/re2js
%attr(755,root,root) %{_bindir}/re2ocaml
%attr(755,root,root) %{_bindir}/re2py
%attr(755,root,root) %{_bindir}/re2rust
%attr(755,root,root) %{_bindir}/re2swift
%attr(755,root,root) %{_bindir}/re2v
%attr(755,root,root) %{_bindir}/re2zig
%{_datadir}/re2c
%{_mandir}/man1/re2c.1*
%{_mandir}/man1/re2d.1*
%{_mandir}/man1/re2go.1*
%{_mandir}/man1/re2hs.1*
%{_mandir}/man1/re2java.1*
%{_mandir}/man1/re2js.1*
%{_mandir}/man1/re2ocaml.1*
%{_mandir}/man1/re2py.1*
%{_mandir}/man1/re2rust.1*
%{_mandir}/man1/re2swift.1*
%{_mandir}/man1/re2v.1*
%{_mandir}/man1/re2zig.1*
