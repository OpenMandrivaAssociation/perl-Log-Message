%define	upstream_name	 Log-Message
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.08
Release:	1

Summary:	Log Message
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Log/Log-Message-0.08.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(IPC::Cmd)                  >= 0.360.0
BuildRequires:  perl(Module::Load::Conditional) >= 0.40.0
BuildRequires:	perl-version
BuildArch:	noarch

%description
Log::Message is a generic message storage mechanism.  It allows you to store
messages on a stack -- either shared or private -- and assign meta-data to it.
Some meta-data will automatically be added for you, like a timestamp and a
stack trace, but some can be filled in by the user, like a tag by which to
identify it or group it, and a level at which to handle the message (for
example, log it, or die with it)

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Log
%{_mandir}/*/*


%changelog
* Sat Jan 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 630623
- update to new version 0.04

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 408962
- rebuild using %%perl_convert_version

* Tue Dec 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdv2009.1
+ Revision: 314757
- update to new version 0.02

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.01-3mdv2009.0
+ Revision: 140691
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jun 25 2007 Buchan Milne <bgmilne@mandriva.org> 0.01-3mdv2008.0
+ Revision: 44117
- Rebuild to fix file corruption caused by spec-helper

* Fri Jun 22 2007 Buchan Milne <bgmilne@mandriva.org> 0.01-2mdv2008.0
+ Revision: 42940
- Fix permissions

* Fri Jun 22 2007 Buchan Milne <bgmilne@mandriva.org> 0.01-1mdv2008.0
+ Revision: 42852
- Import perl-Log-Message



* Thu Jun 21 2007 Buchan Milne <bgmilne@mandriva.org> 0.01-1mdv2007.1
- initial package

