#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-desktop-testing
Version  : 2018.1
Release  : 1
URL      : https://gitlab.gnome.org/GNOME/gnome-desktop-testing/-/archive/v2018.1/gnome-desktop-testing-v2018.1.tar.gz
Source0  : https://gitlab.gnome.org/GNOME/gnome-desktop-testing/-/archive/v2018.1/gnome-desktop-testing-v2018.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0
Requires: gnome-desktop-testing-bin = %{version}-%{release}
Requires: gnome-desktop-testing-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(libsystemd)

%description
See:
https://live.gnome.org/Initiatives/GnomeGoals/InstalledTests

%package bin
Summary: bin components for the gnome-desktop-testing package.
Group: Binaries
Requires: gnome-desktop-testing-license = %{version}-%{release}

%description bin
bin components for the gnome-desktop-testing package.


%package license
Summary: license components for the gnome-desktop-testing package.
Group: Default

%description license
license components for the gnome-desktop-testing package.


%prep
%setup -q -n gnome-desktop-testing-v2018.1
cd %{_builddir}/gnome-desktop-testing-v2018.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587382106
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1587382106
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-desktop-testing
cp %{_builddir}/gnome-desktop-testing-v2018.1/COPYING %{buildroot}/usr/share/package-licenses/gnome-desktop-testing/bf50bac24e7ec325dbb09c6b6c4dcc88a7d79e8f
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ginsttest-runner
/usr/bin/gnome-desktop-testing-runner

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-desktop-testing/bf50bac24e7ec325dbb09c6b6c4dcc88a7d79e8f
