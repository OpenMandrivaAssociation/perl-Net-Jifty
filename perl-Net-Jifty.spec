%define upstream_name    Net-Jifty
Name:		perl-%{upstream_name}
Version:	0.14
Release:	6

Summary:	Interface to online Jifty applications
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Net-Jifty
Source0:	https://cpan.metacpan.org/authors/id/S/SA/SARTAK/Net-Jifty-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Any::Moose)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(Email::Address)
BuildRequires:	perl(Encode) >= 2.410.0
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Hash::Merge)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Term::ReadKey)
BuildRequires:	perl(Test::MockObject)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI)
BuildRequires:	perl(YAML)
BuildArch:	noarch

%description
the Jifty manpage is a full-stack web framework. It provides an optional
REST interface for applications. Using this module, you can interact with
that REST interface to write client-side utilities.

You can use this module directly, but you'll be better off subclassing it,
such as what we've done for the Net::Hiveminder manpage.

This module also provides a number of convenient methods for writing short
scripts. For example, passing 'use_config => 1' to 'new' will look at the
config file for the username and password (or SID) of the user. If neither
is available, it will prompt the user for them.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/Net/

%changelog
* Thu Jan 06 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.140.0-1mdv2011.0
+ Revision: 629073
- new version

* Fri Apr 30 2010 Michael Scherer <misc@mandriva.org> 0.120.0-1mdv2011.0
+ Revision: 541129
- import perl-Net-Jifty


* Fri Apr 30 2010 cpan2dist 0.12-1mdv
- initial mdv release, generated with cpan2dist
