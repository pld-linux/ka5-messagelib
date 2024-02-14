#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.01.95
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		messagelib
Summary:	Message library
Name:		ka5-%{kaname}
Version:	24.01.95
Release:	0.1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/unstable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	d727167ccd959b92ca896043649b24c5
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6Positioning-devel >= 5.11.1
BuildRequires:	Qt6PrintSupport-devel
BuildRequires:	Qt6Qml-devel >= 5.11.1
BuildRequires:	Qt6Quick-devel >= 5.11.1
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6WebChannel-devel >= 5.11.1
BuildRequires:	Qt6WebEngine-devel >= 5.11.1
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	gpgme-qt6-devel >= 1.8.0
BuildRequires:	grantlee-qt6-devel >= 5.1
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
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-karchive-devel >= %{kframever}
BuildRequires:	kf6-kcodecs-devel >= %{kframever}
BuildRequires:	kf6-kcompletion-devel >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf6-kcontacts-devel >= %{kframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kiconthemes-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-kitemviews-devel >= %{kframever}
BuildRequires:	kf6-kjobwidgets-devel >= %{kframever}
BuildRequires:	kf6-kservice-devel >= %{kframever}
BuildRequires:	kf6-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf6-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	kf6-sonnet-devel >= %{kframever}
BuildRequires:	kf6-syntax-highlighting-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qca-qt6-devel
BuildRequires:	qt6-build >= %{qtver}
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
%attr(755,root,root) %{_libdir}/libKPim6MessageComposer.so.*.*
%ghost %{_libdir}/libKPim6MessageComposer.so.6
%attr(755,root,root) %{_libdir}/libKPim6MessageCore.so.*.*
%ghost %{_libdir}/libKPim6MessageCore.so.6
%attr(755,root,root) %{_libdir}/libKPim6MessageList.so.*.*
%ghost %{_libdir}/libKPim6MessageList.so.6
%attr(755,root,root) %{_libdir}/libKPim6MessageViewer.so.*.*
%ghost %{_libdir}/libKPim6MessageViewer.so.6
%attr(755,root,root) %{_libdir}/libKPim6MimeTreeParser.so.*.*
%ghost %{_libdir}/libKPim6MimeTreeParser.so.6
%attr(755,root,root) %{_libdir}/libKPim6TemplateParser.so.*.*
%ghost %{_libdir}/libKPim6TemplateParser.so.6
%attr(755,root,root) %{_libdir}/libKPim6WebEngineViewer.so.*.*
%ghost %{_libdir}/libKPim6WebEngineViewer.so.6
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/headerstyle/messageviewer_defaultgrantleeheaderstyleplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/kf6/ktexttemplate/messageviewer_ktexttemplate_extension.so
%{_datadir}/config.kcfg/customtemplates_kfg.kcfg
%{_datadir}/config.kcfg/templatesconfiguration_kfg.kcfg
%{_datadir}/knotifications6/messageviewer.notifyrc
%{_datadir}/knsrcfiles/messageviewer_header_themes.knsrc
%{_datadir}/libmessageviewer
%{_datadir}/messagelist
%{_datadir}/messageviewer
%{_datadir}/org.kde.syntax-highlighting/syntax/kmail-template.xml
%{_datadir}/qlogging-categories6/messagelib.categories
%{_datadir}/qlogging-categories6/messagelib.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KPim6/MessageComposer
%{_includedir}/KPim6/MessageCore
%{_includedir}/KPim6/MessageList
%{_includedir}/KPim6/MessageViewer
%{_includedir}/KPim6/MimeTreeParser
%{_includedir}/KPim6/TemplateParser
%{_includedir}/KPim6/WebEngineViewer
%{_libdir}/cmake/KPim6MessageComposer
%{_libdir}/cmake/KPim6MessageCore
%{_libdir}/cmake/KPim6MessageList
%{_libdir}/cmake/KPim6MessageViewer
%{_libdir}/cmake/KPim6MimeTreeParser
%{_libdir}/cmake/KPim6TemplateParser
%{_libdir}/cmake/KPim6WebEngineViewer
%{_libdir}/libKPim6MessageComposer.so
%{_libdir}/libKPim6MessageCore.so
%{_libdir}/libKPim6MessageList.so
%{_libdir}/libKPim6MessageViewer.so
%{_libdir}/libKPim6MimeTreeParser.so
%{_libdir}/libKPim6TemplateParser.so
%{_libdir}/libKPim6WebEngineViewer.so
