Name: x11-driver-video-vesa
Version: 1.99.1
Release: %mkrel 2
Summary: X.org driver for Generic VESA Cards
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vesa-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

# git-diff xf86-video-vesa-1.99.1..1a256385169d61c6f42cb6f6d0eb1688570fd79e
Patch0:	xf86-video-vesa-1.99.1-revert-to-version-that-works-with-xserver-1.4.patch
 
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

%description
x11-driver-video-vesa is the X.org driver for Generic VESA Cards.

%prep
%setup -q -n xf86-video-vesa-%{version}

%patch0 -p1

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
