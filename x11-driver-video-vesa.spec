# Need to access symbols from the X Server and other dlopen'ed modules
%define _disable_ld_no_undefined 1

Name:		x11-driver-video-vesa
Version:	2.3.3
Release:	5
Summary:	X.org driver for Generic VESA Cards
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vesa-%{version}.tar.bz2
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-server-devel >= 1.12
BuildRequires:	x11-util-macros >= 1.0.1

Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

Obsoletes:	x11-driver-video-vga
Obsoletes:	x11-driver-video-vermilion

%description
x11-driver-video-vesa is the X.org driver for Generic VESA Cards.

%prep
%setup -qn xf86-video-vesa-%{version}
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/drivers/vesa_drv.so
%{_mandir}/man4/vesa.4*



%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.3.2-1
+ Revision: 810692
- version update 2.3.2

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 2.3.1-2
+ Revision: 787288
- Rebuild for x11-server 1.12

* Mon Mar 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.3.1-1
+ Revision: 786903
- version update 2.3.1

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.3.0-9
+ Revision: 748477
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 2.3.0-8
+ Revision: 703670
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 2.3.0-7
+ Revision: 683554
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 2.3.0-6
+ Revision: 671185
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 2.3.0-5mdv2011.0
+ Revision: 595708
- new release

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 2.3.0-4mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Wed Feb 17 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 2.3.0-3mdv2010.1
+ Revision: 507238
- Obsolete x11-driver-video-vermilion

* Fri Feb 12 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 2.3.0-2mdv2010.1
+ Revision: 504708
- Obsolete vga driver

* Tue Jan 05 2010 Thierry Vignaud <tv@mandriva.org> 2.3.0-1mdv2010.1
+ Revision: 486392
- new release

* Tue Nov 10 2009 Thierry Vignaud <tv@mandriva.org> 2.2.1-2mdv2010.1
+ Revision: 464336
- rebuild for new xserver

* Sun Aug 02 2009 Frederik Himpe <fhimpe@mandriva.org> 2.2.1-1mdv2010.0
+ Revision: 407497
- Update to new version 2.2.1
  _ Use %%configure2_5x macro to fix build

* Wed Feb 18 2009 Thierry Vignaud <tv@mandriva.org> 2.2.0-1mdv2009.1
+ Revision: 342280
- new release

* Wed Dec 31 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.1.0-1mdv2009.1
+ Revision: 321579
- update to new version 2.1.0

  + Colin Guthrie <cguthrie@mandriva.org>
    - Rebuild for new xserver

* Sun Nov 30 2008 Adam Williamson <awilliamson@mandriva.org> 2.0.0-1mdv2009.1
+ Revision: 308211
- drop the X server 1.4 patch now we're using X server 1.5
- rebuild for new X server
- new release 2.0.0

* Wed Jun 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.99.1-2mdv2009.0
+ Revision: 225752
- Added _disable_ld_no_undefined because the driver accesses symbols from
  the X Server and other dlopen'ed modules.
- Revert to a version that works with X Server 1.4 branch.

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.99.1-1mdv2009.0
+ Revision: 219400
- new release (and drop git patches)
- improved description
- add missing dot at end of description
- improved summary

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.3.0-7mdv2008.1
+ Revision: 166183
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.3.0-6mdv2008.1
+ Revision: 156627
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.3.0-5mdv2008.1
+ Revision: 154786
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Update to properly use existing tag xf86-video-vesa-1.3.0, and generated
  patches from that point, up to mandriva branch.
- Update for new policy of hidden symbols and common macros.
--
  Deleted patches are already applied in master.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 16 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.3.0-4mdv2008.1
+ Revision: 99059
- minor spec cleanup
- build against new xserver (1.4)

* Thu Aug 09 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.3.0-3mdv2008.0
+ Revision: 60881
- Replace the randr fix by the proper fix done upstream
- Add one more fix removing mfb code

