# Need to access symbols from the X Server and other dlopen'ed modules
%define _disable_ld_no_undefined 1

Name:		x11-driver-video-vesa
Version:	2.6.0.3
Release:	1
Summary:	X.org driver for Generic VESA Cards
Group:		System/X11
License:	MIT
URL:		https://xorg.freedesktop.org
# Switch to xlibre version instead of almost unmaintainded freedesktop
Source0:  https://github.com/X11Libre/xf86-video-vesa/archive/refs/tags/xlibre-xf86-video-vesa-%{version}.tar.gz
#Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vesa-%{version}.tar.xz
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-server-devel >= 1.18
BuildRequires:	x11-util-macros >= 1.0.1

Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

Obsoletes:	x11-driver-video-vga
Obsoletes:	x11-driver-video-vermilion

%description
x11-driver-video-vesa is the X.org driver for Generic VESA Cards.

%prep
%autosetup -n xf86-video-vesa-xlibre-xf86-video-vesa-%{version} -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%files
%{_libdir}/xorg/modules/xlibre-*.*/drivers/vesa_drv.so
%{_mandir}/man4/vesa.4*
