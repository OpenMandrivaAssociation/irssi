%define _disable_ld_no_undefined 1
%bcond_with perl

Summary:	IRC client
Name:		irssi
Version:	1.2.1
Release:	1
License:	GPLv2+
Group:		Networking/IRC
Url:		http://irssi.org/
Source0:	https://github.com/irssi/irssi/archive/%{version}.tar.gz
%if %{with perl}
BuildRequires:	perl-devel
%endif
BuildRequires:	git-core
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(openssl)
Suggests:	irssi-perl

%description
Irssi is a modular and flexible IRC client for UNIX that has only a text mode
user interface (but as 80-90% of the code isn't text mode specific, other UIs
could be created pretty easily). Also, Irssi isn't really even IRC specific
anymore, there are already working SILC and ICB modules available. Support for
other protocols like ICQ and Jabber could be created some day too.

Irssi is one of the most popular IRC clients at the moment.

%package	devel
Group:		Development/C
Summary:	Static libraries for the development of irssi applications
Requires:	%{name} = %{version}

%description	devel
Static libraries for the development of irssi applications.

%if %{with perl}
%package	perl
Group:		Networking/IRC
Summary:	Perl plugin for irssi
Requires:	%{name} = %{version}
Conflicts:	perl-silc

%description	perl
Perl plugin for irssi.
%endif

%prep
%setup -q

%build
git config --global user.email "builder@openmandriva.org"
git config --global user.name "builder"
git init
git add . && git commit -am 'init'
bash autogen.sh
%configure \
	--disable-static \
	--enable-true-color \
	--with-modules \
	--enable-ipv6 \
	--with-proxy \
	--with-socks \
	--with-bot \
%if %{with perl}
	--with-perl=module \
%endif
	--with-perl-lib=vendor
%make

%install
%makeinstall_std

# Files that should not be installed:
rm -r %{buildroot}%{_docdir}/%{name}

%files
%doc AUTHORS README.md TODO NEWS docs/*
%{_bindir}/*
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/scripts
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%if %{with perl}
%exclude %{_libdir}/%{name}/modules/libfe_perl.*
%exclude %{_libdir}/%{name}/modules/libperl_core.*
%endif
%{_libdir}/%{name}/modules/*.so
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/man1/%{name}.1*

%files devel
%{_includedir}/%{name}

%if %{with perl}
%files perl
%{_libdir}/%{name}/modules/libfe_perl.so
%{_libdir}/%{name}/modules/libperl_core.so
%{perl_vendorarch}/Irssi*
%{perl_vendorarch}/auto/*
%{_datadir}/%{name}/scripts
%endif
