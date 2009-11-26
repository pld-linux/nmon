# $Id: nmon.spec,v 1.1 2009-11-26 17:34:53 blekot Exp $
# Authority: dag
# Upstream: Nigel Griffiths <nag$uk,ibm,com>

Summary:	Performance analysis tool
Name:		nmon
Version:	12f
Release:	0.1
License:	GPL
Group:		Applications/System
URL:		http://nmon.sourceforge.net/pmwiki.php
Source0:	http://sourceforge.net/projects/nmon/files/lmon12f.c/download
# Source0-md5:
Source1:	http://sourceforge.net/projects/nmon/files/makefile/download
# Source1-md5:
Source2:	http://sourceforge.net/projects/nmon/files/Documentation.txt/download
# Source2-md5:
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

ExclusiveArch:	%{ix86} %{x8664} ppc ppc64

%description
nmon is designed for performance specialists to use for monitoring and
analyzing performance data.

%prep
%setup -q -c -a1 -a2

%build

%install
rm -rf $RPM_BUILD_ROOT
%ifarch i386
%{?fc5:%{__install} -Dp -m0755 nmon_x86_fedora5 $RPM_BUILD_ROOT%{_bindir}/nmon}
%{?el4:%{__install} -Dp -m0755 nmon_x86_rhel4 $RPM_BUILD_ROOT%{_bindir}/nmon}
%{?el3:%{__install} -Dp -m0755 nmon_x86_rhel3 $RPM_BUILD_ROOT%{_bindir}/nmon}
%{?el2:%{__install} -Dp -m0755 nmon_x86_rhel2 $RPM_BUILD_ROOT%{_bindir}/nmon}
%{?rh9:%{__install} -Dp -m0755 nmon_x86_redhat9 $RPM_BUILD_ROOT%{_bindir}/nmon}
%endif
%ifarch x86_64
%{?fc6:%{__install} -Dp -m0755 nmon_x86_64_fedora6 $RPM_BUILD_ROOT%{_bindir}/nmon}
%{?el4:%{__install} -Dp -m0755 nmon_x86_64_rhel4u4 $RPM_BUILD_ROOT%{_bindir}/nmon}
%endif
%ifarch ppc ppc64
%{?el4:%{__install} -Dp -m0755 nmon_power_rhel4 $RPM_BUILD_ROOT%{_bindir}/nmon}
%{?el3:%{__install} -Dp -m0755 nmon_power_rhel3 $RPM_BUILD_ROOT%{_bindir}/nmon}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nmon
