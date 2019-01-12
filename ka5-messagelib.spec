%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		messagelib
Summary:	Message library
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	248fb637f967d709dc0c467664c7ce37
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Positioning-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5WebChannel-devel >= 5.11.1
BuildRequires:	Qt5WebEngine-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	gpgme-qt5-devel >= 1.8.0
BuildRequires:	grantlee-qt5-devel >= 5.1
BuildRequires:	ka5-akonadi-contacts-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-mime-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-search-devel >= %{kdeappsver}
BuildRequires:	ka5-grantleetheme-devel >= %{kdeappsver}
BuildRequires:	ka5-kcontacts-devel >= %{kdeappsver}
BuildRequires:	ka5-kdepim-apps-libs-devel >= %{kdeappsver}
BuildRequires:	ka5-kidentitymanagement-devel >= %{kdeappsver}
BuildRequires:	ka5-kldap-devel >= %{kdeappsver}
BuildRequires:	ka5-kmailtransport-devel >= %{kdeappsver}
BuildRequires:	ka5-kmbox-devel >= %{kdeappsver}
BuildRequires:	ka5-kmime-devel >= %{kdeappsver}
BuildRequires:	ka5-kpimtextedit-devel >= %{kdeappsver}
BuildRequires:	ka5-libgravatar-devel >= %{kdeappsver}
BuildRequires:	ka5-libkdepim-devel >= %{kdeappsver}
BuildRequires:	ka5-libkleo-devel >= %{kdeappsver}
BuildRequires:	ka5-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 5.51.0
BuildRequires:	kf5-karchive-devel >= 5.51.0
BuildRequires:	kf5-kcodecs-devel >= 5.51.0
BuildRequires:	kf5-kcompletion-devel >= 5.51.0
BuildRequires:	kf5-kconfig-devel >= 5.51.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.51.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.51.0
BuildRequires:	kf5-ki18n-devel >= 5.51.0
BuildRequires:	kf5-kiconthemes-devel >= 5.51.0
BuildRequires:	kf5-kio-devel >= 5.51.0
BuildRequires:	kf5-kitemviews-devel >= 5.51.0
BuildRequires:	kf5-kjobwidgets-devel >= 5.51.0
BuildRequires:	kf5-kservice-devel >= 5.51.0
BuildRequires:	kf5-ktextwidgets-devel >= 5.51.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.51.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.51.0
BuildRequires:	kf5-kxmlgui-devel >= 5.51.0
BuildRequires:	kf5-sonnet-devel >= 5.51.0
BuildRequires:	kf5-syntax-highlighting-devel >= 5.51.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library which provides support for mail apps.

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
/etc/xdg/messagelib.categories
/etc/xdg/messagelib.renamecategories
/etc/xdg/messageviewer_header_themes.knsrc
%attr(755,root,root) %ghost %{_libdir}/libKF5MessageComposer.so.5
%attr(755,root,root) %{_libdir}/libKF5MessageComposer.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5MessageCore.so.5
%attr(755,root,root) %{_libdir}/libKF5MessageCore.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5MessageList.so.5
%attr(755,root,root) %{_libdir}/libKF5MessageList.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5MessageViewer.so.5
%attr(755,root,root) %{_libdir}/libKF5MessageViewer.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5MimeTreeParser.so.5
%attr(755,root,root) %{_libdir}/libKF5MimeTreeParser.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5TemplateParser.so.5
%attr(755,root,root) %{_libdir}/libKF5TemplateParser.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5WebEngineViewer.so.5
%attr(755,root,root) %{_libdir}/libKF5WebEngineViewer.so.5.*.*
%dir %{_libdir}/qt5/plugins/messageviewer
%dir %{_libdir}/qt5/plugins/messageviewer/grantlee
%dir %{_libdir}/qt5/plugins/messageviewer/grantlee/5.0
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/grantlee/5.0/messageviewer_grantlee_extension.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/messageviewer_defaultgrantleeheaderstyleplugin.so
%{_datadir}/config.kcfg/customtemplates_kfg.kcfg
%{_datadir}/config.kcfg/templatesconfiguration_kfg.kcfg
%{_datadir}/kconf_update/messageviewer.upd
%{_datadir}/knotifications5/messageviewer.notifyrc
%{_datadir}/libmessageviewer
%{_datadir}/messagelist
%{_datadir}/messageviewer
# TODO proper package
%dir %{_datadir}/org.kde.syntax-highlighting
%dir %{_datadir}/org.kde.syntax-highlighting/syntax
%{_datadir}/org.kde.syntax-highlighting/syntax/kmail-template.xml

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/MessageComposer
%{_includedir}/KF5/MessageCore
%{_includedir}/KF5/MessageList
%{_includedir}/KF5/MessageViewer
%{_includedir}/KF5/MimeTreeParser
%{_includedir}/KF5/TemplateParser
%{_includedir}/KF5/WebEngineViewer
%{_includedir}/KF5/messagecomposer
%{_includedir}/KF5/messagecomposer_version.h
%{_includedir}/KF5/messagecore
%{_includedir}/KF5/messagecore_version.h
%{_includedir}/KF5/messagelist
%{_includedir}/KF5/messagelist_version.h
%{_includedir}/KF5/messageviewer
%{_includedir}/KF5/messageviewer_version.h
%{_includedir}/KF5/mimetreeparser
%{_includedir}/KF5/mimetreeparser_version.h
%{_includedir}/KF5/templateparser
%{_includedir}/KF5/templateparser_version.h
%{_includedir}/KF5/webengineviewer
%{_includedir}/KF5/webengineviewer_version.h
%{_libdir}/cmake/KF5MessageComposer
%{_libdir}/cmake/KF5MessageCore
%{_libdir}/cmake/KF5MessageList
%{_libdir}/cmake/KF5MessageViewer
%{_libdir}/cmake/KF5MimeTreeParser
%{_libdir}/cmake/KF5TemplateParser
%{_libdir}/cmake/KF5WebEngineViewer
%attr(755,root,root) %{_libdir}/libKF5MessageComposer.so
%attr(755,root,root) %{_libdir}/libKF5MessageCore.so
%attr(755,root,root) %{_libdir}/libKF5MessageList.so
%attr(755,root,root) %{_libdir}/libKF5MessageViewer.so
%attr(755,root,root) %{_libdir}/libKF5MimeTreeParser.so
%attr(755,root,root) %{_libdir}/libKF5TemplateParser.so
%attr(755,root,root) %{_libdir}/libKF5WebEngineViewer.so
%{_libdir}/qt5/mkspecs/modules/qt_MessageComposer.pri
%{_libdir}/qt5/mkspecs/modules/qt_MessageCore.pri
%{_libdir}/qt5/mkspecs/modules/qt_MessageList.pri
%{_libdir}/qt5/mkspecs/modules/qt_MessageViewer.pri
%{_libdir}/qt5/mkspecs/modules/qt_MimeTreeParser.pri
%{_libdir}/qt5/mkspecs/modules/qt_TemplateParser.pri
%{_libdir}/qt5/mkspecs/modules/qt_WebEngineViewer.pri
