#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.5
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		messagelib
Summary:	Message library
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	000adc1cf1bce4e7466a2a318514801f
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
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	gpgme-qt5-devel >= 1.8.0
BuildRequires:	grantlee-qt5-devel >= 5.1
BuildRequires:	ka5-akonadi-contacts-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-mime-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-search-devel >= %{kdeappsver}
BuildRequires:	ka5-grantleetheme-devel >= %{kdeappsver}
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
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-karchive-devel >= %{kframever}
BuildRequires:	kf5-kcodecs-devel >= %{kframever}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcontacts-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kitemviews-devel >= %{kframever}
BuildRequires:	kf5-kjobwidgets-devel >= %{kframever}
BuildRequires:	kf5-kservice-devel >= %{kframever}
BuildRequires:	kf5-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	kf5-sonnet-devel >= %{kframever}
BuildRequires:	kf5-syntax-highlighting-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qca-qt5-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
ExcludeArch:	x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library which provides support for mail apps.

%description -l pl.UTF-8
Biblioteka, która wspiera aplikacje pocztowe.

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
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%{_datadir}/config.kcfg/customtemplates_kfg.kcfg
%{_datadir}/config.kcfg/templatesconfiguration_kfg.kcfg
%{_datadir}/knotifications5/messageviewer.notifyrc
%{_datadir}/libmessageviewer
%{_datadir}/messagelist
%{_datadir}/messageviewer
%{_datadir}/knsrcfiles/messageviewer_header_themes.knsrc
%{_datadir}/qlogging-categories5/messagelib.categories
%{_datadir}/qlogging-categories5/messagelib.renamecategories
# TODO proper package
%dir %{_datadir}/org.kde.syntax-highlighting
%dir %{_datadir}/org.kde.syntax-highlighting/syntax
%{_datadir}/org.kde.syntax-highlighting/syntax/kmail-template.xml
%dir %{_libdir}/qt5/plugins/pim5/messageviewer
%dir %{_libdir}/qt5/plugins/pim5/messageviewer/grantlee
%dir %{_libdir}/qt5/plugins/pim5/messageviewer/grantlee/5.0
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/messageviewer/grantlee/5.0/messageviewer_grantlee_extension.so
%dir %{_libdir}/qt5/plugins/pim5/messageviewer/headerstyle
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/messageviewer/headerstyle/messageviewer_defaultgrantleeheaderstyleplugin.so

%ghost %{_libdir}/libKPim5MessageComposer.so.5
%attr(755,root,root) %{_libdir}/libKPim5MessageComposer.so.*.*.*
%ghost %{_libdir}/libKPim5MessageCore.so.5
%attr(755,root,root) %{_libdir}/libKPim5MessageCore.so.*.*.*
%ghost %{_libdir}/libKPim5MessageList.so.5
%attr(755,root,root) %{_libdir}/libKPim5MessageList.so.*.*.*
%ghost %{_libdir}/libKPim5MessageViewer.so.5
%attr(755,root,root) %{_libdir}/libKPim5MessageViewer.so.*.*.*
%ghost %{_libdir}/libKPim5MimeTreeParser.so.5
%attr(755,root,root) %{_libdir}/libKPim5MimeTreeParser.so.*.*.*
%ghost %{_libdir}/libKPim5TemplateParser.so.5
%attr(755,root,root) %{_libdir}/libKPim5TemplateParser.so.*.*.*
%ghost %{_libdir}/libKPim5WebEngineViewer.so.5
%attr(755,root,root) %{_libdir}/libKPim5WebEngineViewer.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/qt5/mkspecs/modules/qt_MessageComposer.pri
%{_libdir}/qt5/mkspecs/modules/qt_MessageCore.pri
%{_libdir}/qt5/mkspecs/modules/qt_MessageList.pri
%{_libdir}/qt5/mkspecs/modules/qt_MessageViewer.pri
%{_libdir}/qt5/mkspecs/modules/qt_TemplateParser.pri
%{_libdir}/qt5/mkspecs/modules/qt_WebEngineViewer.pri
%{_includedir}/KPim5/MessageComposer
%{_includedir}/KPim5/MessageCore
%{_includedir}/KPim5/MessageList
%{_includedir}/KPim5/MessageViewer
%{_includedir}/KPim5/MimeTreeParser
%{_includedir}/KPim5/TemplateParser
%{_includedir}/KPim5/WebEngineViewer
%{_libdir}/cmake/KPim5MessageComposer
%{_libdir}/cmake/KPim5MessageCore
%{_libdir}/cmake/KPim5MessageList
%{_libdir}/cmake/KPim5MessageViewer
%{_libdir}/cmake/KPim5MimeTreeParser
%{_libdir}/cmake/KPim5TemplateParser
%{_libdir}/cmake/KPim5WebEngineViewer
%{_libdir}/libKPim5MessageComposer.so
%{_libdir}/libKPim5MessageCore.so
%{_libdir}/libKPim5MessageList.so
%{_libdir}/libKPim5MessageViewer.so
%{_libdir}/libKPim5MimeTreeParser.so
%{_libdir}/libKPim5TemplateParser.so
%{_libdir}/libKPim5WebEngineViewer.so
