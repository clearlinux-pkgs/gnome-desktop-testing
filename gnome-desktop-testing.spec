#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-desktop-testing
Version  : 2021.1
Release  : 5
URL      : https://download.gnome.org/sources/gnome-desktop-testing/2021/gnome-desktop-testing-2021.1.tar.xz
Source0  : https://download.gnome.org/sources/gnome-desktop-testing/2021/gnome-desktop-testing-2021.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0
Requires: gnome-desktop-testing-bin = %{version}-%{release}
Requires: gnome-desktop-testing-license = %{version}-%{release}
Requires: gnome-desktop-testing-man = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(libsystemd)

%description
No detailed description available

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


%package man
Summary: man components for the gnome-desktop-testing package.
Group: Default

%description man
man components for the gnome-desktop-testing package.


%prep
%setup -q -n gnome-desktop-testing-2021.1
cd %{_builddir}/gnome-desktop-testing-2021.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1625031253
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1625031253
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-desktop-testing
cp %{_builddir}/gnome-desktop-testing-2021.1/COPYING %{buildroot}/usr/share/package-licenses/gnome-desktop-testing/bf50bac24e7ec325dbb09c6b6c4dcc88a7d79e8f
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

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ginsttest-runner.1
/usr/share/man/man1/gnome-desktop-testing-runner.1
