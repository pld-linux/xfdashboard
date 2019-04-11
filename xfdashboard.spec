Summary:	Maybe a Gnome shell like dashboard for Xfce
Name:		xfdashboard
Version:	0.7.5
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://archive.xfce.org/src/apps/xfdashboard/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	e658770b2df0c9302bbc1248bf04c343
URL:		http://goodies.xfce.org/projects/applications/xfdashboard/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	clutter-devel >= 1.16.4
BuildRequires:	dbus-glib-devel >= 0.98
BuildRequires:	garcon-devel >= 0.4.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.30.2
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.30
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	xfce4-dev-tools >= 4.12.0
BuildRequires:	xfconf-devel >= 4.12.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfdashboard provides a GNOME shell dashboard like interface for use
with Xfce desktop. It can be configured to run to any keyboard
shortcut and when executed provides an overview of applications
currently open enabling the user to switch between different
applications. The search feature works like Xfce's app finder which
makes it convenient to search for and start applications.

%prep
%setup -q

%{__mv} po/it{_IT,}.po
sed -e 's/it_IT/it/' -i po/it.po configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/{,xfdashboard/plugins}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
/etc/xdg/autostart/xfdashboard-autostart.desktop
%attr(755,root,root) %{_bindir}/xfdashboard
%attr(755,root,root) %{_bindir}/xfdashboard-settings
%attr(755,root,root) %{_libdir}/libxfdashboard.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxfdashboard.so.0
%dir %{_libdir}/xfdashboard
%dir %{_libdir}/xfdashboard/plugins
%attr(755,root,root) %{_libdir}/xfdashboard/plugins/clock-view.so
%attr(755,root,root) %{_libdir}/xfdashboard/plugins/gnome-shell-search-provider.so
%attr(755,root,root) %{_libdir}/xfdashboard/plugins/hot-corner.so
%attr(755,root,root) %{_libdir}/xfdashboard/plugins/middle-click-window-close.so
%dir %{_datadir}/xfdashboard
%{_datadir}/xfdashboard/bindings.xml
%{_datadir}/xfdashboard/preferences.ui
%{_desktopdir}/xfdashboard.desktop
%{_desktopdir}/xfdashboard-settings.desktop
%{_iconsdir}/hicolor/*/apps/xfdashboard*
%{_datadir}/appdata/xfdashboard.appdata.xml
%{_datadir}/themes/xfdashboard
%{_datadir}/themes/xfdashboard-auber
%{_datadir}/themes/xfdashboard-blue
%{_datadir}/themes/xfdashboard-dark
%{_datadir}/themes/xfdashboard-mint
%{_datadir}/themes/xfdashboard-moranga
%{_datadir}/themes/xfdashboard-wine

#%attr(755,root,root) %{_libdir}/libxfdashboard.so
#%{_includedir}/xfdashboard
#%{_pkgconfigdir}/libxfdashboard.pc
