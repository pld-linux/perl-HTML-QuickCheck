%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	QuickCheck
Summary:	HTML::QuickCheck - a simple and fast HTML syntax checking package for perl
Summary(pl):	HTML::QuickCheck - prosty i szybki pakiet do sprawdzania sk³adni HTML-a
Name:		perl-HTML-QuickCheck
Version:	1.0b1
Release:	9
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	55428ba8fefb469ddc7cdf0240172cb1
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
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

%description -l pl
Ide± pakietu HTML::QuickCheck jest udostêpnienie szybkiego,
podstawowego interfejsu do sprawdzania poprawno¶ci HTML-a (w
szczególno¶ci, czas odpowiedzi jest istotny dla skryptów CGI), aby
zapobiec zamieszaniu w pliku, jakie mo¿e wprowadziæ fragment danych
wej¶ciowych w HTML-u. Tzn., ma na celuminimalizacjê i lokalizacjê
mo¿liwych uszkodzeñ dynamicznego dokumentu HTML poprzez wprowadzenie
przez u¿ytkownika swoich danych jako HTML-u.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

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
