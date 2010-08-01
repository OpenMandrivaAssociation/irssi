%define	name	irssi
%define version 0.8.15
%define	rel	4

Name:		%{name}
Version:	%{version}
Release: 	%mkrel %{rel}
Summary:	IRC client
License:	GPLv2+
Group:		Networking/IRC
BuildRequires:	glib2-devel ncurses-devel perl-devel openssl-devel
URL:		http://irssi.org/
Source0:	http://irssi.org/files/%{name}-%{version}.tar.gz
Suggests:   irssi-perl
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

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc AUTHORS README TODO NEWS docs/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/scripts
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%exclude %{_libdir}/%{name}/modules/libfe_perl.*
%exclude %{_libdir}/%{name}/modules/libperl_core.*
%{_libdir}/%{name}/modules/*.so
%{_libdir}/%{name}/modules/*.la
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/man1/%{name}.1*

%files devel
%defattr(-,root,root)
%{_libdir}/%{name}/modules/*.a
%{_includedir}/%{name}

%files perl
%defattr(-,root,root)
%{_libdir}/%{name}/modules/libfe_perl.so
%{_libdir}/%{name}/modules/libfe_perl.la
%{_libdir}/%{name}/modules/libperl_core.so
%{_libdir}/%{name}/modules/libperl_core.la
%{perl_vendorarch}/Irssi*
%{perl_vendorarch}/auto/*
%{_datadir}/%{name}/scripts

