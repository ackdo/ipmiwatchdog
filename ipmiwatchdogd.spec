Name            : ipmiwatchdogd
Version         : 1.0
Release		: 0
Group           : System Environment/Base

Summary         : The configuration file for ipmiwatchdogd daemon 

License         : GPL
Vendor		: Sam.Lee@emerson.com

Buildroot       : %{_tmppath}/%{name}-%{version}
Source          : %{name}-%{version}.tar.gz

%description
This daemon can be used to control the IPMC watchdog without the /dev/watchdog device; just IPMI driver(ipmi_msghandler, ipmi_si and ipmi_devintf) and BMC hardware required. The daemon based on raw ipmi command, get device id, set watchdog command, reset watchdog command and get watchdog command. Wrote by Sam Lee  at Mar 2013; if you have any question/comments please contact Sam Lee at Sam.Lee@emerson.com 

%prep

%setup -q

%build
./configure --prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

install -D -m 755 /tmp/ipmiwatchdogd-1.0/S99zIPMIWATCHDOGD $RPM_BUILD_ROOT%{_sysconfdir}/init.d/S99zIPMIWATCHDOGD
install -D -m 644 /tmp/ipmiwatchdogd-1.0/ipmiwatchdog.conf $RPM_BUILD_ROOT%{_sysconfdir}/ipmiwatchdog.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%{_prefix}/sbin/ipmiwatchdogd

%config(noreplace) %{_sysconfdir}/ipmiwatchdog.conf
%config(noreplace) %{_sysconfdir}/init.d/S99zIPMIWATCHDOGD

%changelog
* Mon Mar 18 2013 Sam Lee <Sam.Lee@emerson.com>
- This is the initail release version 1.0
