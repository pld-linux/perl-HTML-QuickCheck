%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	QuickCheck
Summary:	HTML::QuickCheck perl module
Summary(pl):	Modu� perla HTML::QuickCheck
Name:		perl-HTML-QuickCheck
Version:	1.0b1
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::QuickCheck - fast simple validation of HMTL text.

%description -l pl
HTML::QuickCheck - proste i szybkie sprawdzanie poprawno�ci dokument�w
HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
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
