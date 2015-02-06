%define upstream_name    Net-Jifty
%define upstream_version 0.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Interface to online Jifty applications
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

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
