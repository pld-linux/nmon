Summary:	Performance analysis tool
Summary(pl.UTF-8):	Narzędzie do analizowania wydajności
Name:		nmon
Version:	14g
Release:	3
License:	GPL
Group:		Applications/System
URL:		http://nmon.sourceforge.net/pmwiki.php
BuildRequires:	ncurses-devel
Source0:	http://dl.sourceforge.net/project/nmon/lmon%{version}.c
# Source0-md5:	e537f51446fb375140368b115dc8278b
Source1:	http://dl.sourceforge.net/project/nmon/Documentation.txt
# Source1-md5:	dbb13658cf55d687c4f2ff771a696d4a
ExclusiveArch:	%{ix86} %{x8664} ppc ppc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nmon is designed for performance specialists to use for monitoring and
analyzing performance data.
Collected data can be analyzed by nmonanalyser tool:
http://www.ibm.com/developerworks/wikis/display/WikiPtype/nmonanalyser

%description -l pl.UTF-8
nmon to zbudowany dla specjalistów od wydajnosci aby używać go do
monitorowania i analizoawnia wydajnościowych danych.
Zebrane dane można analizować za pomocą narzędzia nmonanalyser:
http://www.ibm.com/developerworks/wikis/display/WikiPtype/nmonanalyser

%prep
%setup -qcT
install %{SOURCE0} nmon.c
install %{SOURCE1} .

cat <<'EOF' > Makefile
LIBS := -lncurses -ltinfo
OPTFLAGS := -O2
CFLAGS := -Wall -I/usr/include/ncurses -D JFS -D GETUSER -D LARGEMEM -D KERNEL_2_6_18 $(OPTFLAGS)
LDFLAGS := -l/libtinfo.so.5

nmon: nmon.o
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $^ $(LIBS)
EOF

%build
%{__make} nmon \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -p -D nmon $RPM_BUILD_ROOT%{_bindir}/nmon

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Documentation.txt
%attr(755,root,root) %{_bindir}/nmon
