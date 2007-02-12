%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	QuickCheck
Summary:	HTML::QuickCheck - a simple and fast HTML syntax checking package for perl
Summary(pl.UTF-8):   HTML::QuickCheck - prosty i szybki pakiet do sprawdzania składni HTML-a
Name:		perl-HTML-QuickCheck
Version:	1.0b1
Release:	10
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	55428ba8fefb469ddc7cdf0240172cb1
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::QuickCheck - fast simple validation of HMTL text.

The objective of the HTML::QuickCheck package is to provide a fast and
essential HTML check (esp. for CGI scripts where response time is
important) to prevent a piece of user input HTML code from messing up
the rest of a file, i.e., to minimize and localize any possible damage
created by including a piece of user input HTML text in a dynamic
document.

%description -l pl.UTF-8
Ideą pakietu HTML::QuickCheck jest udostępnienie szybkiego,
podstawowego interfejsu do sprawdzania poprawności HTML-a (w
szczególności, czas odpowiedzi jest istotny dla skryptów CGI), aby
zapobiec zamieszaniu w pliku, jakie może wprowadzić fragment danych
wejściowych w HTML-u. Tzn., ma na celu minimalizację i lokalizację
możliwych uszkodzeń dynamicznego dokumentu HTML poprzez wprowadzenie
przez użytkownika swoich danych jako HTML-u.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/HTML/QuickCheck.pm
%{_mandir}/man3/*
