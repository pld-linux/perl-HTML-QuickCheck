%include	/usr/lib/rpm/macros.perl
Summary:	HTML-QuickCheck perl module
Summary(pl):	Modu³ perla HTML-QuickCheck
Name:		perl-HTML-QuickCheck
Version:	1.0b1
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/HTML-QuickCheck-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML-QuickCheck - fast simple validation of HMTL text.

%description -l pl
HTML-QuickCheck - proste i szybkie sprawdzanie poprawno¶ci dokumentów
HTML.

%prep
%setup -q -n HTML-QuickCheck-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/HTML/QuickCheck.pm
%{_mandir}/man3/*
