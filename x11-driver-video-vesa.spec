# Need to access symbols from the X Server and other dlopen'ed modules
%define _disable_ld_no_undefined 1

Name: x11-driver-video-vesa
Version: 2.3.1
Release: 2
Summary: X.org driver for Generic VESA Cards
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vesa-%{version}.tar.bz2

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

Obsoletes: x11-driver-video-vga
Obsoletes: x11-driver-video-vermilion

%description
x11-driver-video-vesa is the X.org driver for Generic VESA Cards.

%prep
%setup -qn xf86-video-vesa-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/drivers/vesa_drv.so
%{_mandir}/man4/vesa.4*

