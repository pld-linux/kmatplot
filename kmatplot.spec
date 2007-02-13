Summary:	KMatplot is a gnuplot-like tool for plotting data sets
Summary(pl.UTF-8):	KMatplot to podobne do gnuplota narzędzie do rysowania wykresów
Name:		kmatplot
Version:	0.4
Release:	1
License:	GPL
Vendor:		kamil <kamildobk@poczta.onet.pl>
Group:		X11/Applications/Science
Source0:	http://kmatplot.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	d5cd9bdddb2d3fc7ed359f409d61c7a7
Patch0:		%{name}-plugin.patch
URL:		http://kmatplot.sourceforge.net/
BuildRequires:	octave-devel
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMatplot is a gnuplot-like tool for plotting data sets in either two
or three dimensions. It can plot many ordinary types of 2d plots,
including pixmaps and contours, and 3d surfaces. It offers a full
WYSIWYG mode with multiple objects on a single page. See the
screenshot section for more details.

As opposite to Gnuplot, KMatplot has no scripting language but it is
more clickable, so easier to use for unexperienced users. It can be
used instead of Gnuplot with Octave and Scilab - there are new dll
functions installed in those packages, which communicate with KMatplot
through an Unix socket. Those functions are named 'kplot', 'kimage',
kmesh',... and are similar to those found in Octave by default.

%description -l pl.UTF-8
KMatplot to podobne do gnuplota narzędzie do rysowania wykresów
zarówno w dwóch jak i trzech wymiarach. Może rysować zwykłe rodzaje
wykresów 2D, w tym bitmapy i kontury, oraz powierzchnie 3D. Oferuje
pełny tryb WYSIWYG z wieloma obiektami lub pojedynczą stroną.

W przeciwieństwie do Gnuplota, KMatplot nie ma języka skryptowego, ale
jest bardziej klikalny, więc łatwiejszy w użyciu dla niedoświadczonych
użytkowników. Może być używany zamiast Gnuplota z Octave lub Scilabem
- do tych pakietów są instalowane nowe funkcje biblioteczne, które
komunikują się z KMatplotem przez gniazdko lokalne. Te funkcje
nazywają się "kplot", "kimage", "kmesh"... i są podobne do tych, które
standardowo znajdują się w Octave.

%prep
%setup -q
%patch0 -p1

%build
QTDIR="%{_prefix}"; export QTDIR
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

# XXX: fix location, add Categories if needed
mv -f $RPM_BUILD_ROOT%{_applnkdir}/{Applications,Scientific}

%find_lang %{name} --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/apps/kmatplot
%{_datadir}/mimelnk/application/x-kmatplot.desktop
%{_desktopdir}/kmatplot.desktop
%{_iconsdir}/*/*/apps/*
