#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : appstream
Version  : 0.16.0
Release  : 34
URL      : https://github.com/ximion/appstream/archive/v0.16.0/appstream-0.16.0.tar.gz
Source0  : https://github.com/ximion/appstream/archive/v0.16.0/appstream-0.16.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1 OFL-1.1
Requires: appstream-bin = %{version}-%{release}
Requires: appstream-data = %{version}-%{release}
Requires: appstream-lib = %{version}-%{release}
Requires: appstream-license = %{version}-%{release}
Requires: appstream-locales = %{version}-%{release}
Requires: appstream-man = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : curl-dev
BuildRequires : docbook-xml
BuildRequires : glibc-bin
BuildRequires : gperf
BuildRequires : gtk-doc-dev
BuildRequires : itstool
BuildRequires : lmdb-dev
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(xmlb)
BuildRequires : pkgconfig(yaml-0.1)
BuildRequires : qttools-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
AppStream
=========
<img align="right" src="docs/images/src/png/appstream-logo.png">

%package bin
Summary: bin components for the appstream package.
Group: Binaries
Requires: appstream-data = %{version}-%{release}
Requires: appstream-license = %{version}-%{release}

%description bin
bin components for the appstream package.


%package data
Summary: data components for the appstream package.
Group: Data

%description data
data components for the appstream package.


%package dev
Summary: dev components for the appstream package.
Group: Development
Requires: appstream-lib = %{version}-%{release}
Requires: appstream-bin = %{version}-%{release}
Requires: appstream-data = %{version}-%{release}
Requires: appstream-extras = %{version}-%{release}
Provides: appstream-devel = %{version}-%{release}
Requires: appstream = %{version}-%{release}

%description dev
dev components for the appstream package.


%package doc
Summary: doc components for the appstream package.
Group: Documentation
Requires: appstream-man = %{version}-%{release}

%description doc
doc components for the appstream package.


%package extras
Summary: extras components for the appstream package.
Group: Default

%description extras
extras components for the appstream package.


%package lib
Summary: lib components for the appstream package.
Group: Libraries
Requires: appstream-data = %{version}-%{release}
Requires: appstream-license = %{version}-%{release}

%description lib
lib components for the appstream package.


%package license
Summary: license components for the appstream package.
Group: Default

%description license
license components for the appstream package.


%package locales
Summary: locales components for the appstream package.
Group: Default

%description locales
locales components for the appstream package.


%package man
Summary: man components for the appstream package.
Group: Default

%description man
man components for the appstream package.


%package tests
Summary: tests components for the appstream package.
Group: Default
Requires: appstream = %{version}-%{release}

%description tests
tests components for the appstream package.


%prep
%setup -q -n appstream-0.16.0
cd %{_builddir}/appstream-0.16.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1674831824
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dstemming=false \
-Dapt-support=false \
-Dqt=true  builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
mkdir -p %{buildroot}/usr/share/package-licenses/appstream
cp %{_builddir}/appstream-%{version}/COPYING %{buildroot}/usr/share/package-licenses/appstream/7fab4cd4eb7f499d60fe183607f046484acd6e2d || :
cp %{_builddir}/appstream-%{version}/tests/samples/compose/Noto.LICENSE %{buildroot}/usr/share/package-licenses/appstream/d0f13df6b8f332b284e46d6bc228489e6115eda7 || :
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang appstream

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/appstreamcli

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/AppStream-1.0.typelib
/usr/share/gettext/its/metainfo.its
/usr/share/gettext/its/metainfo.loc
/usr/share/gir-1.0/*.gir
/usr/share/metainfo/org.freedesktop.appstream.cli.metainfo.xml

%files dev
%defattr(-,root,root,-)
/usr/include/AppStreamQt/appstreamqt_export.h
/usr/include/AppStreamQt/bundle.h
/usr/include/AppStreamQt/category.h
/usr/include/AppStreamQt/component.h
/usr/include/AppStreamQt/contentrating.h
/usr/include/AppStreamQt/icon.h
/usr/include/AppStreamQt/image.h
/usr/include/AppStreamQt/launchable.h
/usr/include/AppStreamQt/metadata.h
/usr/include/AppStreamQt/pool.h
/usr/include/AppStreamQt/provided.h
/usr/include/AppStreamQt/relation.h
/usr/include/AppStreamQt/release.h
/usr/include/AppStreamQt/screenshot.h
/usr/include/AppStreamQt/spdx.h
/usr/include/AppStreamQt/suggested.h
/usr/include/AppStreamQt/systeminfo.h
/usr/include/AppStreamQt/translation.h
/usr/include/AppStreamQt/utils.h
/usr/include/AppStreamQt/version.h
/usr/include/AppStreamQt/video.h
/usr/include/appstream/appstream.h
/usr/include/appstream/as-agreement-section.h
/usr/include/appstream/as-agreement.h
/usr/include/appstream/as-artifact.h
/usr/include/appstream/as-branding.h
/usr/include/appstream/as-bundle.h
/usr/include/appstream/as-category-gir.h
/usr/include/appstream/as-category.h
/usr/include/appstream/as-checksum.h
/usr/include/appstream/as-component.h
/usr/include/appstream/as-content-rating.h
/usr/include/appstream/as-context.h
/usr/include/appstream/as-distro-details.h
/usr/include/appstream/as-enum-types.h
/usr/include/appstream/as-enums.h
/usr/include/appstream/as-icon.h
/usr/include/appstream/as-image.h
/usr/include/appstream/as-issue.h
/usr/include/appstream/as-launchable.h
/usr/include/appstream/as-metadata.h
/usr/include/appstream/as-pool-gir.h
/usr/include/appstream/as-pool.h
/usr/include/appstream/as-provided.h
/usr/include/appstream/as-relation.h
/usr/include/appstream/as-release.h
/usr/include/appstream/as-review.h
/usr/include/appstream/as-screenshot.h
/usr/include/appstream/as-spdx.h
/usr/include/appstream/as-suggested.h
/usr/include/appstream/as-system-info.h
/usr/include/appstream/as-translation.h
/usr/include/appstream/as-utils.h
/usr/include/appstream/as-validator-issue.h
/usr/include/appstream/as-validator.h
/usr/include/appstream/as-vercmp.h
/usr/include/appstream/as-version.h
/usr/include/appstream/as-video.h
/usr/lib64/cmake/AppStreamQt/AppStreamQtConfig.cmake
/usr/lib64/cmake/AppStreamQt/AppStreamQtConfigVersion.cmake
/usr/lib64/libAppStreamQt.so
/usr/lib64/libappstream.so
/usr/lib64/pkgconfig/appstream.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/appstream/*
/usr/share/gtk-doc/html/appstream

%files extras
%defattr(-,root,root,-)
/usr/lib64/libAppStreamQt.so.2

%files lib
%defattr(-,root,root,-)
/usr/lib64/libAppStreamQt.so.0.16.0
/usr/lib64/libappstream.so.0.16.0
/usr/lib64/libappstream.so.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/appstream/7fab4cd4eb7f499d60fe183607f046484acd6e2d
/usr/share/package-licenses/appstream/d0f13df6b8f332b284e46d6bc228489e6115eda7

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/appstreamcli.1

%files tests
%defattr(-,root,root,-)
/usr/share/installed-tests/appstream/metainfo-validate.test

%files locales -f appstream.lang
%defattr(-,root,root,-)

