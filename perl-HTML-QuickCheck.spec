%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	QuickCheck
Summary:	HTML::QuickCheck perl module
Summary(pl):	Modu³ perla HTML::QuickCheck
Name:		perl-HTML-QuickCheck
Version:	1.0b1
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::QuickCheck - fast simple validation of HMTL text.

%description -l pl
HTML::QuickCheck - proste i szybkie sprawdzanie poprawno¶ci dokumentów
HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/HTML/QuickCheck.pm
%{_mandir}/man3/*
