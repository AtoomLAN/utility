Summary: utility
Name: utility 
Version: 1.0.0
Release: 42 
License: Jeroen Habraken
Group: EOS/Extension
Source0: utility.tar
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: Eos-release >= 2:4.9.0
%description 
Arista utility extension
%prep
%setup -q -n utility 
%build
%install
mkdir -p $RPM_BUILD_ROOT/usr/lib/python2.7/site-packages/CliPlugin
mkdir -p $RPM_BUILD_ROOT/usr/lib/python2.7/site-packages/CliPlugin/Utility
cp -R Utility.py $RPM_BUILD_ROOT/usr/lib/python2.7/site-packages/CliPlugin/
cp -R Utility/* $RPM_BUILD_ROOT/usr/lib/python2.7/site-packages/CliPlugin/Utility
%files
%defattr(755,root,root,-)
/usr/lib/python2.7/site-packages/CliPlugin/Utility.py
/usr/lib/python2.7/site-packages/CliPlugin/Utility/Acl.py
/usr/lib/python2.7/site-packages/CliPlugin/Utility/Firewall.py
/usr/lib/python2.7/site-packages/CliPlugin/Utility/Private.py
