Name: x11-driver-video-vesa
Version: 1.3.0
Release: %mkrel 6
Summary: The X.org driver for Generic VESA Cards
Group: System/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-vesa  xorg/drivers/xf86-video-vesa
# cd xorg/drivers/xf86-video/vesa
# git-archive --format=tar --prefix=xf86-video-vesa-1.3.0/ xf86-video-vesa-1.3.0 | bzip2 -9 > xf86-video-vesa-1.3.0.tar.bz2
########################################################################
Source0: xf86-video-vesa-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-video-vesa-1.3.0..origin/mandriva+gpl
Patch1: 0001-Add-conditional-support-for-pci-rework-branch.patch
Patch2: 0002-Correct-ifdef-to-ifndef-.-Oops.patch
Patch3: 0003-Remove-all-trace-of-mfb.patch
Patch4: 0004-Don-t-disable-FB-access-when-it-s-already-disabled.patch
Patch5: 0005-Rename-.cvsignore-to-.gitignore.patch
Patch6: 0006-Add-to-.gitignore-to-skip-patch-emacs-droppings.patch
Patch7: 0007-Use-XSERVER_LIBPCIACCESS-to-autodetect-libpciaccess.patch
Patch8: 0008-Use-pci_device_map_range-instead-of-pci_device_map_m.patch
Patch9: 0009-Bug-11090-xf86-video-vesa-COPYING-file.patch
Patch10:0010-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
Patch11:0011-Fix-oversight-not-adding-macro-to-check-for-conditio.patch
########################################################################
BuildRequires: x11-util-macros		>= 1.1.5-4mdk
BuildRequires: libpixman-1-devel	>= 0.9.6
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: x11-server-devel		>= 1.4
Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for Generic VESA Cards

%prep
%setup -q -n xf86-video-vesa-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/drivers/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/vesa_drv.so
%{_mandir}/man4/vesa.4*
