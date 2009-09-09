Name:		enemylines4
Summary:	A simple futuristic racing game
Version:	1.0
Release:	%mkrel 7
Source0:	http://proj.phk.at/el/4/%{name}-%{version}.tar.bz2
Source10:	%{name}.png
# include assert.h in track.cc to fix build failure - AdamW 2008/02
Patch0:		enemylines4-assert.patch
URL:		http://proj.phk.at/el/4/
Group:		Games/Arcade
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL+
BuildRequires:	SDL_image-devel SDL-devel mesaglut-devel
BuildRequires:  imagemagick

%description
A simple futuristic racing game. Urgent deliveries - Reach goal before
time runs out. Times aren't what they used to be though.
Road conditions are horrible and traffic safety and control systems
have been offline for months.

%prep
%setup -q
%patch0 -p1 -b .assert

%build
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/%{name}/
cp ./data/* %{buildroot}%{_datadir}/%{name}/
install -m755 %{name} -D %{buildroot}%{_gamesbindir}/%{name}

mkdir -p %{buildroot}/%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
install -m644 %{SOURCE10} %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert -scale 32x32 %{SOURCE10} %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16x16 %{SOURCE10} %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Categories=Game;ArcadeGame;
Name=Enemy Lines 4
Comment=A simple futuristic racing game
EOF

%post
%if %mdkversion < 200900
%{update_menus}
%endif
%{update_icon_cache}

%postun
%if %mdkversion < 200900
%{clean_menus}
%endif
%{clean_icon_cache}

%clean 
rm -rf %{buildroot} 

%files 
%defattr(-,root,root)
%doc README
%{_datadir}/%{name}
%{_gamesbindir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
