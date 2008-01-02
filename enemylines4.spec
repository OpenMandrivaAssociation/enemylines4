%define	name	enemylines4
%define	version 1.0
%define rel	3
%define	release	%mkrel %rel

Name:		%{name} 
Summary:	A simple futuristic racing game
Version:	%{version} 
Release:	%{release} 
Source0:	%{name}-%{version}.tar.bz2
Source10:	%{name}.png
URL:		http://raum1.memebot.com/enemylines/enemylines4.html
Group:		Games/Arcade
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
BuildRequires:	SDL_image1.2-devel SDL-devel libMesaglut-devel
BuildRequires:  ImageMagick

%description
A simple futuristic racing game. Urgent deliveries - Reach goal before
time runs out. Times aren't what they used to be though.
Road conditions are horrible and traffic safety and control systems
have been offline for months.

%prep
%setup -q

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/
cp ./data/* $RPM_BUILD_ROOT%{_datadir}/%{name}/
install -m755 %{name} -D $RPM_BUILD_ROOT%{_gamesbindir}/%{name}
mkdir -p %{buildroot}/%{_iconsdir}/ %{buildroot}/%{_miconsdir}/ $RPM_BUILD_ROOT%{_menudir}/
install -m644 %SOURCE10 -D %{buildroot}/%{_liconsdir}/%{name}.png
convert %{buildroot}/%{_liconsdir}/%{name}.png -resize 24x24 %{buildroot}/%{_iconsdir}/%{name}.png
convert %{buildroot}/%{_liconsdir}/%{name}.png -resize 16x16 %{buildroot}/%{_miconsdir}/%{name}.png
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="%{_gamesbindir}/%{name}" \
                  icon=%{name}.png \
                  needs="x11" \
                  section="More Applications/Games/Arcade" \
                  title="Enemy lines 4"\
                  longtitle="A simple futuristic racing game. Urgent deliveries!"
EOF

%post
%{update_menus}

%postun
%{clean_menus}

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc README
%{_datadir}/%{name}/*
%{_gamesbindir}/%{name}
%{_iconsdir}/*
%{_menudir}/%{name}
