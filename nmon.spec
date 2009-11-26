# $Id: nmon.spec,v 1.5 2009-11-26 18:20:54 blekot Exp $
# Authority: dag
# Upstream: Nigel Griffiths <nag$uk,ibm,com>

Summary:	Performance analysis tool
Name:		nmon
Version:	12f
Release:	0.1
License:	GPL
Group:		Applications/System
URL:		http://nmon.sourceforge.net/pmwiki.php
BuildRequires:	ncurses-devel
Source0:	http://downloads.sourceforge.net/project/nmon/lmon12f.c
# Source0-md5:	36da7485cc16dccbd6f840359c76ad83
Source1:	http://downloads.sourceforge.net/project/nmon/Documentation.txt
# Source1-md5:	dbb13658cf55d687c4f2ff771a696d4a
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

ExclusiveArch:	%{ix86} %{x8664} ppc ppc64

%description
nmon is designed for performance specialists to use for monitoring and
analyzing performance data.

%prep
%setup -q -T -c
cp -f %{SOURCE0} .
cp -f %{SOURCE1} .

%build
#%{__cc} %{rpmcflags} %{rpmldflags} -I/usr/include -I/usr/include/ncurses -o nmon lmon*.c -D JFS -D GETUSER -D LARGEMEM
%{__cc} -g -O2 -D JFS -D GETUSER -Wall -D LARGEMEM -I/usr/include/ncurses -lncurses -g -o nmon lmon*.c

%install
rm -rf $RPM_BUILD_ROOT
install -D nmon $RPM_BUILD_ROOT%{_bindir}/nmon

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Documentation.txt
%attr(755,root,root) %{_bindir}/nmon
