Name: x11-driver-video-vesa
Version: 1.3.0
Release: %mkrel 7
Summary: X.org driver for Generic VESA Cards
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vesa-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
 
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

Patch1: 0001-Don-t-disable-FB-access-when-it-s-already-disabled.patch
Patch2: 0002-Bug-11090-xf86-video-vesa-COPYING-file.patch
Patch3: 0003-Remove-all-trace-of-mfb.patch

%description
The X.org driver for Generic VESA Cards

%prep
%setup -q -n xf86-video-vesa-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/vesa_drv.la
%{_libdir}/xorg/modules/drivers/vesa_drv.so
%{_mandir}/man4/vesa.4*
