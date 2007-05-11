#
# Conditional build:
#%%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
#
Summary:	-
Summary(pl.UTF-8):	-
Name:		re2c
Version:	0.12.0
Release:	1
License:	Public Domain
Group:		Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	68d6d1faf26179a7fe1f2d348cf90ac8
URL:		http://re2c.org/
#BuildRequires:	-
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
#Requires(postun):	-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires:	-
#Provides:	-
#Provides:	group(foo)
#Provides:	user(foo)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%prep
%setup -q

%build
#%%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
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
%doc CHANGELOG README doc/* examples lessons
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
