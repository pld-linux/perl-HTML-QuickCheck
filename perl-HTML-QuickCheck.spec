%include	/usr/lib/rpm/macros.perl
Summary:	HTML-QuickCheck perl module
Summary(pl):	Modu³ perla HTML-QuickCheck
Name:		perl-HTML-QuickCheck
Version:	1.0b1
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/HTML-QuickCheck-%{version}.tar.gz
Patch0:		perl-HTML-QuickCheck-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
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
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/HTML/QuickCheck
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/HTML/QuickCheck.pm
%{perl_sitearch}/auto/HTML/QuickCheck

%{_mandir}/man3/*
