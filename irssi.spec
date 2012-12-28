Name:		irssi
Version:	0.8.15
Release:	8
Summary:	IRC client
License:	GPLv2+
Group:		Networking/IRC
BuildRequires:	pkgconfig(glib-2.0) pkgconfig(ncursesw) pkgconfig(openssl)
BuildRequires:	perl-devel
URL:		http://irssi.org/
Source0:	http://irssi.org/files/%{name}-%{version}.tar.gz
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
%configure2_5x	--with-modules \
		--enable-ipv6 \
		--with-proxy \
		--with-socks \
		--with-bot \
		--with-perl=module \
		--with-perl-lib=vendor
%make

%install
%makeinstall_std

# Files that should not be installed:
rm -f %{buildroot}%{perl_vendorarch}/perllocal.pod
rm -rf %{buildroot}%{_docdir}/%{name}

%files
%doc AUTHORS README TODO NEWS docs/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/scripts
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%exclude %{_libdir}/%{name}/modules/libfe_perl.*
%exclude %{_libdir}/%{name}/modules/libperl_core.*
%{_libdir}/%{name}/modules/*.so
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/man1/%{name}.1*

%files devel
%{_libdir}/%{name}/modules/*.a
%{_includedir}/%{name}

%files perl
%{_libdir}/%{name}/modules/libfe_perl.so
%{_libdir}/%{name}/modules/libperl_core.so
%{perl_vendorarch}/Irssi*
%{perl_vendorarch}/auto/*
%{_datadir}/%{name}/scripts

%changelog
* Fri Dec 28 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.8.15-8
- use pkgconfig() deps for buildrequires
- rebuild for new perl

* Wed Feb 01 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.8.15-7
+ Revision: 770478
- use versioned perl-devel dependency to get required linker flag fix
- replace dead --with-plugins configurie option with --with-modules
- cleanups
- svn commit -m mass rebuild of perl extension against perl 5.14.2

  + Bogdano Arendartchuk <bogdano@mandriva.com>
    - rebuild for new perl

* Wed Apr 06 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 0.8.15-6
+ Revision: 651341
- rebuild for yet another new perl

* Sun Sep 19 2010 Jérôme Quelin <jquelin@mandriva.org> 0.8.15-5mdv2011.0
+ Revision: 579815
- rebuild with perl 5.12.2

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.8.15-4mdv2011.0
+ Revision: 564282
- rebuild for new perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.8.15-3mdv2011.0
+ Revision: 555225
- rebuild

* Thu Apr 08 2010 Eugeni Dodonov <eugeni@mandriva.com> 0.8.15-2mdv2010.1
+ Revision: 533005
- Rebuild for new openssl

* Thu Apr 08 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.8.15-1mdv2010.1
+ Revision: 532875
- New release 0.8.15

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.14-3mdv2010.1
+ Revision: 511580
- rebuilt against openssl-0.9.8m

* Wed Sep 09 2009 Jérôme Quelin <jquelin@mandriva.org> 0.8.14-2mdv2010.0
+ Revision: 435589
- rebuild

* Wed Jul 29 2009 Michael Scherer <misc@mandriva.org> 0.8.14-1mdv2010.0
+ Revision: 402975
- new version
- remove patch0, applied upstream

* Tue Jun 16 2009 Oden Eriksson <oeriksson@mandriva.com> 0.8.13-2mdv2010.0
+ Revision: 386334
- P0: security fix for CVE-2009-1959

* Sat May 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.13-1mdv2010.0
+ Revision: 373851
- new version

* Mon Dec 15 2008 Michael Scherer <misc@mandriva.org> 0.8.12-4mdv2009.1
+ Revision: 314415
- update license
- move script to perl subpackage, as proposed by gustavodn

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.8.12-3mdv2009.0
+ Revision: 170344
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Tue Jan 22 2008 Gustavo De Nardin <gustavodn@mandriva.com> 0.8.12-3mdv2008.1
+ Revision: 156079
- rebuild for perl-5.10.0
- Patch0: in perl 5.10.0, DynaLoader is in libperl

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild for new perl
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Oct 21 2007 Anssi Hannula <anssi@mandriva.org> 0.8.12-1mdv2008.1
+ Revision: 100741
- new version
- drop patch0, fixed upstream

* Sun Oct 21 2007 Anssi Hannula <anssi@mandriva.org> 0.8.11-2mdv2008.1
+ Revision: 100730
- build with SSL support (br was missing)

  + Pixel <pixel@mandriva.com>
    - add explict conflict from irssi-perl on perl-silc

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - fix race condition wrt parallel builds (P0)
    - cosmetics

* Mon Apr 30 2007 Michael Scherer <misc@mandriva.org> 0.8.11-1mdv2008.0
+ Revision: 19594
- remove regeneration of Makefile, as this is not needed anymore
- 0.8.11, patch 0 included upstream


* Thu Mar 01 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.8.10-10mdv2007.0
+ Revision: 130754
- do not package huge (1.2Mb!) ChangeLog
- do not package huge (1.2Mb!) ChangeLog

  + Michael Scherer <misc@mandriva.org>
    - remove svn:mime-type from patch, as they are no longer binaries
    - remove unused macros
    - also bunzip the patch file ( i ran the commit from a wrong place )
    - bunzip patch
    - Import irssi

* Tue Sep 19 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 0.8.10-9
- Rebuild

* Thu Aug 10 2006 Michael Scherer <misc@mandriva.org> 0.8.10-8mdv2007.0
- Rebuild

* Fri Jul 21 2006 Michael Scherer <misc@mandriva.org> 0.8.10-7mdv2007.0
- Remove old menu, as this is a non graphical irc client

* Thu Apr 27 2006 Michael Scherer <misc@mandriva.org> 0.8.10-6mdk
- fix 22151, sotlen ubuntu and irssi patch

* Wed Jan 25 2006 Michael Scherer <misc@mandriva.org> 0.8.10-5mdk
- remove artificial perl deps on main package, as we splitted in irssi-perl

* Fri Jan 20 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.8.10-4mdk
- Rebuild for new perl

* Mon Dec 12 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.8.10-3mdk
- fix build with automake 1.7

* Sun Dec 11 2005 Michael Scherer <misc@mandriva.org> 0.8.10-2mdk
- fix backporting ( regenerate configure )
- fix BuildRequires
- compile perl as a module

* Sun Dec 11 2005 Michael Scherer <misc@mandriva.org> 0.8.10-1mdk
- 0.8.10

* Mon Nov 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.10-0.rc5.20050809.3mdk
- rebuilt against openssl-0.9.8a

* Fri Aug 12 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.8.10-0.rc5.20050809.2mdk
- fix multiarch

* Fri Aug 12 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.8.10-0.rc5.20050809.1mdk
- update to 0.8.10-rc5 (svn snapshot from 20050809)
- drop P0 (fixed upstream)
- do libtoolize again
- add headers to devel package

* Fri May 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.8.9-7mdk
- Rebuild for new perl
- Patch 0 to build with gcc 4.0.0

* Fri Mar 25 2005 Michael Scherer <misc@mandrake.org> 0.8.9-6mdk
- Rebuild to fix #14964
- fix summary

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.8.9-5mdk
- Rebuild for new perl; description nits

* Thu Jul 08 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.8.9-4mdk
- Rebuild for new perl

* Wed Apr 07 2004 Michael Scherer <misc@mandrake.org> 0.8.9-3mdk
- rebuild for new perl
- change menu section

