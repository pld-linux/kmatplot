Summary:	KMatplot is a gnuplot-like tool for plotting data sets
Summary(pl):	KMatplot to podobne do gnuplota narzêdzie do rysowania wykresów
Name:		kmatplot
Version:	0.3
Release:	1
License:	GPL
Vendor:		kamil <kamildobk@poczta.onet.pl>
Group:		X11/Applications/Science
Source0:	http://kmatplot.sourceforge.net/%{name}-%{version}.tar.gz
URL:		http://kmatplot.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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

%description -l pl
KMatplot to podobne do gnuplota narzêdzie do rysowania wykresów
zarówno w dwóch jak i trzech wymiarach. Mo¿e rysowaæ zwyk³e rodzaje
wykresów 2D, w tym bitmapy i kontury, oraz powierzchnie 3D. Oferuje
pe³ny tryb WYSIWYG z wieloma obiektami lub pojedyncz± stron±.

W przeciwieñstwie do Gnuplota, KMatplot nie ma jêzyka skryptowego, ale
jest bardziej klikalny, wiêc ³atwiejszy w u¿yciu dla niedo¶wiadczonych
u¿ytkowników. Mo¿e byæ u¿ywany zamiast Gnuplota z Octave lub Scilabem
- do tych pakietów s± instalowane nowe funkcje biblioteczne, które
komunikuj± siê z KMatplotem przez gniazdko lokalne. Te funkcje
nazywaj± siê "kplot", "kimage", "kmesh"... i s± podobne do tych, które
standardowo znajduj± siê w Octave.

%prep
%setup -q

%build
%config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > $RPM_BUILD_DIR/file.list.kmatplot
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.kmatplot
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.kmatplot

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ../file.list.kmatplot
%defattr(644,root,root,755)
