%define	upstream_name	 Log-Message
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.08
Release:	6

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
