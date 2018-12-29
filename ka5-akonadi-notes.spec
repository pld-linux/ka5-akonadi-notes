%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		akonadi-notes
Summary:	Akonadi Notes
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	28a6bf8971e51ee9f77d97fd081d9e8a
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Test-devel >= 5.9.0
BuildRequires:	Qt5Xml-devel >= 5.9.0
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-akonadi-devel >= 5.10.0
BuildRequires:	ka5-kmime-devel >= 5.10.0
BuildRequires:	kf5-extra-cmake-modules >= 5.51.0
BuildRequires:	kf5-ki18n-devel >= 5.51.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for akonadi notes integration.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libKF5AkonadiNotes.so.5
%attr(755,root,root) %{_libdir}/libKF5AkonadiNotes.so.5.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/Akonadi/Notes
%{_includedir}/KF5/akonadi-notes_version.h
%{_includedir}/KF5/akonadi/notes
%{_libdir}/cmake/KF5AkonadiNotes
%attr(755,root,root) %{_libdir}/libKF5AkonadiNotes.so
%{_libdir}/qt5/mkspecs/modules/qt_AkonadiNotes.pri
