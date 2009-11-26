Summary:	Performance analysis tool
Name:		nmon
Version:	12f
Release:	1
License:	GPL
Group:		Applications/System
URL:		http://nmon.sourceforge.net/pmwiki.php
BuildRequires:	ncurses-devel
Source0:	http://dl.sourceforge.net/project/nmon/lmon%{version}.c
# Source0-md5:	36da7485cc16dccbd6f840359c76ad83
Source1:	http://dl.sourceforge.net/project/nmon/Documentation.txt
# Source1-md5:	dbb13658cf55d687c4f2ff771a696d4a
ExclusiveArch:	%{ix86} %{x8664} ppc ppc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nmon is designed for performance specialists to use for monitoring and
analyzing performance data.

%prep
%setup -qcT
install %{SOURCE0} nmon.c
install %{SOURCE1} .

cat <<'EOF' > Makefile
LIBS := -lncurses
OPTFLAGS := -O2
CFLAGS := -Wall -I/usr/include/ncurses -D JFS -D GETUSER -D LARGEMEM $(OPTFLAGS)

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
