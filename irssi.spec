%define	name	irssi
%define version 0.8.11
%define	rel	1

Name:		%{name}
Version:	%{version}
Release: 	%mkrel %{rel}
Summary:	Irssi is an IRC client
License:	GPL
Group:		Networking/IRC
BuildRequires:	glib2-devel ncurses-devel perl-devel
URL:		http://irssi.org/
Source0:	http://irssi.org/irssi/files/%{name}-%{version}.tar.bz2
Patch0:		irssi-0.8.11-makefile-race-fix.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package	perl
Group:		Networking/IRC
Summary:	Perl plugin for irssi
Requires:	%{name} = %{version}
Conflicts:	perl-silc

%description	perl
Perl plugin for irssi.

%prep
%setup -q 
%patch0 -p1 -b .parallel

%build
%configure2_5x	--with-plugins \
		--enable-ipv6 \
		--with-proxy \
		--with-socks \
		--with-bot \
		--with-perl=module \
		--with-perl-lib=%{perl_vendorlib}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

# Files that should not be installed:
rm -f %{buildroot}%{perl_vendorarch}/perllocal.pod
rm -rf %{buildroot}%{_docdir}/%{name}

%multiarch_includes %{buildroot}%{_includedir}/%{name}/config.h

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc AUTHORS README TODO NEWS docs/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%exclude %{_libdir}/%{name}/modules/libfe_perl.*
%exclude %{_libdir}/%{name}/modules/libperl_core.*
%{_libdir}/%{name}/modules/*.so
%{_libdir}/%{name}/modules/*.la
%{_libdir}/%{name}/modules/*so.*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/man1/%{name}.1*

%files devel
%defattr(-,root,root)
%{_libdir}/%{name}/modules/*.a
%{_includedir}/%{name}
%multiarch %{multiarch_includedir}/%{name}

%files perl
%defattr(-,root,root)
%{_libdir}/%{name}/modules/libfe_perl.so
%{_libdir}/%{name}/modules/libfe_perl.la
%{_libdir}/%{name}/modules/libperl_core.so
%{_libdir}/%{name}/modules/libperl_core.la
%{perl_vendorarch}/Irssi*
%{perl_vendorarch}/auto/*
